#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class Vector(object):
  """Representa un vector tridimencional"""
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
  
  def toTuple(self):
    """Retorna una tupla con los datos del vector."""
    return (self.x, self.y, self.z)
  
  def toTuple2d(self):
    """Retorna una tupla con los datos del vector en 2d."""
    return (self.x, self.y)

