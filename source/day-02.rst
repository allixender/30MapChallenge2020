Day 02 - Lines: Estonian rivers and streams by from Estonian Landboard (Maa-Amet)
=======================================================================================


.. image:: _static/day-02-river-lines.png

https://twitter.com/allixender/status/1323293939865104384

Data
----

the layer *E_203_vooluveekogu_j* (lit. translation: flowing water bodies as **lines**) from the file ETAK_EESTI_GPKG.gpkg,
`downloaded in Geopackage <https://geoportaal.maaamet.ee/eng/Maps-and-Data/Estonian-Topographic-Database/Download-Topographic-Data-p618.html>`_ format (GPKG)  ( 1.2G )
under `Estonian Landboard Open Data License <https://geoportaal.maaamet.ee/docs/Avaandmed/Licence-of-open-data-of-Estonian-Land-Board.pdf>`_.

I am using the column *tyyp* which denotes the "magnitude" of the river, i.e.: 50=river, 40=stream ... channel, 10=ditch. The higher the values, the more intense the colour is meant to shine.

https://github.com/allixender/30MapChallenge2020/tree/main/02

- `Geopandas <https://geopandas.org/mapping.html>`_ for reading the Data and pre-processing
- `Datashader <https://datashader.org/>`_ for fancy glow plotting more than 845 000 geometries within a few seconds

What Datashader does, is resampling the hundreds of thousands geometries into a much smaller number of pixels. It is very efficient and optimized,
using things like Dask and Numba under the hood.
Datashader itself exposes a comparatively small `API <https://datashader.org/api.html>`_. However, I struggled to integrate the plotting with
the typical elements I am used from e.g. *matplotlib* , such as title, legend and geographic coordinates.

Suggestions welcome.
