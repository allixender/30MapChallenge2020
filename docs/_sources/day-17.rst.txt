Day 16-17 - Historical Maps of the Estonian Island of Vormsi
------------------------------------------------------------

.. image:: _static/day-17-historical.gif

https://twitter.com/tjukanov/status/1311568912950140930

Data
~~~~

Estonian Land Board / Maa-Amet hosts a rich collection of old and new layers available as WMS service.

- https://geoportaal.maaamet.ee/eng/Services/Public-WMS-Service-p346.html

I am using the crafty `OWSlib package <https://geopython.github.io/OWSLib/#wms>`_ to download images for the same extent (Vormsi island, Estonia)

Then I use Python ``imageio`` to join them to a GIF file.

The Jupyter notebook `(view here) <https://nbviewer.jupyter.org/github/allixender/30MapChallenge2020/blob/main/17/day-17.ipynb>`_ is provided in my `GitHub repo <https://github.com/allixender/30MapChallenge2020/tree/main/17>`_.
