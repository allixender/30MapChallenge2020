Day 11 - 3D Elevation as scientific surface plot
------------------------------------------------

.. image:: _static/day-11-3d.png

https://twitter.com/allixender/status/1325843393050710016

Data
~~~~

The DEM is a pre-clipped and reprojected (in QGIS) GeoTiff from the awesome MERIT-Hydro global hydrologically pre-processed DEM:

http://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_Hydro/

It would be quite straight-forward to do the clipping and reprojecting in Rasterio, too (e.g. `here <https://kodu.ut.ee/~kmoch/geopython2020/L5/raster.html#reproject-a-raster>`_).

For the scientific plot style I experimented with the `HoloViews python package <https://holoviews.org/gallery/demos/matplotlib/surface_3d.html#demos-matplotlib-gallery-surface-3d>`_ using a Surface3D and `Scatter3D plot <http://holoviews.org/reference/elements/matplotlib/Scatter3D.html>`_.

That's all, folks :-)

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/11/day-11.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/11>`_.
