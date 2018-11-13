#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku
from .sprite import Sprite

class Actor(Sprite):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, *k, **kv):
    # cargamos la imagen:
    self.imagen = kv.get('imagen', "")
    # ajustamos el posicionamiento:
    self.figura.centerx = kv.get('x', 0)
    self.figura.centery = kv.get('y', 0)
    Sprite.__init__(self, **kv)
  
  @property
  def imagen(self):
    return self._surface
  
  @imagen.setter
  def imagen(self, img):
    if type(img) == str:
      self._surface = iku.instancia().imagen(img)
    else:
      self._surface=img
    self.figura = self._surface.get_rect()


  
  def redimensionar(self,ancho,alto):
    self._surface = self.iku.escalarSuperficie(self._surface, ancho=ancho, alto=alto)
    self.figura.size = self._surface.get_rect().size
  
  def dibujarEn(self, superficie):
    if self.visible:
      r = self.figura.move(self.iku.centro)
      superficie.blit(self._surface, r)
  
  def escala(self, x):
    self.figura.w*=x
    self.figura.h*=x
