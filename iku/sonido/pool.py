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
  
  def reproducir(self, ruta, posicion=(0,0,0)):
    """carga y reproduce un sonido"""
    px, py, pz = posicion
    pos = (px-self.camx, py-self.camy, pz-self.camz)
    self.lista[self.x] = self.iku.sonido3d(ruta, pos)
    sonido= self.lista[self.x]
    sonido.reproducir()
    self.x = (self.x+1)%self.cantidadDeSonidos
    return sonido
  
  def _alMoverCamara(self, evento):
    print("mueve camara", evento)
  
  def ajustarPosicion(self):
    self.camx, self.camy, self.camz = self.iku.camara.posicion
    print("ajjustada", self.iku.camara.posicion)

