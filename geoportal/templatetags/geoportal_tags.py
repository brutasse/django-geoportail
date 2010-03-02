from django import template
from django.conf import settings

from django.contrib.gis.gdal import OGRGeomType

from geoportal import utils

import itertools
import random

register = template.Library()


class MapNode(template.Node):
    def __init__(self, args):
        self.geo_field = template.Variable(args[1])
        self.options = {}
        if len(args) > 2:
            # Eating empty options, u''
            options = [o for o in ''.join(args[2:]).split(',') if o]
            for o in options:
                key, value = o.split('=')
                available = ('width', 'height', 'visible', 'color',
                             'opacity', 'zoom')
                if not key in available:
                    raise template.TemplateSyntaxError('"%s" option is not su'
                            'pported. Available options are: %s' % (key,
                            ', '.join(available)))
                self.options[key] = value

    def render(self, context):
        # Generate a probably unique name for javascript variables -- in case
        # there are several maps on a page
        map_var = ''.join(random.sample('abcdefghijklmopqrstuvwxyz', 5))

        # Field type
        geo_field = self.geo_field.resolve(context)
        ftype = geo_field.geom_type.upper()
        is_collection = ftype in ('MULTIPOINT', 'MULTILINESTRING',
                                  'MULTIPOLYGON', 'GEOMETRYCOLLECTION')
        if is_collection:
            if ftype == 'GEOMETRYCOLLECTION': collection_type = 'Any'
            else: collection_type = OGRGeomType(ftype.replace('MULTI', ''))
        else:
            collection_type = 'None'

        # Default options
        if not 'width' in self.options:
            self.options['width'] = utils.DEFAULT_WIDTH

        if not 'height' in self.options:
            self.options['height'] = utils.DEFAULT_HEIGHT

        if not 'color' in self.options:
            self.options['color'] = utils.DEFAULT_COLOR;

        if not 'opacity' in self.options:
            self.options['opacity'] = utils.DEFAULT_OPACITY

        if not 'visible' in self.options:
            self.options['visible'] = True
        elif self.options['visible'].lower() in ('false', '0', 'f'):
            self.options['visible'] = False

        # Completely isolated context
        isolated_context = template.Context({
            'options': self.options,
            'api_key': settings.GEOPORTAL_API_KEY,
            'MEDIA_URL': settings.MEDIA_URL,
            'map_var': 'map_%s' % map_var,
            'is_point': ftype in ('POINT', 'MULTIPOINT'),
            'is_linestring': ftype in ('LINESTRING', 'MULTILINESTRING'),
            'is_polygon': ftype in ('POLYGON', 'MULTIPOLYGON'),
            'is_collection': is_collection,
            'collection_type': collection_type,
            'layers': utils.get_layers((('maps', 1),)),
            'default_lon': utils.DEFAULT_LON,
            'default_lat': utils.DEFAULT_LAT,
            'default_zoom': utils.DEFAULT_ZOOM,
            'point_zoom': utils.POINT_ZOOM,
            'srid': 4326,
            'field_name': ftype.capitalize(),
            'wkt': geo_field.wkt,
            'wms_url': utils.WMS_URL,
        })
        loaded = template.loader.get_template('geoportal/map.html')
        return loaded.render(isolated_context)


@register.tag
def geoportal_map(parser, token):
    """
    {% geoportal_map field option1=value1, option2=value2, ... %}

    Renders a geographic field (point, polygon, path...)

    Options:             Default
     * width (pixels)    400
     * height (pixels)   300
     * visible (1|0)     1
     * color (rrggbb)    ee9900 (OpenLayers.Feature.Vector.style["default"]["fillColor"])
     * opacity (0 -> 1)  0.4
     * zoom (~3 -> 14)   if not provided, calculated automatically
    """
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError('geoportal_map takes at least one '
                                           'argument')
    return MapNode(bits)
