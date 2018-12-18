#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
 #
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import libaudioverse

from .sonido import Sonido
from .sonido3d import Sonido3d
from .pool import SoundPool

libaudioverse.initialize()

class Audio(object):
  def __init__(self, iku, md=125, density=0.8, reverbcutoff=22050, reverbtime=1.0):
    self.iku =iku
    self.pool = SoundPool(iku)
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
  
  def sonido(self, ruta):
    if ruta is None:
      return SonidoNulo()
    else:
      return Sonido(ruta)
  
  def sonido3d(self, ruta, posicion):
    return Sonido3d(self.server, self.world, ruta, posicion)
  
  def finalizar(self):
    self.shutdown()
  
  def reproducirEvento(self, evento):
    # recibe un evento con info del audio y lo reproduce utilizando el pool de iku engine.
    if evento.tipo == "sonido":
      self.pool.reproducir(evento.ruta, evento.posicion)

class SonidoNulo(object):
  def reproducir(self):
    pass


def iniciar(iku):
  return Audio(iku)