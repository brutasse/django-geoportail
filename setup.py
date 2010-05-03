# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-geoportail',
    version='0.3.1',
    author=u'Bruno Renie',
    author_email='bruno@renie.fr',
    packages=['geoportal', 'geoportal.forms', 'geoportal.templatetags'],
    package_data={'geoportal': ['templates/geoportal/*.html',
                                'templates/gis/admin/*']},
    url='http://bitbucket.org/bruno/django-geoportail',
    license='BSD licence, see LICENCE.txt',
    description='Add maps and photos from the French National Geographic' + \
                'Institute to GeoDjango',
    long_description=open('README.txt').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    zip_safe=False
)
