#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class SoundPool(object):
  """Pool que gestiona todo los sonidos del juego"""
  def __init__(self, iku, cantidadDeSonidos=200):
    self.iku = iku
    self.cantidadDeSonidos = cantidadDeSonidos
    self.x = 0
    self.lista = [None]*cantidadDeSonidos
  
  def reproducir(self, ruta):
    """carga y reproduce un sonido"""
    self.lista[self.x] = self.iku.sonido(ruta)
    self.lista[self.x].reproducir()
    self.x = (self.x+1)%self.cantidadDeSonidos
