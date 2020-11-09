Day 08 - Yellow Global mining areas
===================================

.. image:: _static/day-08-yellow.png

https://twitter.com/allixender/status/1325532260171444229

Data
----

Maus, V., Giljum, S., Gutschlhofer, J. et al. A global-scale data set of mining areas. Sci Data 7, 289 (2020). https://doi.org/10.1038/s41597-020-00624-w

https://www.nature.com/articles/s41597-020-00624-w

https://doi.pangaea.de/10.1594/PANGAEA.910894

Then I generated the ISEA4T DGGS at level 5, ca. 20000 triangles, and saved as GeoPackage. I did this with the help of a little library I am working on:

https://github.com/allixender/dggrid4py/

It uses GeoPandas and DGGRID - a free software program for creating and manipulating Discrete Global Grids. DGGRID version 7.0 was released in September, 2019.

https://www.discreteglobalgrids.org/software/

From GeoPandas I took the *lowres_naturalearth* dataset to retain only those triangles for the areas of landmass.
Then I did a spatial left join (based on intersect) to aggregate the mining polygon data (esp. *AREA*) into the triangle grid.

Eventually I used `GeoViews <https://geoviews.org/>`_ to provide a static orthographic (say globe) basemap view.

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/08/day-08.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/08>`_.
