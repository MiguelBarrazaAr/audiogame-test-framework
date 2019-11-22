#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

import pygame
#from pygame.locals import *
import time


class PygameEngine():
  def __init__(self, iku, titulo, ancho, alto):
    self.iku = iku
    # iniciamos el motor pygame:
    pygame.init()
    self.reloj = pygame.time.Clock()
    self._winLoop = True
    
    # iniciamos el motor gráfico:
    pygame.display.set_caption(titulo)
    self.ventana = pygame.display.set_mode(iku.configuracion.dimension)
    pygame.display.flip()
    # cargamos una fuente default:
    self.fuente = pygame.font.Font("freesansbold.ttf", 30)
  
  def ejecutar(self):
    while self._winLoop:
      self.iku._timestamp = time.time()
      # monitorizamos eventos:
      for event in pygame.event.get():
        self._procesarEvento(event)
      
      # controlamos el tiempo de refresco.
      tick=self.reloj.tick(self.iku.fps)
      self.iku.teclado.actualizar(pygame.key.get_pressed())
      self.iku.tareas.actualizar(tick)
      self.iku.escenas.escenaActual.actualizar(tick)
      self.iku.escenas.escenaActual.dibujarEn(self.ventana)
      pygame.display.flip()
      tick=self.reloj.tick(self.iku.fps)
  
  def _procesarEvento(self, event):
    if event.type == pygame.QUIT:
      self.iku.eventos.usuario.emitir(accion="salir")
      self.iku.finalizar()
    # pulsa una tecla:
    if event.type == pygame.KEYDOWN:
      self.iku.eventos.pulsaTecla.emitir(tecla=self.iku.teclado.tecla(event.key), representacion=event.unicode)
      # si pulsa escape, emitimos pulsaEscape
      if event.key == pygame.K_ESCAPE:
        self.iku.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type)
      if event.key == pygame.K_F4 and self.iku.teclado.altPulsado():
        self.iku.eventos.usuario.emitir(accion="salir")
        self.iku.finalizar()
      if event.key == pygame.K_F9:
        # si esta en modo desarrollador, se activa el depurador.
        self.iku.eventos.usuario.emitir(accion="depurador", escena=self.escena)
    # suelta una tecla:
    if event.type == pygame.KEYUP:
      self.iku.eventos.sueltaTecla.emitir(tecla=self.iku.teclado.tecla(event.key))
    # si algún botón del mouse es presionado
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.iku.eventos.clickMouse.emitir(boton=event.button, posicion=event.pos)
    # si algún botón del mouse es soltado
    if event.type == pygame.MOUSEBUTTONUP:
      self.iku.eventos.finalizaClickMouse.emitir(boton=event.button, posicion=event.pos)
    # si el mouse es movido
    if event.type == pygame.MOUSEMOTION:
      self.iku.eventos.mueveMouse.emitir(botones=event.buttons, posicion=event.pos, movimiento=event.rel)
  
  def definirTitulo(self, titulo):
    pygame.display.set_caption(titulo)
  
  def finalizar(self):
    self._winLoop = False
    pygame.quit()
  
  def escalarSuperficie(self,superficie, ancho, alto):
    return pygame.transform.scale(superficie, (int(ancho), int(alto)))
  
  def cargarImagen(self, rutaImagen):
    """Carga una imagen y retorna una superficie."""
    return pygame.image.load(rutaImagen)
