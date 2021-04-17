Day 14 - Climate Change: Trends in River flows in Estonia
---------------------------------------------------------

.. image:: _static/day-14-climate-change.png

https://twitter.com/allixender/status/1330801820764151810


Data
~~~~

The establishment of the meteorological observatory of the University of Tartu laid the foundation for the hydrological observation network of Estonian inland waters. The observatory first measured the water level of the Emajõgi River in 1866, but more regular measurements began in the spring of 1867. Daily water level and regular flow measurements began on the Emajõgi River in 1922. In the 1920s, regular flow measurements were started on many other Estonian rivers.

From here it is possible to download the daily flow rates or drainage of the operating hydrometry stations. Information about operating stations can be found by clicking on the following link: https://www.ilmateenistus.ee/ilmateenistus/ Vaatlusvork/#hydro

The name of the station is followed by a homogeneous reference period. Long-term average and historical maximum / minimum flow rates have been calculated from the beginning of the uniform observation series for each station until 2015.

- https://www.ilmateenistus.ee/siseveed/ajaloolised-vaatlusandmed/vooluhulgad/

**Testing Mann-Kendall python package to calculate trend for flow timeseries**

- https://joss.theoj.org/papers/10.21105/joss.01556
- https://pypi.org/project/pymannkendall/


The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/14/day-14.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/14>`_.


`Alternative - sea ice data visual <https://ghrc.nsstc.nasa.gov/hydro/details/AU_SI25_NRT_R04>`_

https://twitter.com/allixender/status/1332266269400326145

(Data_archive/data_formats - lab session 2 Map Sea Ice Concentration of 10 days.pdf)

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
