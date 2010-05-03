The Forms library
=================

*django-geoportail* ships with rich form widgets, on which your users can draw
geographic features. The forms library extends Django's built-in library, and
switching to django-geoportail's form library is as simple as changing:

.. code-block:: python

    from django import forms

to:

.. code-block:: python

    from geoportal import forms

All the fields and widgets from django's form library are available, plus a
set of geographic fields and widgets. All the geographic widgets require
javascript, so you have to make sure your users have it enabled.

Like with the template library, you need to load the javascript library each
time you render a rich geographic widget in a template. See :ref:`load-js`

Fields
``````

The following fields are available. Each field correspond to a geographic
model field.

* PointField

* MultiPointField

* LineStringField

* MultiLineStringField

* PolygonField

* MultiPolygonField

Basic usage
```````````

Suppose you need a simple form to let users enter a name and point to a
location on a map. The form can be written as follows.

.. code-block:: python

    from geoportal import forms

    class LocationForm(forms.Form):
        name = forms.CharField(max_length=200)
        location = forms.PointField()

When the form is rendered in the template, a map is displayed and the user can
draw a point on the map. The drawn feature will be validated as a geographic
field and can be saved to the database.

Integration with ``ModelForm`` 's
`````````````````````````````````

Let's define a model with some geographic fields and generate a ``ModelForm``
for it:

.. code-block:: python

    # models.py
    from django.contrib.gis.db import models

    class Location(models.Model):
        name = models.CharField(max_length=255)
        point = models.PointField()

Unfortunately, it is not possible to automatically generate a rich widget for
geographic fields (geodjango already sets the default widget to a
``<textarea>``). However, it is very simple to change the default widget to a
rich one:

.. code-block:: python

    # forms.py
    from geoportal import forms
    from models import Location

    class LocationForm(forms.ModelForm):
        point = forms.PointField()
        class Meta:
            model = Location

Using a ``ModelForm`` and overriding the widget for geographic fields can be
easier than manually declaring all the different fields.

Customizing the form widget
```````````````````````````

By default, all geographic widgets use the default or overridden settings for
rendering the form fields (see :ref:`settings-ref`). Those settings can be
overridden on a per-widget basis to allow better customization. This is done
by manually specifying the widget instance with its options to the form field.

The following widgets are available:

* PointWidget

* MultiPointWidget

* LineStringWidget

* MultiLineStringWidget

* PolygonWidget

* MultiPolygonWidget

Each field has its default widget: a ``PointField`` has a ``PointWidget``, a
``MultiPolygonField`` has a ``MultiPolygonWidget`` and so on. When you specify
the widget, make sure it corresponds to the type of the field.

The following attributes can be passed to a form widget:

* ``width``: the width of the map, in pixels.

* ``height``: the height of the map, in pixels.

* ``color``: the color of the drawn feature, in ``rrggbb`` format.

* ``opacity``: the opacity of the inner part of the feature (for polygons),
  between 0 and 1.

* ``default_zoom``: the zoom level for a form field with no value.

* ``default_lon``: the longitude for a form field with no value.

* ``default_lat``: the latitude for a form field with no value.

* ``layers``: the layers to display on the map. See :ref:`admin-ref` for
  the syntax.

* ``srid``: the ``SRID`` to use with this field.

Let us rewrite the previous form to customize the map:

.. code-block:: python

    # forms.py
    from geoportal import forms
    from models import Location

    class LocationForm(forms.ModelForm):
        point = forms.PointField(widget=forms.PointWidget(attrs={
                'width': 300,
                'height': 300,
                'srid': 900913,
                'layers': (
                            ('maps', 1),
                            ('photos', 0.3)
                          ),
                },
        ))
        class Meta:
            model = Location

While the syntax can be a little verbose, it allows a lot of customization.
Also, remember to set the default settings: if you need to display 500x300px
maps in the admin, the templates and the forms, set it in your settings and
you'll never have to specify it again.
