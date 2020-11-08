Day 08 - Yellow Global mining areas
===================================

.. image:: _static/day-08-yellow.png

Data
----

Maus, V., Giljum, S., Gutschlhofer, J. et al. A global-scale data set of mining areas. Sci Data 7, 289 (2020). https://doi.org/10.1038/s41597-020-00624-w

https://www.nature.com/articles/s41597-020-00624-w

https://doi.pangaea.de/10.1594/PANGAEA.910894

Then I generated the ISEAH7 DGGS at level 4, ca. 24000 hexagons, and saved as GeoPackage. I did this with the help of a little library I am working on:

https://github.com/allixender/dggrid4py/

It uses GeoPandas and DGGRID - a free software program for creating and manipulating Discrete Global Grids. DGGRID version 7.0 was released in September, 2019.

https://www.discreteglobalgrids.org/software/

Eventually I used `GeoViews <https://geoviews.org/>`_ to provide a static orthographic (say globe) basemap view.

The notebook is provided here:

https://github.com/allixender/30MapChallenge2020/tree/main/08
