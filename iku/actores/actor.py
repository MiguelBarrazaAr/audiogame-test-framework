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
    Sprite.__init__(self, **kv)
    # ajustamos el posicionamiento:
    self.posicionar(x=kv.get('x', 0),
      y=kv.get('y', 0),
      absoluto=kv.get('absoluto', False))
    self._escala = 1 
  
  @property
  def imagen(self):
    return self._surface
  
  @imagen.setter
  def imagen(self, img):
    try:
      posicion=self.figura.center
    except:
      posicion=(0,0)
    
    if type(img) == str:
      self._surface = iku.instancia().imagen(img)
    else:
      self._surface=img
    self.figura = self._surface.get_rect()
    self.figura.center = posicion
  
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
  
  def dibujarEn(self, superficie):
    if self.visible:
      superficie.blit(self._surface, self.figura)
  
  @property
  def escala(self):
    return self._escala
  
  @escala.setter
  def escala(self, x):
    ancho=self.figura.w*x
    alto=self.figura.h*x
    self.figura.w*=x
    self.figura.h*=x
    self._escala*=x
    self.redimensionar(ancho, alto)
