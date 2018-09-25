#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from .vector import Vector

class Posicion(Vector):
  def __eq__(self, posicion):
    return self.x==posicion.x and self.y==posicion.y and self.z==posicion.z
  
  def __str__(self):
    return "posicion: "+str((self.x, self.y, self.z))
  def actualizar(self, x=None, y=None, z=None):
    if x is not None:
      self.x = x
    if y is not None:
      self.y = y
    if z is not None:
      self.z = z
    return self
  
  def copia(self):
    return Posicion(x=self.x, y=self.y, z=self.z)
  
  def mover(self, x=0, y=0, z=0):
    self.x = self.x+x
    self.y = self.y+y
    self.z = self.z+z
    return self
