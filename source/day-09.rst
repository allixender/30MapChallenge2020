Day 09 - Monochrome Stream Delineation
--------------------------------------

.. image:: _static/day-09_monochrome.png

https://twitter.com/allixender/status/1325843393050710016

Data
~~~~

The DEM is a pre-clipped and reprojected (in QGIS) GeoTiff from the awesome MERIT-Hydro global hydrologically pre-processed DEM:

http://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_Hydro/

It would be quite straight-forward to do the clipping and reprojecting in Rasterio, too (e.g. `here <https://kodu.ut.ee/~kmoch/geopython2019/L4/raster.html#reproject-a-raster>`_).

But now we do an actual fully scripted stream delineation in Python with PySheds:

https://github.com/mdbartos/pysheds

https://www.hatarilabs.com/ih-en/watershed-and-stream-network-delimitation-with-python-and-pysheds-tutorial


Hillshade with Earthpy: https://earthpy.readthedocs.io/en/latest

Plotting it all together wit hsome Seaborn and Matplotlib color tinkering.

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/09/day-09.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/09>`_.

It would be interesting to redo the exercise with e.g. `pygeoprocessing <https://github.com/natcap/pygeoprocessing>`_
