Day 03 - Polygons: Reported average through crimes and offense in Tallinn, Estonia
==================================================================================


.. image:: _static/day-03-polys.png

Data
----

It is a dataset provided by the Information Technology and Development Center of the Ministry of the Interior of Estonia  (SMIT).  SMIT is the largest IT institution in the country, which creates and manages information systems necessary for saving lives and ensuring internal security. The data contains anonymised records of crimes, felonies and other offenses against the law.
The data is binned into squares of either 500mx500m or 1000mx1000m.

- https://opendata.riik.ee/et/dataset/avaliku-korra-vastased-ja-avalikus-kohas-toime-pandud-syyteod
- https://opendata.smit.ee/ppa/csv/avalik_3.csv

In addition I took the Administrative-and-Settlement-Divisions dataset from the Estonian Landboard and only took the Tallinn area.

- https://geoportaal.maaamet.ee/eng/Spatial-Data/Administrative-and-Settlement-Division-p312.html
- https://geoportaal.maaamet.ee/docs/haldus_asustus/asustusyksus_shp.zip?t=20201101020927
- https://geoportaal.maaamet.ee/index.php?lang_id=2&page_id=663

Most challenging was the pre-processing of the crime dataset. As the polygons (squares) are a bit too small to look great on Estonian national level, I decided to overlay it on the Tallinn city and sub-urban area. In addition I classified the data with `PySAL's mapclassify <https://pysal.org/mapclassify/>`_ and used `Contextily <https://contextily.readthedocs.io/en/latest/>`_ to provide a static basemap.

Again the main work is done with Pandas/GeoPandas and matplotlib.

The notebook is provided here:

https://github.com/allixender/30MapChallenge2020/tree/main/03
