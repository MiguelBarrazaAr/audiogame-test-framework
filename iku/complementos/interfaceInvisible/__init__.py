#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .UiBoton import UiBoton
from .UiIngresaTexto import UiIngresaTexto
from .UiLista import UiLista
from .UiSelector import UiSelector
from .UiTexto import UiTexto
from .Contenedor import Contenedor
from .menu import Menu
from .ejecutarConFlechas import EjecutarConFlechas

class Complemento(object):
  def __init__(self, iku):
    iku.actores.vincular(EjecutarConFlechas)
    iku.actores.vincular(Menu)
    iku.actores.vincular(Contenedor)
    iku.actores.vincular(UiBoton)
    iku.actores.vincular(UiIngresaTexto)
    iku.actores.vincular(UiLista)
    iku.actores.vincular(UiSelector)
    iku.actores.vincular(UiTexto)
