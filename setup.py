#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup

setup(
        name='ikuEngine',
        zip_safe=False,
        version="0.3",
        description="""Iku Engine - un motor para realizar videojuegos y audiojuegos de manera rápida y sencilla.

Es una herramienta orientada a desarrollar juegos accesibles para personas con discapacidad visual.
""",
        author='Miguel Barraza',
        author_email='miguelbarraza2015@gmail.com',
        install_requires=[
            'setuptools',
            'pygame',
            'libaudioverse',
            'accessible-output2',
            ],
        packages=[
            'ikuEngine',
            'ikuEngine.actores',
            'ikuEngine.complementos',
            'ikuEngine.escenas',
            'ikuEngine.sonido',
            'ikuEngine.utiles',
        ],
        url='http://www.iku-engine.com.ar',
        include_package_data = True,

        package_data = {
            'images': [ 'ikuEngine/imagenes/*' ]
        },

        scripts=[]#['bin/iku'],
)
