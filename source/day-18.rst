Day 18 - Landuse Copernicus C3S Landcover for Estonia
-----------------------------------------------------

.. image:: _static/day-18-landcover.png

https://twitter.com/allixender/status/1330961744999698432

Data
~~~~

https://cds.climate.copernicus.eu

http://maps.elie.ucl.ac.be/CCI/viewer/download.php


The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/18/day-18.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/18>`_.

.. code::

    0# No Data
    10#Cropland, rainfed
    20#Cropland, irrigated or post-flooding
    30#Mosaic cropland (>50%) / natural vegetation (tree, shrub, herbaceous cover) (<50%)
    40#Mosaic natural vegetation (tree, shrub, herbaceous cover) (>50%) / cropland (<50%)
    50#Tree cover, broadleaved, evergreen, closed to open (>15%)
    60#Tree cover, broadleaved, deciduous, closed to open (>15%)
    70#Tree cover, needleleaved, evergreen, closed to open (>15%)
    80#Tree cover, needleleaved, deciduous, closed to open (>15%)
    90#Tree cover, mixed leaf type (broadleaved and needleleaved)
    100#Mosaic tree and shrub (>50%) / herbaceous cover (<50%)
    110#Mosaic herbaceous cover (>50%) / tree and shrub (<50%)
    120#Shrubland
    130#Grassland
    140#Lichens and mosses
    150#Sparse vegetation (tree, shrub, herbaceous cover) (<15%)
    160#Tree cover, flooded, fresh or brackish water
    170#Tree cover, flooded, saline water
    180#Shrub or herbaceous cover, flooded, fresh/saline/brackishwater
    190#Urban areas
    200#Bare areas
    210#Water bodies
    220#Permanent snow and ice

GDAL extract layer band from netcdf:

.. code::

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:C3S-LC-L4-LCCS-Map-300m-P1Y-2018-v2.1.1.nc:lccs_class C3S-LC-L4-LCCS-Map-300m-P1Y-2018-v2.1.1_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:C3S-LC-L4-LCCS-Map-300m-P1Y-2016-v2.1.1.nc:lccs_class C3S-LC-L4-LCCS-Map-300m-P1Y-2016-v2.1.1_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:ESACCI-LC-L4-LCCS-Map-300m-P1Y-2006-v2.0.7cds.nc:lccs_class ESACCI-LC-L4-LCCS-Map-300m-P1Y-2006-v2.0.7cds_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:ESACCI-LC-L4-LCCS-Map-300m-P1Y-2008-v2.0.7cds.nc:lccs_class ESACCI-LC-L4-LCCS-Map-300m-P1Y-2008-v2.0.7cds_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:ESACCI-LC-L4-LCCS-Map-300m-P1Y-2010-v2.0.7cds.nc:lccs_class ESACCI-LC-L4-LCCS-Map-300m-P1Y-2010-v2.0.7cds_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:ESACCI-LC-L4-LCCS-Map-300m-P1Y-2012-v2.0.7cds.nc:lccs_class ESACCI-LC-L4-LCCS-Map-300m-P1Y-2012-v2.0.7cds_mode.tif

    gdalwarp -of Gtiff -co COMPRESS=LZW -co TILED=YES -ot Byte -r mode -te -180.0000000 -90.0000000 180.0000000 90.0000000 -tr 0.002777777777778 0.002777777777778 -t_srs EPSG:4326 NETCDF:ESACCI-LC-L4-LCCS-Map-300m-P1Y-2014-v2.0.7cds.nc:lccs_class ESACCI-LC-L4-LCCS-Map-300m-P1Y-2014-v2.0.7cds_mode.tif
