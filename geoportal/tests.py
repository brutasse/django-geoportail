from django.contrib.gis.db import models
from django.template import Template, TemplateSyntaxError
from django.test import TestCase

import geoportal


BASE_TEMPLATE = """
{%% load geoportal_tags %%}
{%% geoportal_map geo_field %s %%}
"""


class GeoportalUtilsTest(TestCase):
    def test_utils(self):
        self.assertEquals(len(geoportal.utils.LAYERS), 12)

    def test_get_layers(self):
        layers = (('maps', 1),)
        geo_layers = geoportal.utils.get_layers(layers)
        self.assertEquals(len(geo_layers), 1)
        self.assertEquals(geo_layers[0]['resource_name'],
                          'GEOGRAPHICALGRIDSYSTEMS.MAPS')

        layers = (('photos', 1), ('maps', 0.3))
        geo_layers = geoportal.utils.get_layers(layers)
        self.assertEquals(len(geo_layers), 2)
        self.assertEquals(geo_layers[0]['resource_name'],
                          'ORTHOIMAGERY.ORTHOPHOTOS')


class TestModel(models.Model):
    """A model which is not in the DB but we can use it in our templatetags"""
    point = models.PointField()
    line = models.LineStringField()
    polygon = models.PolygonField()


class GeoTemplateTest(TestCase):
    def setUp(self):
        self.geo_model = TestModel(
            point='POINT (6.8643511274086046 45.8325858329590829)',
            line='LINESTRING (-4.8687808591351045 48.5177935040483490, -3.9600705509226786 48.7201659712547794, -3.6126224919002792 48.6833709772172654)',
            polygon='POLYGON((1.1981967868713883 48.59138349212341,1.331830655726157 46.714838796209094,6.062469613184964 46.64124880813403,4.9666718885758625 48.70176847423602,1.1981967868713883 48.59138349212341))'
        )

    def tearDown(self):
        pass

    def test_simple_template(self):
        context = {'geo_field': self.geo_model.point}
        rendered = Template(BASE_TEMPLATE % '').render(context)
        self.assertTrue(str(self.geo_model.point) in rendered)

    def test_template_with_options(self):
        context = {'geo_field': self.geo_model.line}
        rendered = Template(BASE_TEMPLATE % 'width=120, height=150').render(context)
        self.assertTrue(str(self.geo_model.line) in rendered)

    def test_invalid_template(self):
        context = {'geo_field': self.geo_model.line}
        self.assertRaises(TemplateSyntaxError,
                lambda: Template(BASE_TEMPLATE % 'some_option=some_value'))

    def test_template_with_variable(self):
        context = {'geo_field': self.geo_model.polygon,
                   'map_width': 200,
                   'map_height': 400}
        rendered = Template(BASE_TEMPLATE % 'width=map_width, height=map_height').render(context)
        self.assertTrue('width: 200px; height: 400px;' in rendered)
        self.assertTrue(str(self.geo_model.polygon) in rendered)

    def test_invisible_feature(self):
        context = {'geo_field': self.geo_model.polygon}
        rendered = Template(BASE_TEMPLATE % 'visible=0').render(context)
        # This is the line that adds the feature to the map
        # (should not be here)
        self.assertFalse('.viewer.map.addLayer(' in rendered)

    def test_as_var_name(self):
        context = {'geo_field': self.geo_model.polygon}
        rendered = Template(BASE_TEMPLATE % 'as some_variable').render(context)

        # This is a 5-char random string
        self.assertEquals(len(context['some_variable']), 5)
