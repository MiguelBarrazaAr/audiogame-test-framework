#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - 2019: Miguel Barraza

import asyncio
import datetime
import os
import random
import sys
import time
import traceback

import pygame
from pygame.locals import *

from .actores import Actores
from .camara import Camara
from .complementos import Complementos
from .decoradores import SingletonDecorator
from .escenas import *
from .eventos import *
from .sonido import iniciar as iniciarAudio
from .tareas import Tareas
from .tecla import Tecla
from .tts import TTS
from .utiles import *



VERSION = "0.2.1"
ikuEngine = None

@SingletonDecorator
class Iku(object):
  """Representa el area de juego de IkuEngine, el componente principal.
  Internamente, este objeto es el que representa el motor de la aplicación. Es quien mantiene con "vida" el juego completo.
  """
  
  def __init__(self, ancho=640, alto=480, titulo='Iku engine', fps=25, capturarErrores=True, habilitarMensajesLog=True, complementos=False, modoTest=False, *k, **kv):
    # configuración:
    self.capturarErrores = capturarErrores
    self.modoTest=modoTest
    self.mensajesLog=False
    self.fps =fps
    self._winLoop = False
    self.dimension = (ancho, alto)
    self.centro = (ancho/2, alto/2)
    
    if not self.modoTest:
      self.mensajesLog=habilitarMensajesLog
      self.log("iniciando el motor 'iku'")
      self._iniciarGrafica(titulo, ancho, alto)
    
    self.loop = asyncio.new_event_loop()
    # cargamos los objetos de iku:
    self.eventos = Eventos(self)
    self.camara = Camara(self)
    self.escenas = escenas.Escenas(self)
    self.actores = Actores(self)
    self.complementos = Complementos(self, complementos)
    self.datos = AttrDict()
    self.tareas = Tareas()
    self.tecla = Tecla()
    self.tts = TTS()
    self.audio = iniciarAudio(self)
    self.log("motor 'iku' iniciado")
  
  @property
  def escena(self):
    return self.escenas.escenaActual
  
  def reproducir(self, *args, **kwargs):
    return self.audio.pool.reproducir(*args, **kwargs)
  
  def _iniciarGrafica(self, titulo, ancho, alto):
    # iniciamos el motor pygame:
    pygame.init()
    self.reloj = pygame.time.Clock()
    self._winLoop = True
    
    # iniciamos el motor gráfico:
    pygame.display.set_caption(titulo)
    self.ventana = pygame.display.set_mode(self.dimension)
    pygame.display.flip()
    # cargamos una fuente default:
    self.fuente = pygame.font.Font("freesansbold.ttf", 30)
  
  def ejecutar(self):
    #self.loop.run_forever()
    while self._winLoop:
      # monitorizamos eventos:
      for event in pygame.event.get():
        self._procesarEvento(event)
      
      # controlamos el tiempo de refresco.
      tick=self.reloj.tick(self.fps)
      self.tareas.actualizar(tick)
      self.escenas.escenaActual.actualizar(tick)
      self.escenas.escenaActual.dibujarEn(self.ventana)
      pygame.display.flip()
      tick=self.reloj.tick(self.fps)
  
  def _procesarEvento(self, event):
    # si pulsa en cerrar emitimos pulsaEscape
    if event.type == pygame.QUIT:
      self.eventos.pulsaEscape.emitir(tecla=pygame.K_ESCAPE, tipo=event.type  )
    # pulsa una tecla:
    if event.type == pygame.KEYDOWN:
      self.eventos.pulsaTecla.emitir(tecla=event.key, representacion=event.unicode)
      # si pulsa escape, emitimos pulsaEscape
      if event.key == pygame.K_ESCAPE:
        self.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type  )
      if event.key == pygame.K_F4 and self.tecla.altPulsado():
        self.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type  )
      if event.key == pygame.K_F9:
        # si esta en modo desarrollador, se activa el depurador.
        self.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type  )
    # suelta una tecla:
    if event.type == pygame.KEYUP:
      self.eventos.sueltaTecla.emitir(tecla=event.key)
    # si algún botón del mouse es presionado
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.eventos.clickMouse.emitir(boton=event.button, posicion=event.pos)
    # si algún botón del mouse es soltado
    if event.type == pygame.MOUSEBUTTONUP:
      self.eventos.finalizaClickMouse.emitir(boton=event.button, posicion=event.pos)
    # si el mouse es movido
    if event.type == pygame.MOUSEMOTION:
      self.eventos.mueveMouse.emitir(botones=event.buttons, posicion=event.pos, movimiento=event.rel)
  
  def aleatorio(self, x, y):
    """Hace una tirada de random aleatorio."""
    return random.randint(x, y)
  
  def elegir(self, lista):
    """Elige un elemento aleatorio en una lista."""
    return random.choice(lista)
  
  def mezclar(self, lista):
    """Mezcla los elementos de una lista."""
    return random.shuffle(lista)
  
  def esperar(self, tiempo):
    """Realiza una espera de cierto tiempo."""
    time.sleep(tiempo)

  def finalizar(self):
    """Finaliza la ejecución  de iku"""
    self.loop.close()
    pygame.quit()
    self.audio.finalizar()
    self.eventos.finalizaMotor.emitir(modo="okey", mensaje="")
    self.log("IkuEngine finalizado.")
    self._winLoop = False
    sys.exit(0)
  
  def escalarSuperficie(self,superficie, ancho, alto):
    return pygame.transform.scale(superficie, (int(ancho), int(alto)))
  
  def imagen(self, rutaImagen):
    """Carga una imagen y retorna una superficie."""
    return pygame.image.load(rutaImagen)
  
  def leer(self, texto, interrumpir=True, registrar=True):
    """Envia un texto al tts para ser verbalizado"""
    self.tts.hablar(texto, interrumpir, registrar)
  
  def listarDirectorio(self, ruta):
    return os.listdir(ruta)
  
  def log(self, *mensaje):
    """Si mensajeLog está habilitado, muestra los mensajes por consola."""
    if self.mensajesLog:
      hora = datetime.datetime.now().strftime("%H:%M:%S")
      mensaje = map(lambda x: repr(x), mensaje)
      texto = " ".join(mensaje)
      print(":: %s :: %s " % (hora, texto))
  
  def posicion(self, x=0, y=0, z=0):
    return Posicion(x=x, y=y, z=z)
  
  def rectangulo(self, x=0, y=0, ancho=1, alto=1):
    return pygame.Rect(x,y,ancho,alto)
    
  def sonido(self, ruta=None):
    """ carga un archivo de sonido y devuelve un objeto sound
    
    :param ruta: se refiere a la ruta donde se encuentra el archivo *.ogg o *.wav
    :type ruta: string
    Si se pasa None o no se pasa ninguna devuelve un sonido nulo. que no ahce nada.
    """
    return self.audio.sonido(ruta)
  
  def sonido3d(self, ruta, posicion):
    """ carga un archivo de sonido y devuelve un objeto sound3d"""
    return self.audio.sonido3d(ruta, posicion)


def instancia():
  # retorna la instancia activa de iku engine, si hay alguna:
  return ikuEngine  

def iniciar(*k, **kv):
  global ikuEngine
  if ikuEngine  is None:
    ikuEngine  = Iku(*k, **kv)
  return ikuEngine
  #else:
  #raise Exception("Ya hay una instancia de ikuEngine Inicializada.")
