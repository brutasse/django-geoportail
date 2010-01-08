=================
Django-Geoportail
=================

Geodjango with the maps and photos from the French National Geographic
Institute.

* Installation: see INSTALL

* Get involved: http://bitbucket.org/bruno/django-geoportail/

* Bugs: http://bitbucket.org/bruno/django-geoportail/issues/

Quickstart
==========

Add some maps to your django sites...

Known Issues
------------

The maps are not displayed properly for Multi* fields:

* MultiPointField

* MultiLineStringField

* MultiPolygonField

* (untested) GeometryCollectionField

In those cases, the objects will be displayed on the map but the map won't be
automatically focused to the objects when you try to edit existing objects.
You'll have to find them manually. Editing works.

In the admin
------------

To register a geographic model, add those lines to your <app_dir>/admin.py::

    from geoportal.admin import GeoPortalAdmin
    from django.contrib.gis import admin
    from my_app.models import MyModel

    admin.site.register(MyModel, GeoPortalAdmin)

If you need some customization, you can easily override the GeoPortalAdmin
class::

    class MyGeoAdmin(GeoPortalAdmin):
        # Your options here

Available options are:

* ``map_width``: the width of the map (in pixels). Default: 600

* ``map_height``: the height of the map, still in pixels. Default: 400

* ``default_zoom``: the zoom level when a new empty map is created. Default: 5

* ``default_lon``: default longitude for a new map. Default: 2

* ``default_lat``: default latitude for a new map. Default: 47.
  ``default_lon``, ``default_lat`` and ``default_zoom`` are set to display a
  map centered on France with the whole country.

* ``point_zoom``: the zoom level to select when you see a single point.
  Default: 15, for a 1:25000 map (best resolution available)

* ``map_info`` (broken atm): show Geoportal's scale and coordinates widget.
  Default: True

* ``layers``: customize the layers. Default: 'auto'. Could be either:

  * 'auto': automatically fill the map with a combination of the available
    layers (maps, photos...).
  * A 2-tuple tuple: ``( ('code', opacity), (..., ...), )``. ``code`` is the
    codename of the layer you want to display, ``opacity`` is its opacity,
    between 0 and 1.

    The order is important, the layers are added to the map in the same order
    as they are defined. If you add a layer with an opacity set to 1 to some
    previously added layers, this will hide the previous layers.

    Available layers are:

    * 'photos'
    * 'maps'
    * 'terrain': elevation map
    * 'cadaster': cadastral parcels
    * 'hydrography'
    * 'roads'
    * 'railways'
    * 'runways'
    * 'buildings'
    * 'gov': utility and governmental services
    * 'boundaries': adminstrative boundaries
    * 'coast': sea regions

    Note that layers may or may not be available depending on your API key.
    The free contract gives you only 'photos' and 'maps'.

    For more information about the different layers, please visit:
    https://api.ign.fr/geoportail/api/doc/fr/webmaster/layers.html

In your templates
-----------------

(not yet)
