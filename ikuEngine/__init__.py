#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2018 - 2019: Miguel Barraza

import importlib
import os
import random
import sys
import time
import traceback

from .actores import Actores
from .camara import Camara
from .complementos import Complementos, Complemento
from .configuracion import *
from .decoradores import SingletonDecorator
from .escenas import *
from .eventos import *
from .grafica import iniciar as iniciarGrafica
from .habilidades import Habilidades
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
  
  def __init__(self, titulo='Iku engine', fps=25, capturarErrores=True, habilitarMensajesLog=True, complementos=False, modoTest=False, ancho=640, alto=480, tts=None,
    audio="soundlib", motorGrafico="pygame", *args, **kwargs):
    # configuración:
    self.configuracion = AttrDict()
    self.configuracion['capturarErrores'] = capturarErrores
    self.configuracion['modoTest'] = modoTest
    self.configuracion['mensajesLog'] = habilitarMensajesLog
    self.configuracion['fps'] = fps
    self.fps = fps
    self.configuracion['audio'] = audio
    self.configuracion['grafico'] = motorGrafico
    self._winLoop = False
    self.configuracion['dimension'] = (ancho, alto)
    self.centro = (ancho/2, alto/2)
    self._timestamp = 0
    self.grafica = None
    
    self.eventos = Eventos(self)
    if not modoTest:
      self.grafica = iniciarGrafica(iku=self, motor=motorGrafico, titulo=titulo, ancho=ancho, alto=alto)
      self.mensajesLog=habilitarMensajesLog
      self.log = Log(self)
      self.log("iniciando el motor 'iku'")
      self.tecla = self.grafica.codigoDeTeclas()
    
    # cargamos los objetos de iku:
    self.camara = Camara(self)
    self.escenas = escenas.Escenas(self)
    self.actores = Actores(self)
    self.complementos = Complementos(self, complementos)
    self.datos = AttrDict()
    self.habilidades = Habilidades()
    self.tareas = Tareas(self)
    self.teclado = Teclado(self)
    self.tts = ttsEngine.iniciar(tts)
    self.audio = iniciarAudio(self, audio, *args, **kwargs)
    self._configurarAtajos()
    self.__iniciarPlugins__()
    self.juego = Juego(self)
    self.log("motor 'iku' iniciado")
  
  def _configurarAtajos(self):
    self.sonido = self.audio.sonido
    self.definirTitulo = self.grafica.definirTitulo
    self.cargarImagen = self.grafica.cargarImagen
  
  def     __iniciarPlugins__(self):
    for name, plug in plugins.items():
      plugins[name].iku = self
      plugins[name]._modificarMotor()
      self.log("activo el complemento: '{}'".format(name))
  
  @property
  def escena(self):
    return self.escenas.escenaActual
  
  @property
  def timestamp(self):
    return self._timestamp
  
  def reproducir(self, *args, **kwargs):
    return self.audio.pool.reproducir(*args, **kwargs)
  
  
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
  
  def ejecutar(self):
    self.grafica.ejecutar()
  
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
    self.audio.finalizar()
    self.grafica.finalizar()
    self.log("IkuEngine finalizado.")
    sys.exit(0)
    return True
  
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
    import pygame
    return pygame.Rect(x,y,ancho,alto)
  
  def retardarFuncion(self, funcion, *args, **kwargs):
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
