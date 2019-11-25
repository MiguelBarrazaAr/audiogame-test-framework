#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza
from pygame.math import Vector3

class Vector():
  """Representa un vector tridimencional"""
  def __init__(self, x=0, y=0, z=0):
    self.vec = Vector3(x,y,z)
  
  @property
  def x(self):
    return self.vec.x
  
  @x.setter
  def x(self, value):
    self.vec.x=x
  
  @property
  def y(self):
    return self.vec.y
  
  @y.setter
  def y(self, value):
    self.vec.y=y
  
  @property
  def z(self):
    return self.vec.z
  
  @z.setter
  def z(self, value):
    self.vec.z=z
  
  @property
  def xyz(self):
    """Retorna una tupla con los datos del vector."""
    return (self.vec.x, self.vec.y, self.vec.z)
  
  @property
  def xyzint(self):
    """Retorna una tupla (int, int, int) con los datos del vector."""
    return (int(self.vec.x), int(self.vec.y), int(self.vec.z))
  
  @property
  def xy(self):
    """Retorna una tupla con los datos del vector en 2d."""
    return (self.vec.x, self.vec.y)
  
  @property
  def xyint(self):
    """Retorna una tupla (int, int) con los datos del vector en 2d."""
    return (int(self.vec.x), int(self.vec.y))
  
  def mover(self, x=0, y=0, z=0):
    self.vec.update(self.vec.x+x, self.vec.y+y, self.vec.z+z)
    return self
  
  def posicionar(self, x=0, y=0, z=0):
    self.vec.update(x,y,z)
    return self
