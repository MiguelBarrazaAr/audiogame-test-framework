#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import pygame
from pygame.locals import *

class PygameVideo(object):
  """Representa la propiedad iku.grafica
  
  Se Encarga de dibujar en pantalla los gráficos y de controlar todos los parámetros de video. como eventos de interacción hardware con el usuario. LA UI.
  """
  
  def __init__(self, iku, titulo, dimension):
    self.iku = iku
    self.x = iku.x
    self.y = iku.y
    
    pygame.display.set_caption(titulo)
    self.ventana = pygame.display.set_mode(dimension)
    pygame.display.flip()
  
  def dibujar(self, escena):
    self.ventana.fill(escena.colorFondo)
    if escena.fondo is not None:
      self.ventana.blit(escena.fondo, (0,0))
    # dibujamos actores:
    for actor in escena.actores:
      if (actor.imagen is not None) and actor.visible:
        self.ventana.blit(actor.imagen, self.centrar(actor.posicion))
    pygame.display.flip()
  
  def centrar(self, posicion):
    return (self.x + posicion.x, self.y + posicion.y)

def iniciar(iku, titulo, dimension):
  return PygameVideo(iku, titulo, dimension)