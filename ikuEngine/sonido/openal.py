#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# 2019 - Alan Escola y Miguel Barraza

import openal  

class OpenAlEngine():
  def __init__(self, *args, **kwargs):
    # obtenemos el listener y le damos una orientación hacia adelante
    self.escucha = Escucha(openal.oalGetListener())
  
  def posicionarEscucha(self, posicion):
    self.escucha.posicion = posicion
  
  def sonido(self, ruta, *args, **kwargs):
    return Sonido(ruta, *args, **kwargs)
  
  def finalizar(self):
    openal.oalQuit()


class Escucha():
  """ adapter del listener. """
  def __init__(self, listener):
    self.escucha = listener
  
  @property
  def posicion(self):
    self.escucha.position
  
  @posicion.setter
  def posicion(self, tupla3d):
    self.escucha.set_position(tupla3d)
  
  def posicionar(self, x=None, y=None, z=None):
    x1, y1, z1 = self.escucha.position
    x = x1 if x is None else x
    y = y1 if y is None else y
    z = z1 if z is None else z
    self.escucha.set_position((x, y, z))

class Sonido():
  def __init__(self,ruta, volumen=50.0, relativo=True, factor=1.0):
    fuente = openal.oalOpen(ruta)
    fuente.relative = relativo
    fuente.set_rolloff_factor(factor)
    fuente.set_gain(volumen)
    self.fuente = fuente
    #super().__init__()
  
  def reproducir(self, continuo=False):
    self.loop = continuo
    if self.fuente.get_state() == openal.AL_PLAYING:
      self.detener()
    self.fuente.set_looping(continuo)
    self.fuente.play()
    if continuo:
      pass#iku.instancia().escenas.escenaActual.registrarPausable(self)
  
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
    return self.fuente.position
  
  @posicion.setter
  def posicion(self, valor):
    self.fuente.set_position(valor)
    #self._posicion = valor
  
  @property
  def continuo(self):
    return self.fuente.looping
  
  @continuo.setter
  def continuo(self, bool):
    self.fuente.set_looping(bool)
