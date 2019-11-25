#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import ikuEngine
from .elemento import Elemento

class Actor(Elemento):
  """
  Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, *args, **kwargs):
    Elemento.__init__(self, *args, **kwargs)
    self._posicion = self.iku.vector(x=kwargs.get("x", 0),
      y=kwargs.get("y", 0),
      z=kwargs.get("z", 0))
  
  @property
  def x(self):
    return self._posicion.x
  
  @property
  def y(self):
    return self._posicion.y
  
  @property
  def z(self):
    return self._posicion.z
  
  @property
  def posicion2d(self):
    return self._posicion.xy
  
  @property
  def posicion(self):
    return self._posicion.xyz
  
  @posicion.setter
  def posicion(self, tupla):
    self._posicion.posicionar(*tupla)
    self.alCambiarPosicion()
  
  def mover(self, x=0, y=0, z=0):
    self._posicion.mover(x, y, z)
    self.alCambiarPosicion()
  
  def coordenadaAlMover(self, x=0, y=0, z=0):
    """Retorna a que coordenada estaría el actor si se le sumaría tantos pasos en x, y, z."""
    return (self.x+x, self.y+y, self.z+z)
  
  def alCambiarPosicion(self):
    """ metodo que se ejecuta cuando la posicion se cambia. """
    pass
