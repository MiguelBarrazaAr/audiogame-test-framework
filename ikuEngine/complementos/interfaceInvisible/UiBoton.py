#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .ElementoUi import ElementoUi

class UiBoton(ElementoUi):
  """representa a un botón de la interface invisible. """
  @property
  def tipo(self):
    return "botón"
