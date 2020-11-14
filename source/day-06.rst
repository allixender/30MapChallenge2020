Day 06 - Red DEM shading of Mars (the red planet)
=================================================

.. image:: _static/day-06-red.png

https://twitter.com/allixender/status/1324670496747696128

Data
----

Mars MGS MOLA DEM 463m v2

https://astrogeology.usgs.gov/search/details/Mars/GlobalSurveyor/MOLA/Mars_MGS_MOLA_DEM_mosaic_global_463m/cub

**Publisher** GeoScience PDS Node

**Author** MOLA Team

**Originator** Goddard Space Flight Center

Only loading the DEM with rasterio and then plotting with EarthPy.

I did a little cheating in QGIS/GDAL though, where I "reprojected" (to give it a working projection for Earth's geospatial tools) and downsampled it to 1km grid resolution, because my Jupyter notebook would run out of memory when doing the hillshading and plotting together. I got a funny message in QGIS that informed me that the on-the-fly reprojection doesn't work, because WGS84 and MARS are not the same celestial bodies :-D Aww, sweet.

https://earthpy.readthedocs.io/en/latest/gallery_vignettes/plot_dem_hillshade.html

https://astrogeology.usgs.gov/search/details/Phobos/MarsExpress/HRSC/Phobos_ME_HRSC_ClrShade_Global_2ppd/cub

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/06/day-06.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/06>`_.
