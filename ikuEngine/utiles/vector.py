#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class Vector(object):
  """Representa un vector tridimencional"""
  def __init__(self, x=0, y=0, z=0):
    self._x = x
    self._y = y
    self._z = z
  
  @property
  def x(self):
    return self._x
  
  @property
  def y(self):
    return self._y
  
  @property
  def z(self):
    return self._z
  
  def toTuple(self):
    """Retorna una tupla con los datos del vector."""
    return (self._x, self._y, self._z)
  
  def toTuple2d(self):
    """Retorna una tupla con los datos del vector en 2d."""
    return (self._x, self._y)
  
  def mover(self, x=0, y=0, z=0):
    self._x = self._x+x
    self._y = self._y+y
    self._z = self._z+z
    return self

