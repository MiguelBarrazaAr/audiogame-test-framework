#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine
from .UiBoton import UiBoton
from .UiIngresaTexto import UiIngresaTexto
from .UiLista import UiLista
from .UiSelector import UiSelector
from .UiTexto import UiTexto
from .Contenedor import Contenedor
from .menu import Menu
from .ejecutarConFlechas import EjecutarConFlechas

@ikuEngine.vincularComplemento
class interfaceInvisible(ikuEngine.Complemento):
  def __init__(self):
    self.iku = None
  
  def _modificarMotor(self):
    self.iku.actores.vincular(EjecutarConFlechas)
    self.iku.actores.vincular(Menu)
    self.iku.actores.vincular(Contenedor)
    self.iku.actores.vincular(UiBoton)
    self.iku.actores.vincular(UiIngresaTexto)
    self.iku.actores.vincular(UiLista)
    self.iku.actores.vincular(UiSelector)
    self.iku.actores.vincular(UiTexto)
