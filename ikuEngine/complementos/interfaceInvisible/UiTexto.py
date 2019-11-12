#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .ElementoUi import ElementoUi

class UiTexto(ElementoUi):
  """representa a un texto o etiqueta de la interface invisible. """
  def __init__(self, *args, **kwargs):
    ElementoUi.__init__(self, *args, **kwargs)
    print(self.visibleConTab)
    self.visibleConTab = False
    print(self.visibleConTab)
  
  def __str__(self):
    return self._texto
