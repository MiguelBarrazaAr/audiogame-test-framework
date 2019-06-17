#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku
from .elemento import Elemento

class ActorAbstracto(Elemento):
  """
  nivel superior de actor y actorInvisible.
  """
  def __init__(self, *l, **kv):
    Elemento.__init__(self)
  
  @property
  def x(self):
    return self.figura.centerx
  
  @property
  def y(self):
    return self.figura.centery
  
  @property
  def posicion(self):
    return self.figura.center
  
  @property
  def posicion3d(self):
    return (self.figura.centerx, self.figura.centery, 0)
  
  @posicion.setter
  def posicion(self, tupla):
    self.figura.center = tupla   
  
  @property
  def ancho(self):
    return self.figura.w
  
  @property
  def alto(self):
    return self.figura.h
  
  def mover(self, x=0, y=0):
    self.figura.move_ip(x,y)
  
  def coordenadaAlMover(self, x=0, y=0):
    return (self.x+x, self.y+y)
  
  def posicionar(self, x, y, absoluto=False):
    if absoluto:
     self.posicion = (x,y)
    else:
      #  en posicionamiento relativo toma como centro (0,0) el centro de la pantalla.
      cx, cy = self.iku.centro
      self.posicion = (cx+x, cy-y)
  
  def redimensionar(self,ancho,alto):
    self._surface = self.iku.escalarSuperficie(self._surface, ancho=ancho, alto=alto)
    self.figura.size = self._surface.get_rect().size
