gaugesrv
========

A simple gauge web service/visualization using gauge.js.

Currently under development.  The way to get this demo running is
roughly the following:

.. code::

    $ git clone https://github.com/metatoaster/gaugesrv.git
    $ pip install -e .[dev,webpack,scss]
    $ calmjs npm --install -i gaugesrv[dev,webpack,scss]
    $ python setup.py build && python -m gaugesrv.app
