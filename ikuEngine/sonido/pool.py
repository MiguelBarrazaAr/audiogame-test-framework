#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class SoundPool(object):
  """Pool que gestiona todo los sonidos del juego"""
  def __init__(self, iku, cantidadDeSonidos=200):
    self.iku = iku
    self.camx, self.camy, self.camz = (0,0,0) # posicion donde se centra el audio.
    iku.eventos.mueveCamara.conectar(self._alMoverCamara)
    self.ajustarPosicion()
    self.cantidadDeSonidos = cantidadDeSonidos
    self.x = 0
    self.lista = [None]*cantidadDeSonidos
  
  def reproducir(self, ruta, posicion=(0,0), respuesta=None, espera=0, continuo=False, *args, **kwargs):
    """carga y reproduce un sonido"""
    if len(posicion) == 2:
      return self._reproducir2d(ruta, posicion, respuesta, espera, continuo, *args, **kwargs)
    else:
      return self._reproducir3d(ruta, posicion, respuesta, espera, continuo, *args, **kwargs)
  
  def _reproducir2d(self, ruta, posicion=(0,0), respuesta=None, espera=0, continuo=False, *args, **kwargs):
    sonido = self.iku.sonido(ruta)
    sonido.reproducir(continuo)
    self.lista[self.x] = sonido
    self.x = (self.x+1)%self.cantidadDeSonidos
    return sonido
  
  def _reproducir3d(self, ruta, posicion=(0,0), respuesta=None, espera=0, continuo=False, *args, **kwargs):
    px, py, pz = posicion
    pos = (px-self.camx, py-self.camy, pz-self.camz)
    sonido = self.iku.sonido3d(ruta, pos)
    # si tiene callback agregamos una tarea:
    def alFinalizar():
      if respuesta is not None:
        self.iku.tareas.unaVez(espera, respuesta, *args, **kwargs)
      s=self.lista[self.x]
      self.lista[self.x] = None
      del s
    sonido.respuesta = alFinalizar
    sonido.reproducir(continuo)
    self.lista[self.x] = sonido
    self.x = (self.x+1)%self.cantidadDeSonidos
    return sonido
  
  def _alMoverCamara(self, evento):
    pass  
  
  def ajustarPosicion(self):
    self.camx, self.camy, self.camz = self.iku.camara.posicion
