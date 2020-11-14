Day 10 - Grid comparison of different global grid systems
=========================================================

https://twitter.com/allixender/status/1324055326111485959

.. image:: _static/day-10-grids.png

Data
----

No real data, but grid generators:  I generated the ISEA4H (hexagons), ISEA4T (triangles) and saved as GeoPackage. I did this with the help of a little library I am working on:

https://github.com/allixender/dggrid4py/

It uses GeoPandas and DGGRID - a free software program for creating and manipulating Discrete Global Grids. DGGRID version 7.0 was released in September, 2019.

https://www.discreteglobalgrids.org/software/

Then I used `Uber H3 <https://eng.uber.com/h3/>`_ and MLandcare Cresearch/Manaaki Whenua `RhealPixDGGS-py <https://github.com/manaakiwhenua/rhealpixdggs-py>`_.

Each of these 4 grid systems I generated two subsequent resolutions to depict the "aperture" and parent child spatial relation ships.

Eventually I used `GeoViews <https://geoviews.org/>`_ to provide a static orthographic (say globe) basemap view.

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/10/day-10.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/10>`_.
