#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# 2019 - Alan Escola

import openal  

class OpenAlEngine():
  def __init__(self, *args, **kwargs):
    # obtenemos el listener y le damos una orientación hacia adelante
    self.oyente = openal.oalGetListener().set_orientation((0, 0, -1, 0, 1, 0))
  
  def sonido(self, ruta):
    return Sonido3d(ruta)
  
  def finalizar(self):
    openal.oalQuit()


class Sonido3d():
  def __init__(self,ruta):
    fuente = openal.oalOpen(ruta)
    fuente.relative = True
    fuente.set_rolloff_factor(10.0)
    fuente.set_gain(50.0)
    self.fuente = fuente
    #super().__init__()
  
  def reproducir(self, continuo=False):
    self.loop = continuo
    if self.fuente.get_state() == openal.AL_PLAYING:
      self.detener()
    self.fuente.set_looping(continuo)
    self.fuente.play()
    if continuo:
      iku.instancia().escenas.escenaActual.registrarPausable(self)
  
  def detener(self):
    self.fuente.stop()
  
  def pausar(self):
    self.fuente.pause()
  
  def continuar(self):
    self.fuente.play()
  
  @property
  def volumen(self):
    return self.fuente.gain
  
  @volumen.setter
  def volumen(self, valor):
    self.fuente.set_gain(valor)
  
  @property
  def posicion(self):
    return self._posicion
  
  @posicion.setter
  def posicion(self, valor):
    self.fuente.set_position(valor)
    self._posicion = valor