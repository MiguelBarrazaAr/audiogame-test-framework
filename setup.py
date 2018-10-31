#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup

setup(
        name='iku',
        zip_safe=False,
        version="0.1",
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
            'iku',
            'iku.actores',
            'iku.complementos',
            'iku.escenas',
            'iku.eventos',
            'iku.sonido',
            'iku.utiles',
        ],
        url='http://www.iku-engine.com.ar',
        include_package_data = True,

        package_data = {
            'images': [ 'iku/imagenes/*' ]
        },

        scripts=[]#['bin/iku'],
)
