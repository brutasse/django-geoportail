Installation
============

Requirements
------------

.. _ign-api-access:

IGN's API access
````````````````

The Geoportal API can only be accessed with a key delivered by the IGN.
Depending on what kind of data you need, you will have to setup a free or
paid contract with the French National Geographic Institute. The free
contract gives you access to the maps and aerial photos at the highest
resolution available, which can be all you need.

Fill the online `registration form`_ and get your API key now. Once you've
received your key, add it to your project's settings file:

.. code-block:: python

    GEOPORTAL_API_KEY = 'I will not give you mine, but it is full of numbers'

.. _registration form: https://api.ign.fr/geoportail/registration.do

.. note:: About the API key

   The API key is free, but it's required if you want to use the service. A
   key is bound to a domain but will also work for local development. If you
   apply for a key for the domain ``example.com``, you won't be able to use it
   on ``example.org``. However, you can use it at will for experimenting on
   ``localhost``.

GeoDjango
`````````

We assume here that you have a fully-working GeoDjango environment:

* A spatial database (PostGIS or SpatiaLite)
* The required geospatial libraries

The documentation on how to install this environment can be found on
`GeoDjango's documentation`_.

.. _GeoDjango's documentation: http://geodjango.org/docs/install.html

Once you have a spatial database and a few geographic models you are ready to
install *django-geoportail* itself.

Get the code
------------

The development of *django-geoportail* is done on the `mercurial repository`_
hosted on bitbucket. This is where you can contribute to fix bugs and add new
features. However, the mercurial repository may not be stable all the time.

If you want a stable installation, it is recommended to use the python
package. If you have ``pip`` installed, you can run::

    $ pip install -U django-geoportail

or, if you just have ``easy_install``::

    $ easy_install -U django-geoportail

If you want the development version::

    $ hg clone http://bitbucket.org/bruno/django-geoportail/
    $ cd django-geoportail
    $ python setup.py install

.. _mercurial repository: http://bitbucket.org/bruno/django-geoportail/

Now, *django-geoportail* is available in you python path. You can check the
installation in the django shell of your project::

    $ python manage.py shell
    >>> import geoportal
    >>> geoportal.get_version()
    '0.4.1'

And of course, add ``geoportal`` to your django project's ``INSTALLED_APPS``.
In ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        '...',
        # whatever you already have
        '...',
        'geoportal',
    )

Once you've done it, try to run your tests for the whole project or just
*django-geoportal*:

.. code-block:: bash

    ./manage.py test # for the whole project
    ./manage.py test geoportal # only django-geoportail's tests

If it works as expected (i.e. the tests pass), you're ready to use
*django-geoportail*.

.. _media-files:

Media files
-----------

.. warning:: Optional step

    This step is optional and you probably don't need to do it, unless you
    know what you're doing. This is about serving the Geoportal JS API
    yourself instead of having to rely on the hosted version.

*Django-geoportal* requires a bunch of media files:

* The Geoportal.js library (contains OpenLayers and some custom classes)
* Some static files used when maps are displayed on your site

By default, *django-geoportail* will use the hosted versions of these files on
`api.ign.fr`_. However, if you prefer to host them yourself, you can get them
from the `downloads`_ section of the Geoportal website. Once you've grabbed
the files, put them into a subdirectory of your project's ``MEDIA_ROOT`` and
set ``GEOPORTAL_MEDIA_URL`` to the public URL of this subdirectory in your
project settings:

.. code-block:: python

    GEOPORTAL_MEDIA_URL = 'http://media.example.com/geoportal/'

The trailing slash is required. This directory should contain
``Geoportal.js``, ``GeoportalExtended.js`` and an ``img`` and a ``theme``
directory.

.. _api.ign.fr: http://api.ign.fr
.. _downloads: https://api.ign.fr/geoportail/api/doc/fr/developpeur/download.html
