#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.6)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import libaudioverse
from libaudioverse._lav import buffer_get_duration

class Sonido3d(object):
  def __init__(self, server, world, fileRoute, position):
    self.server=server
    self.world = world
    self.source = libaudioverse.SourceNode(server, world)
    self.buffer = libaudioverse.BufferNode(server)
    b = libaudioverse.Buffer(server)
    b.load_from_file(fileRoute)
    self.buffer.buffer = b
    self.buffer.state = libaudioverse.NodeStates.paused
    self.posicion = position
    self.buffer.set_end_callback(self.fin)
    self.duracion = buffer_get_duration(b)
  
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
  
  def fin(self):
    print("fin del audio")
  
  def reproducirContinuo(self):
    self.reproducir(True)
  
  def estaReproduciendo(self):
    return self.buffer.state.value is libaudioverse.NodeStates.playing
  
  def detener(self):
    if self.estaReproduciendo():
      self.buffer.state = libaudioverse.NodeStates.paused
  
  @property
  def posicion(self):
    x,y,z=self.source.position
    return self.iku.posicion(x=x, y=y, z=z)
  
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
