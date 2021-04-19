Day 14 - Climate Change: Sea ice extent around Antarctica
---------------------------------------------------------

.. image:: _static/antartica-10-days.gif

Antarctica in white, and sea water in very light blue. Sea is blue.

https://twitter.com/allixender/status/1332266269400326145


Data
~~~~

`sea ice data visual <https://ghrc.nsstc.nasa.gov/hydro/details/AU_SI25_NRT_R04>`_


- GET DATA: 	https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice25/R04/hdfeos5/
- ALTERNATE ACCESS: 	https://lance.itsc.uah.edu/amsr2-science/data/level3/seaice25/R04/hdfeos5/
- PROJECT HOME PAGE: 	https://earthdata.nasa.gov/earth-observation-data/near-real-time
- DOI: 	http://dx.doi.org/10.5067/AMSRU/AU_SI25_NRT_R04
- CITING DATA: 	https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data

.. code::

    D:\data\seaice_example

    https://nsidc.org/data/AU_SI25/versions/1

    Polar Stereographic South EPSG:3412

    gdal_translate.exe -of Gtiff  -a_srs "+proj=stere +lat_0=-90 +lat_ts=-70 +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378273 +b=6356889.449 +units=m +no_defs" -a_ullr -3950000 4350000 3950000 -3950000 HDF5:"AMSR_U2_L3_SeaIce25km_R04_20201116.he5"://HDFEOS/GRIDS/SpPolarGrid25km/Data_Fields/SI_25km_SH_ICECON_DAY AMSR_U2_L3_SeaIce25km_R04_20201116_icecon_day_3412_tr.tif

    epsg:4312

    lower left x -3950 E, y -3950 S
    upper left x -3950    ulymap 4350

    X (km)  Y (km) Latitude (deg) Longitude (deg) Pixel Location
    -3950 	4350 	-39.23 	317.76 	corner
    0 	4350 	-51.32 	0.00 	midpoint
    3950 	4350 	-39.23 	42.24 	corner
    3950 	0 	-54.66 	90.00 	midpoint
    3950 	-3950 	-41.45 	135.00 	corner
    0 	-3950 	-54.66 	180.00 	midpoint
    -3950 	-3950 	-41.45 	225.00 	corner
    -3950 	0 	-54.66 	270.00 	midpoint

    +proj=stere +lat_0=-90 +lat_ts=-70 +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378273 +b=6356889.449 +units=m +no_defs

    -a_ullr -3950000 4350000 3950000 -3950000


The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/14/day-14.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/14>`_.
