#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import libaudioverse
from libaudioverse._lav import buffer_get_duration

libaudioverse.initialize()

class LibAudioVerseEngine():
  def __init__(self, md=125, density=0.8, reverbcutoff=22050, reverbtime=1.0, *args, **kwargs):
    self.server=libaudioverse.Server()
    self.server.set_output_device()
    self.world = libaudioverse.EnvironmentNode(self.server,"default")
    self.world.panning_strategy = libaudioverse.PanningStrategies.hrtf
    #self.world.orientation = 0, 1, 0, 0, 0, 1
    #self.world.max_distance=md
    #self.world.distance_model=libaudioverse.DistanceModels.inverse_square
    #self.world.min_reverb_level=1
    #self.world.max_reverb_level=1
    #self.reverb = libaudioverse.FdnReverbNode(self.server)
    #send = self.world.add_effect_send(channels = 4, is_reverb = True, connect_by_default = True)
    #self.world.connect(send, self.reverb, 0)
    #self.reverb.connect(0, self.server)
    #self.reverb.density=density
    #self.reverb.cutoff_frequency=reverbcutoff
    #self.reverb.t60=reverbtime
    #self.reverb.default_reverb_distance=50
    self.world.connect(0, self.world.server)
  
  def set_reverb_distance(self,distance):
    self.reverb.default_reverb_distance=50
  
  def set_reverb_time(self,time):
    self.reverb.t60=time
  
  def set_reverb_cutoff(self,cutoff):
    self.reverb.cutoff_frequency=reverbcutoff
  
  def set_reverb_density(self,density):
    self.reverb.density=density
  
  def shutdown(self):
    libaudioverse.shutdown()
  
  def sonido(self, ruta, posicion, respuesta=None):
    return Sonido3d(self.server, self.world, ruta, posicion, respuesta)
  
  def finalizar(self):
    self.shutdown()


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
        ikuEngine.instancia().escenas.escenaActual.registrarPausable(self)
  
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
