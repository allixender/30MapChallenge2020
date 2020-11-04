Day 04 - Hexagons: NASA GPWv4 global population density in ISEAH7 DGGS Hexagons
===============================================================================

#30DayMapChallenge 4 - Hexagons: #NASAsedac #GPWv4 global population density sampled into proper #DGGS in #ISEAH7 (level 4) projection with #DGGRID, #dggrid4py, #rasterio / #rasterstats and @geopandas and visualised with #GeoViews @holoviz_org

https://twitter.com/allixender/status/1324055326111485959

.. image:: _static/day-04-hexa.png

Data
----

NASA Sedac GPWv4 global population density:

https://sedac.ciesin.columbia.edu/data/collection/gpw-v4

Then I generated the ISEAH7 DGGS at level 4, ca. 24000 hexagons, and saved as GeoPackage. I did this with the help of a little library I am working on:

https://github.com/allixender/dggrid4py/

It uses GeoPandas and DGGRID - a free software program for creating and manipulating Discrete Global Grids. DGGRID version 7.0 was released in September, 2019.

https://www.discreteglobalgrids.org/software/

Then I used `Rasterio <https://rasterio.readthedocs.io/en/latest/>`_ and `Rasterstats <https://pythonhosted.org/rasterstats/>`_ to summarize (mean) the population density data into the hexagon features. Subsequently I classified the data with `PySAL's mapclassify <https://pysal.org/mapclassify/>`_ due to it's large range of values.

Eventually I used `GeoViews <https://geoviews.org/>`_ to provide a static orthographic (say globe) basemap view.

The notebook is provided here:

https://github.com/allixender/30MapChallenge2020/tree/main/04
