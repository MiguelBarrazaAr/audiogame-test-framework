#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku
from .actorAbstracto import ActorAbstracto

class ActorInvisible(ActorAbstracto):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, *k, **kv):
    # generamos la figura:
    ActorAbstracto.__init__(self, **kv)
    self.figura = iku.instancia().rectangulo(x=kv.get('x', 0),
      y=kv.get('y', 0),
      alto=kv.get('alto', 1),
      ancho=kv.get('ancho', 1))
  
  def redimensionar(self,ancho,alto):
    self.figura.size = (ancho, alto)
  
  def escala(self,escala):
    self.figura.size = ( (self.figura.w*escala), (self.figura.h*escala) )
  
  def dibujarEn(self, superficie):
    pass