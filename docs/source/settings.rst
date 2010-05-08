Overriding default settings
===========================

*Django-geoportal* shares a few common settings between the template API and
the admin API. They are defined in ``geoportal.utils`` and luckily they are
easy to override from your project.

*Django-geoportail* checks if those settings are defined in your Django
project settings, and if no value is found it provides a default value. All
the settings are prefixed by ``GEOPORTAL_`` to avoid conflicts with other
apps.

If you override a setting, its value will be used in the admin, the template
system and the forms library, given that you haven't set it manually in the
admin class or in the templatetag/widget options.

.. _settings-ref:

Settings reference
------------------

* ``GEOPORTAL_POINT_ZOOM``: the zoom value when a single point is displayed
  on a map. Default: ``14``.

* ``GEOPORTAL_DEFAULT_LON``: the longitude of a new map. Default: ``2``.

* ``GEOPORTAL_DEFAULT_LAT``: the latitude of a new map. Default: ``47``.

* ``GEOPORTAL_DEFAULT_ZOOM``: the zoom level of a new map. Default: ``5``.

* ``GEOPORTAL_DEFAULT_WIDTH``: the width of a map in the admin or in a
  template. Default: ``600``.

* ``GEOPORTAL_DEFAULT_HEIGHT``: the height of a map in the admin or in a
  template. Default: ``400``.

* ``GEOPORTAL_DEFAULT_COLOR``: the color of the drawing feature in the admin
  widget or the template map, in ``rrggbb`` format. Default: ``'ee9900'``, a
  light orange (OpenLayer's default value).

* ``GEOPORTAL_DEFAULT_OPACITY``: the opacity of the inner part of a surface in
  the admin or the template maps. Default: ``0.4`` (OpenLayer's default
  value).

* ``GEOPORTAL_API_KEY`` is a required setting and no map will show up until
  you set it to the key given by the IGN. See :ref:`ign-api-access`.

* ``GEOPORTAL_MEDIA_URL`` points to the Geoportal Javascript library. The
  default value is ``http://api.ign.fr/geoportail/api/js/1.0/``, which is the
  hosted version. If you want to host it yourself, see :ref:`media-files`.
