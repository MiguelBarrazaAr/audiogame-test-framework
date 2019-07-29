#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .ElementoUi import ElementoUi

class UiSelector(ElementoUi):
  """representa a una casilla de verificación de la interface invisible. """
  def __init__(self, texto, seleccionado=False, *args, **kwargs):
    if isinstance(seleccionado, bool):
      ElementoUi.__init__(self, texto, *args, **kwargs)
      self._seleccionado = seleccionado
    else:
      ElementoUi.__init__(self, texto, seleccionado, *args, **kwargs)

  def _estado(self):
    if self._seleccionado:
      return "seleccionado"
    else:
      return "no seleccionado"
  
  def __str__(self):
    return "{texto} {estado}".format(texto=self._texto, estado=self._estado())
  
  @property
  def seleccionado(self):
    return self._seleccionado
  
  def alternarSeleccion(self):
    self._seleccionado = not self._seleccionado
  
  def seleccionar(self):
    self._seleccionado = True
  
  def deseleccionar(self):
    self._seleccionado = False
  
  def ejecutar(self):
    self.alternarSeleccion()
    self.iku.leer(self._estado())
    super().ejecutar()

