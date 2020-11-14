Day 05 - Blue Cornflower distribution Centaurea cyanus
------------------------------------------------------

The Blue Cornflower is also a National Estonian symbol.

.. image:: _static/day-05-blue.png

https://twitter.com/allixender/status/1324476330143064064

Data
~~~~

https://www.gbif.org/

Searched for "Centaurea cyanus", almost 100.000 specimen locations

Citation
~~~~~~~~

    GBIF.org (05 November 2020) GBIF Occurrence Download https://doi.org/10.15468/dl.qvcqpv

License
~~~~~~~

    CC BY-NC 4.0

Other places to look for would be
are the Estonian repositories PlutoF and Elurikkus (thanks Jaan and Yiming for inspiration and hints to data):

https://elurikkus.ee/generic-hub/occurrences/search?taxa=+Centaurea+cyanus+&sort=occurrence_date&dir=desc&pageSize=#records

https://plutof.ut.ee/#/search?module=observation&page_size=50&page=1&q=Centaurea+cyanus&parent_taxon=true&columns=name%2Clm%2Cow

Apparently, a challenge with these data (also the GBIF data) is that, many plant species are surveyed in 10km squares (eg. https://plutof.ut.ee/#/observation/view/4142487 ). The coordinates provided then are mostly represented as the centre of the polygon instead of the accurate point of the plant (but there could be also some accurate records).

A quite simple workflow: geocoding the latitudes and longitudes to shapely points, creating a GeoPandas GeoDataFrame, clipping to Estonia and plotting as a Kernel Density Plot with contours - a functionality kindly provided by `Geoplot <https://residentmario.github.io/geoplot/index.html>`_. As usual, a lot of time goes on testing the styling.

I probably could have better inverted the blue colormap and adjust the darker blue hues to be still visible. A matter of intuitive interpretation of the image: Is lighter where is more density or where it is darker? And as we talk about the Blue Cornflower, should it be more blue where there were more records? Well, a lesson for another time.

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/05/day-05.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/05>`_.
