#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import datetime
import os
import random
import sys
import time
import traceback

import pygame
from pygame.locals import *

from .camara import Camara
from .escenas import *
from .eventos import *
from .sonido import iniciar as iniciarAudio
from .tecla import Tecla
from .tts import TTS
from .utiles import *

VERSION = "0.1"

class Iku(object):
  """Representa el area de juego de IkuEngine, el componente principal.
  Internamente, este objeto es el que representa el motor de la aplicación. Es quien mantiene con "vida" el juego completo.
  """
  
  def __init__(self, ancho=640, alto=480, titulo='Iku engine', capturarErrores=True, habilitarMensajesLog=True, plugins=False, modoTest=False):
    # configuración:
    self.capturarErrores = capturarErrores
    self.mensajesLog=habilitarMensajesLog
    self.plugins=plugins
    self.modoTest=modoTest
    self.log("iniciando el motor 'iku'")
    
    # iniciamos el motor pygame:
    pygame.init()
    self.reloj = pygame.time.Clock()
    self.fps =25
    self._winLoop = True
    
    # iniciamos el motor gráfico:
    self.dimension = (ancho, alto)
    self.centro = (ancho/2, alto/2)
    pygame.display.set_caption(titulo)
    self.ventana = pygame.display.set_mode(self.dimension)
    pygame.display.flip()
    
    # cargamos los objetos de iku:
    self.audio = iniciarAudio(self)
    self.camara = Camara()
    self.datos = {}
    self.escenas = escenas.Escenas(self)
    self.eventos = Eventos(self)
    self.tecla = Tecla()
    self.tts = TTS()
    self.log("motor 'iku' iniciado")
  
  def ejecutar(self):
    while self._winLoop:
      # monitorizamos eventos:
      for event in pygame.event.get():
        self._procesarEvento(event)
      
      # controlamos el tiempo de refresco.
      self.reloj.tick(self.fps)
      self.escenas.escenaActual.dibujarEn(self.ventana)
      pygame.display.flip()
  
  def _procesarEvento(self, event):
    # si pulsa en cerrar emitimos pulsaEscape
    if event.type == pygame.QUIT:
      self.eventos.pulsaEscape.emitir(tecla=pygame.K_ESCAPE, tipo=event.type  )
    # si pulsa una tecla:
    if event.type == pygame.KEYDOWN:
      self.eventos.pulsaTecla.emitir(tecla=event.key, representacion=event.unicode)
      # si pulsa escape, emitimos pulsaEscape
      if event.key == pygame.K_ESCAPE:
        self.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type  )
  
  def aleatorio(self, x, y):
    """Hace una tirada de random aleatorio."""
    return random.randint(x, y)
  
  def esperar(self, tiempo):
    """Realiza una espera de cierto tiempo."""
    time.sleep(tiempo)

  def finalizar(self):
    """Finaliza la ejecución  de iku"""
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
  
  def log(self, *mensaje):
    """Si mensajeLog está habilitado, muestra los mensajes por consola."""
    if self.mensajesLog:
      hora = datetime.datetime.now().strftime("%H:%M:%S")
      mensaje = map(lambda x: str(x), mensaje)
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
  
  def sonido3d(self, ruta):
    """ carga un archivo de sonido y devuelve un objeto sound3d"""
    return self.audio.sonido3d(ruta)

def iniciar(titulo='IkuEngine', ancho=640, alto=480, capturarErrores=True, habilitarMensajesLog=True, plugins=False, modoTest=False):
  return Iku(titulo=titulo, ancho=ancho, alto=alto, capturarErrores=capturarErrores, habilitarMensajesLog=habilitarMensajesLog, plugins=plugins, modoTest=modoTest)
