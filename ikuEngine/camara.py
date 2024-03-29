#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class Camara(object):
  """representa a la camara, a lo que se puede visualizar en pantalla"""
  def __init__(self, iku):
    self.iku = iku
    self.evento = iku.eventos.crear('eventoCamara')
    self._x = 0
    self._y = 0
    self._z = 0
  
  def reiniciar(self):
    self.posicion = (0, 0, 0)
  
  @property
  def posicion(self):
    return (self._x, self._y, self._z)
  
  @posicion.setter
  def posicion(self, tupla):
    """actualiza la posicion con la tupla pasada"""
    self._x, self._y, self._z = tupla
    self.evento.emitir(posicion=tupla, x=self._x, y=self._y, z=self._z)
