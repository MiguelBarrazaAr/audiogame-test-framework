#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - 2019: Miguel Barraza
import iku
import libaudioverse
from libaudioverse._lav import buffer_get_duration

class Sonido3d(object):
  def __init__(self, server, world, fileRoute, position, callback=None):
    self.server=server
    self.world = world
    self.source = libaudioverse.SourceNode(server, world)
    self.buffer = libaudioverse.BufferNode(server)
    b = libaudioverse.Buffer(server)
    b.load_from_file(fileRoute)
    self.ruta = fileRoute
    self.buffer.buffer = b
    self.buffer.state = libaudioverse.NodeStates.paused
    self.source.position = position
    self.respuesta = callback
    self.buffer.set_end_callback(self._lanzarRespuesta)
    self.duracion = buffer_get_duration(b)
  
  def __str__(self):
    return f"Sonido3d: {self.ruta}"
  
  def transcurrido(self):
    return       self.buffer.position
  
  def l(self):
    self.buffer.disconnect()
    del self
  
  def reproducir(self, continuo=False):
    if not self.estaReproduciendo():
      self.buffer.connect(0, self.source, 0)
      self.buffer.position=0
      self.buffer.looping = continuo
      self.buffer.state = libaudioverse.NodeStates.playing
      if continuo:
        iku.instancia().escenas.escenaActual.registrarPausable(self)
  
  def _lanzarRespuesta(self, buffer):
    if self.respuesta is not None:
      self.respuesta()
  
  def estaReproduciendo(self):
    return self.buffer.state.value is libaudioverse.NodeStates.playing
  
  def finalizar(self):
    """Finaliza la reproducción, lanza el callback y se elimina."""
    if self.estaReproduciendo():
      self.buffer.state = libaudioverse.NodeStates.paused
    self._lanzarRespuesta(self.buffer)
    del self
  
  def detener(self):
    if self.estaReproduciendo():
      self.buffer.state = libaudioverse.NodeStates.paused
  
  @property
  def posicion(self):
    return self.source.position.value
  
  @posicion.setter
  def posicion(self, pos):
    self.source.position = pos
  
  @property
  def pitch(self):
    return self.buffer.rate
  
  @pitch.setter
  def pitch(self, x):
    self.buffer.rate = x/100
  
  @property
  def paneo(self):
    pass #return self.handle.pan
  
  @paneo.setter
  def paneo(self, valor):
    pass #self.handle.pan = valor
  
  @property
  def volumen(self):
    return self.source.mul * 100
  
  @volumen.setter
  def volumen(self, x):
    self.source.mul = x/100
