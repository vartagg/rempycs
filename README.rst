Python .pyc remover
===================



Simple Python .pyc files remover.


License
-------

Free software: BSD license

Features
--------

Remove all .pyc files having .py analogs from current place by walking on all subdirectories.
Ignores files whose names begin with "." ("hidden" files in UNIX systems).


Installation
------------

.. code:: bash

    $ pip install rempycs


Usage
-----

.. code:: bash

    $ cd /directory_with_python_sources
    $ rempycs
