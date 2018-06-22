gaugesrv
========

A simple gauge web service/visualization using gauge.js.

Currently under development.  The way to get this demo installed and
running may be done using the following commands:

.. code::

    $ git clone https://github.com/metatoaster/gaugesrv.git
    $ cd gaugesrv
    $ pip install -e .[dev,webpack,scss]
    $ calmjs npm --install -i -D gaugesrv[dev,webpack,scss]
    $ python setup.py build
    $ gaugesrv-demo

Connect a web browser to http://localhost:8000 to view the demo once
everything is successfully installed.

For running the tests for of both Python and JavaScript code shipped
with this project, run the following (provided that the ``dev`` extras
were installed, which the above instructions will do so.:

.. code::

    $ python -m unittest gaugesrv.tests.make_suite
    $ calmjs karma webpack -w gaugesrv

RequireJS may be used, however the default app is not set up to include
the RequireJS boilerplates needed for the system to work, but if the
``rjs`` extras is also specified in the relevant install commands, the
dependencies will be pulled and the ``calmjs rjs`` command may be used
to generate the artifacts.
