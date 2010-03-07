from geoportal import utils, admin, templatetags

VERSION = (0, 2, 1)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__all__ = ['utils', 'admin', 'templatetags']
