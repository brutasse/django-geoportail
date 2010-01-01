from django.contrib.gis import admin
from django.conf import settings


if not hasattr(settings, 'GEOPORTAL_API_KEY'):
    # Just raising a warning, it's not fatal after all
    import warnings
    warnings.warn("GEOPORTAL_API_KEY could not be found in your settings. It is necessary to get maps to work.")


class GeoPortalAdmin(admin.GeoModelAdmin):
    """A base model for displaying a GeoPortal admin map"""
    ##############
    # Public API #
    ##############

    map_width = 600  # Dimensions of the
    map_height = 400 # map (pixels)

    max_zoom = 20    # Zoom levels: 20 = finest
    min_zoom = 0     #               0 = world
    point_zoom = 15  # Default zoom level for a single point

    default_zoom = 5 # display a whole country

    default_lon = 2  # Default location
    default_lat = 47 # is France

    # Show map info or not (broken atm)
    map_info = True

    # Layers
    layers = 'auto' # Show the default set of layers provided by GeoPortal
    #layers = (
        # ('code', opacity),
        # Order matters, layers are added in this order.
        #('photos', 1),
        #('maps', 1),
    #)

    ###############
    # Private API #
    ###############
    map_template = 'gis/admin/geoportal.html'
    wms_url = 'http://wxs.ign.fr/geoportail/wmsc'
    openlayers_url = 'geoportal/GeoportalExtended.js'

    # Display the layer switcher
    layerswitcher = False

    # Mouse position: already displayed by Geoportail
    mouse_position = False
    # Same for scale
    scale_text = False


    _layers = {
        # See https://api.ign.fr/geoportail/api/doc/fr/webmaster/layers.html
        # for an explanation of the meaning of each layer.

        # The layers can or cannot be accessed depending on your API contract.
        'photos': 'ORTHOIMAGERY.ORTHOPHOTOS:WMSC',
        'maps': 'GEOGRAPHICALGRIDSYSTEMS.MAPS:WMSC',
        'terrain': 'ELEVATION.SLOPS',
        'cadaster': 'CADASTRALPARCELS.PARCELS',
        'hydrography': 'HYDROGRAPHY.HYDROGRAPHY',
        'roads': 'TRANSPORTNETWORKS.ROADS',
        'railways': 'TRANSPORTNETWORKS.RAILWAYS',
        'runways': 'TRANSPORTNETWORKS.RUNWAYS',
        'buildings': 'BUILDINGS.BUILDINGS',
        'gov': 'UTILITYANDGOVERNMENTALSERVICES.ALL',
        'boundaries': 'ADMINISTRATIVEUNITS.BOUNDARIES',
        'coast': 'SEAREGIONS.LEVEL0',
    }

    def get_layers(self):
        if self.layers == 'auto':
            # forcing layerswitcher display
            self.layerswitcher = True
            return self.layers
        lyrs = []
        for (key, value) in self.layers:
            lyrs.append({
                'name': self._layers[key],
                'resource_name': self._layers[key].split(':')[0],
                'opacity': value,
            })
        return lyrs

    def get_map_widget(self, db_field):
        widget = super(GeoPortalAdmin, self).get_map_widget(db_field)
        widget.params['map_info'] = self.map_info
        widget.params['layers'] = self.get_layers()
        widget.params['api_key'] = settings.GEOPORTAL_API_KEY
        return widget
