from geoportal import utils, admin, templatetags, forms

VERSION = (0, 4, 5)

get_version = lambda: '.'.join(map(str, VERSION))

__all__ = ['utils', 'admin', 'templatetags', 'forms']
