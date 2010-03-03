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

If you want the development version::

    $ hg clone http://bitbucket.org/bruno/django-geoportail/
    $ cd django-geoportail
    $ python setup.py install

.. _mercurial repository: http://bitbucket.org/bruno/django-geoportail/

If you want a stable installation, it is recommended to use the python
package. If you have ``pip`` installed, you can run::

    $ pip install -U django-geoportail

or, if you just have ``easy_install``::

    $ easy_install django-geoportail

Now, *django-geoportail* is available in you python path. You can check the
installation in a python shell::

    $ python
    >>> import geoportal
    >>> geoportal.get_version()
    '0.2.1'

If it works as expected, you are almost ready to use *django-geoportail*.
Almost.

Media files
-----------

*Django-geoportal* ships with a bunch of media files:

* The Geoportal.js library (contains OpenLayers and some custom classes)
* Some static files used when maps are displayed on your site

Of course, you have to add those media files to your project.
*Django-geoportal* expects to see those under the <media_url>/geoportal, where
media_url is the MEDIA_URL from your project's settings file.

You can create a symlink or just copy the whole directory to your project's
media directory:

* Using the symlink::

      $ cd /path/to/project/media
      $ ln -s /path/to/site-packages/django-geoportal/media geoportal

* Copying the whole directory::

      $ cd /path/to/project/media
      $ cp -a /path/to/site-packages/django-geoportal/media geoportal

It is recommended to create a symlink to always have up-to-date files when you
update *django-geoportail*. However, depending on your production environment,
you may need to copy the files for the web server to serve them.

You're now ready to start experimenting with *django-geoportail*.
