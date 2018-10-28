#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

from .sprite import Sprite

class ActorInvisible(Sprite):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, iku, *k, **kv):
    # generamos la figura:
    self.figura = iku.rectangulo(x=kv.get('x', 0),
      y=kv.get('y', 0),
      alto=kv.get('alto', 1),
      ancho=kv.get('ancho', 1))
    Sprite.__init__(self, iku, visible=False, **kv)
  
  def redimensionar(self,ancho,alto):
    self.figura.size = (ancho, alto)
  
  def escala(self,escala):
    self.figura.size = ( (self.figura.w*escala), (self.figura.h*escala) )
