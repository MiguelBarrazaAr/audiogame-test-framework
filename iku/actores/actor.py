#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku
from .actorAbstracto  import ActorAbstracto

class Actor(ActorAbstracto):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self,   visible=True, actualizable=False, colisionable=False, *k, **kv):
    self.iku = iku.instancia()
    self.visible = visible
    self.actualizable = actualizable
    self.colisionable = colisionable
    # cargamos la imagen:
    self.imagen = kv.get('imagen', "")
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
