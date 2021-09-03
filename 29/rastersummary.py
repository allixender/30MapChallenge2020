# -*- coding: utf-8 -*-
"""
/***************************************************************************

 Summarizes raster statistics in parallel from grids to polygons
                             -------------------
        copyright            : (C) 2018-2020 by Alexander Kmoch
        email                : alexander.kmoch at ut.ee
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the MIT License                                 *
 *                                                                         *
 ***************************************************************************/
"""
from dask.distributed import Client
import geopandas as gpd

import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import fiona  # type: ignore
from fiona.crs import from_epsg # type: ignore
import fiona
import datetime

from rasterstats import zonal_stats


if __name__ == "__main__":
    # client = Client()
    client = Client(processes=True,
                    n_workers=6,
                    threads_per_worker=1,
                    memory_limit='16GB')

    print(client.scheduler_info()['services'])

    base_path = 'D:/data/ECMWF_CCI_Landuse'

    # twi_5m_estonia.tif tri_5m_estonia.tif tri_5m_estonia.tif ls_faktor_5m_estonia.tif
    rastergrids = {
        'lulc2006': 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2006-v2.0.7cds_mode.tif',
        'lulc2008': 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2008-v2.0.7cds_mode.tif',
        'lulc2010': 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2010-v2.0.7cds_mode.tif',
        'lulc2012': 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2012-v2.0.7cds_mode.tif',
        'lulc2014': 'ESACCI-LC-L4-LCCS-Map-300m-P1Y-2014-v2.0.7cds_mode.tif',
        'lulc2016': 'C3S-LC-L4-LCCS-Map-300m-P1Y-2016-v2.1.1_mode.tif',
        'lulc2018': 'C3S-LC-L4-LCCS-Map-300m-P1Y-2018-v2.1.1_mode.tif'
    }

    raster_file_collection = []

    template_raster_conf = {
        'variable_name': 'lulc2006',
        'actual_file_ref': 'D:/data/ECMWF_CCI_Landuse/ESACCI-LC-L4-LCCS-Map-300m-P1Y-2006-v2.0.7cds_mode.tif'
    }


    for layer_type in rastergrids.keys():
        file_name = f"{rastergrids[layer_type]}"
        try:
            with open(f"{base_path}/{file_name}", 'r') as fh:
                # Load configuration file values
                print(file_name)
                template_raster_conf = {
                    'variable_name': layer_type,
                    'actual_file_ref': f"{base_path}/{file_name}"
                }
                raster_file_collection.append(template_raster_conf)
        except FileNotFoundError:
            # Keep preset values
            print("NOT " + f"{rastergrids[layer_type]}")

    geom_template = (f"{base_path}/ISEA7H_5.gpkg", 'ISEA7H_5_crosstouch')

    print("reading in template geoms")

    geom_template_df = gpd.read_file(geom_template[0], layer=geom_template[1], driver='GPKG', encoding='utf-8')

    refdf_scattered = client.scatter(geom_template_df, broadcast=True)

    def inner_raster_summary(raster_conf_dict, scattered_df):

        print("Starting with {} at {}".format(raster_conf_dict['actual_file_ref'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        variable_name = raster_conf_dict['variable_name']
        actual_file_ref = raster_conf_dict['actual_file_ref']

        tif_src = actual_file_ref

        parquet_tmp_out = f"{base_path}/{variable_name}_zonal_stats.parquet.gzip"

        print("zonal stats")
        outputs = zonal_stats(scattered_df['geometry'],
                tif_src,
                stats="majority",
                # geojson_out=True,
                nodata=0,
                all_touched=True)

        print("output df preps")
        geo_stats_df = pd.DataFrame(outputs)
        print(geo_stats_df.columns)

        var1_name = f"{variable_name}"

        geo_stats_df.rename(columns={'majority': var1_name}, inplace=True)

        print(geo_stats_df.columns)

        geom_df = pd.concat([scattered_df, geo_stats_df], axis=1)
        geom_df.drop(columns=['geometry'], inplace=True)
        geom_df = geom_df[['Name', var1_name]]
        geom_df.set_index('Name', inplace=True)

        print("writing {} at {}".format(parquet_tmp_out, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        geom_df.to_parquet(parquet_tmp_out, compression='gzip', engine='pyarrow')

        del(geom_df)
        del(outputs)
        del(geo_stats_df)

        return f"{parquet_tmp_out} written"

    futures = [client.submit(inner_raster_summary, raster_conf_obj, refdf_scattered) for raster_conf_obj in raster_file_collection]
    # futures = client.map(inner_raster_summary, raster_file_collection)(refdf_scattered)
    results = client.gather(futures)
    for i in results:
        print(i)


    layer1 = gpd.read_file(geom_template[0], layer=geom_template[1], driver='GPKG', encoding='utf-8')
    layer1.set_index('Name', inplace=True)

    for layer in rastergrids.keys():
        parquet_tmp_out = f"{base_path}/{variable_name}_zonal_stats.parquet.gzip"
        next_layer = pd.read_parquet(parquet_tmp_out)

        layer1 = layer1.join(next_layer, how='inner')

    layer1.to_file(geom_template[0], layer=f"{geom_template[1]}_lulc", driver='GPKG', encoding='utf-8')
