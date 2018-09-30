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
    if escena._imagenFondo is not None:
      self.ventana.blit(escena._imagenFondo, (0,0))
    # dibujamos actores:
    for actor in escena.actores:
      if (actor.imagen is not None) and actor.visible:
        r = actor.rect.move(self.iku.x, self.iku.y)
        #print(self.iku.x, self.iku.y)
        #print("dibujando", r.centerx, r.centery)
        self.ventana.blit(actor.imagen, r)
    pygame.display.flip()
  
  def escalar(self,imagen, dimenciones):
    return pygame.transform.scale(imagen, dimenciones)

def iniciar(iku, titulo, dimension):
  return PygameVideo(iku, titulo, dimension)