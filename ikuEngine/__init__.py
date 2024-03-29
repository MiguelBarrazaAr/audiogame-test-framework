﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2018 - 2019: Miguel Barraza

import asyncio
import importlib
import os
import random
import sys
import time
import traceback

import pygame
from pygame.locals import *

from .actores import Actores
from .camara import Camara
from .complementos import Complementos, Complemento
from .configuracion import *
from .decoradores import SingletonDecorator
from .escenas import *
from .eventos import *
from .juego import Juego
from .Log import Log
from .sonido import iniciar as iniciarAudio
from .tareas import Tareas
from .teclado import Teclado
from . import tts as ttsEngine
from .utiles import *

ikuEngine = None
plugins = {} # lista de complementos.

def printTraceback(exc_type, exc_value, tb):
  for i, (frame, _) in enumerate(traceback.walk_tb(tb)):
    if os.path.basename(os.path.dirname(frame.f_code.co_filename)) == 'iku':
      limit = i
      break
  else:
    limit = None
  traceback.print_exception(exc_type, exc_value, tb, limit=limit, chain=False)

excepthook = sys.excepthook
sys.excepthook = printTraceback

@SingletonDecorator
class Iku(object):
  """Representa el area de juego de IkuEngine, el componente principal.
  Internamente, este objeto es el que representa el motor de la aplicación. Es quien mantiene con "vida" el juego completo.
  """
  
  def __init__(self, ancho=640, alto=480, titulo='Iku engine', fps=25, capturarErrores=True, habilitarMensajesLog=True, complementos=False, modoTest=False, tts=None, audio="openal", *args, **kwargs):
    # configuración:
    self.capturarErrores = capturarErrores
    self.modoTest=modoTest
    self.mensajesLog=False
    self.fps =fps
    self._winLoop = False
    self.dimension = (ancho, alto)
    self.centro = (ancho/2, alto/2)
    self._timestamp = 0
    
    self.eventos = Eventos(self)
    self.log = Log(self)
    if not self.modoTest:
      self.mensajesLog=habilitarMensajesLog
      self.log("iniciando el motor 'iku'")
      self._iniciarGrafica(titulo, ancho, alto)
    
    self.loop = asyncio.new_event_loop()
    # cargamos los objetos de iku:
    self.camara = Camara(self)
    self.escenas = escenas.Escenas(self)
    self.actores = Actores(self)
    self.complementos = Complementos(self, complementos)
    self.datos = AttrDict()
    self.tareas = Tareas(self)
    self.teclado = Teclado()
    self.tts = ttsEngine.iniciar(tts)
    self.audio = iniciarAudio(self, audio, *args, **kwargs)
    self.__iniciarPlugins__()
    self.juego = Juego(self)
    self.log("motor 'iku' iniciado")
  
  def     __iniciarPlugins__(self):
    for name, plug in plugins.items():
      plugins[name].iku = self
      plugins[name]._modificarMotor()
      self.log("activo el complemento: '{}'".format(name))
  
  @property
  def escena(self):
    return self.escenas.escenaActual
  
  def reproducir(self, *args, **kwargs):
    return self.audio.pool.reproducir(*args, **kwargs)
  
  def posicionarEscucha(self, posicion):
    self.audio.motor.posicionarEscucha(posicion)  
  
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
      self._timestamp = time.time()
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
    if event.type == pygame.QUIT:
      self.eventos.usuario.emitir(accion="salir")
      self.finalizar()
    # pulsa una tecla:
    if event.type == pygame.KEYDOWN:
      self.eventos.pulsaTecla.emitir(tecla=self.teclado.tecla(event.key), representacion=event.unicode)
      # si pulsa escape, emitimos pulsaEscape
      if event.key == pygame.K_ESCAPE:
        self.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type)
      if event.key == pygame.K_F4 and self.teclado.altPulsado():
        self.eventos.usuario.emitir(accion="salir")
        self.finalizar()
      if event.key == pygame.K_F9:
        # si esta en modo desarrollador, se activa el depurador.
        self.eventos.usuario.emitir(accion="depurador", escena=self.escena)
    # suelta una tecla:
    if event.type == pygame.KEYUP:
      self.eventos.sueltaTecla.emitir(tecla=self.teclado.tecla(event.key))
    # si algún botón del mouse es presionado
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.eventos.clickMouse.emitir(boton=event.button, posicion=event.pos)
    # si algún botón del mouse es soltado
    if event.type == pygame.MOUSEBUTTONUP:
      self.eventos.finalizaClickMouse.emitir(boton=event.button, posicion=event.pos)
    # si el mouse es movido
    if event.type == pygame.MOUSEMOTION:
      self.eventos.mueveMouse.emitir(botones=event.buttons, posicion=event.pos, movimiento=event.rel)
  
  def definirTitulo(self, titulo):
    pygame.display.set_caption(titulo)
  
  def definirSemilla(self, semilla):
    """ determina una semilla para una tirada de random aleatoria. """
    random.seed(semilla)
  
  def aleatorio(self, x, y, cantidad=1):
    """Hace una tirada de random aleatorio."""
    if cantidad == 1:
      return random.randint(x, y)
    else:
      nums = []
      for n in range(0, cantidad):
        nums.append(random.randint(x, y))
      return nums
  
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
    if not isinstance(texto, str):
      texto = str(texto)
    self.tts.hablar(texto, interrumpir, registrar)
  
  def listarDirectorio(self, ruta):
    return os.listdir(ruta)
  
  def listarArchivos(self, ruta, extension, nombreCompleto=True):
    extension="."+extension
    list = []
    for f in os.listdir(ruta):
      nom, ext  = os.path.splitext(f)
      if ext == extension:
        if nombreCompleto:
          list.append(f)
        else:
          list.append(nom)
    return list
  
  def vector(self, x=0, y=0, z=0):
    return Vector(x=x, y=y, z=z)
  
  def rectangulo(self, x=0, y=0, ancho=1, alto=1):
    return pygame.Rect(x,y,ancho,alto)
    
  def sonido(self, ruta=None):
    """ carga un archivo de sonido y devuelve un objeto sound
    
    :param ruta: se refiere a la ruta donde se encuentra el archivo *.ogg o *.wav
    :type ruta: string
    Si se pasa None o no se pasa ninguna devuelve un sonido nulo. que no ahce nada.
    """
    return self.audio.sonido(ruta)
  
  def sonido3d(self, ruta, posicion, respuesta=None):
    """ carga un archivo de sonido y devuelve un objeto sound3d"""
    return self.audio.sonido3d(ruta, posicion, respuesta)
  
  def llamadaAFuncion(self, funcion, *args, **kwargs):
    """ Crea una funcion que se puede llamar despues y llamará a la función pasada por parametro. """  
    def f():
      funcion(*args, **kwargs)
    return f
  
  def __getattr__(self, nombre):
    """ cuando se llama a un metodo que no existe en iku lo busca entre sus plugins. """
    if nombre in plugins:
      return plugins[nombre]
    else:
      raise AttributeError("'Iku' object has no attribute '{nombre}'".format(nombre=nombre))

def vincularComplemento(comp):
  """ Agrega un complemento a iku. """
  #if isinstance(comp, ModuloIku):
  nombre = comp.__name__
  if nombre in plugins:
    raise Exception("Error, ya existe un complemento vinculado con el nombre: " + nombre)
  else:
    plugins[nombre]=comp()
  #else:
  #raise Exception("se intento vincular {obj} como un complemento de iku.".format(obj=comp))

def importarComplemento(nombre):
  mod = importlib.import_module("ikuEngine.complementos."+nombre)

def instancia():
  # retorna la instancia activa de iku engine, si hay alguna:
  return ikuEngine  

def debugIku(active=True):
  if active:
    sys.excepthook = excepthook
  else:
    sys.excepthook = printTraceback

def iniciar(*k, **kv):
  global ikuEngine
  if ikuEngine  is None:
    ikuEngine  = Iku(*k, **kv)
  return ikuEngine
  #else:
  #raise Exception("Ya hay una instancia de ikuEngine Inicializada.")
