#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import libaudioverse

from .pool import SoundPool

libaudioverse.initialize()

class Audio(object):
  def __init__(self, iku, tipo, md=125, density=0.8, reverbcutoff=22050, reverbtime=1.0, *args, **kwargs):
    self.iku =iku
    self.log = self.iku.log
    self.pool = SoundPool(iku)
    if tipo == "openal":
      from .openal import OpenAlEngine
      self.motor = OpenAlEngine()
    elif tipo == "soundlib":
      from .soundlib import SoundLibEngine
      self.motor = SoundLibEngine()
    elif tipo == "libaudioverse":
      from .libaudioverse import LibAudioVerseEngine
      self.motor = LibAudioVerseEngine()
    else:
      raise ValueError("'{tipo}' no es un motor de audio valido.".format(tipo=tipo))
  
  def sonido(self, ruta, *args, **kwargs):
    if ruta is None:
      return SonidoNulo()
    else:
      self.log.info("Se carga el audio: '{}'.".format(ruta))
      return self.motor.sonido(ruta, *args, **kwargs)
  
  def finalizar(self):
    self.motor.finalizar()
  
  def reproducirEvento(self, evento):
    # recibe un evento con info del audio y lo reproduce utilizando el pool de iku engine.
    if evento.tipo == "sonido":
      self.pool.reproducir(evento.ruta, evento.posicion)

class SonidoNulo(object):
  def __getattr__(self, nombre, *args, **kwargs):
    pass


def iniciar(iku, tipo, *args, **kwargs):
  return Audio(iku, tipo, *args, **kwargs)