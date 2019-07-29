#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import iku

class ElementoNavegable(iku.actores.Elemento):
  """elemento navegable, permite anexar actores y moverse entre esos anexados con el tab."""
  def __init__(self, *k, **kv):
    iku.actores.Elemento.__init__(self)
    self._index=0
  
  @property
  def elemento(self):
    return self._anexados[self._index]
  
  @property
  def foco(self):
    return self._anexados[self._index]
  
  @foco.setter
  def foco(self, elemento):
    self._index = self._anexados.index(elemento)
    self.elemento.focoConTab()
    self.leerElementoEnfocado(False)
  
  def total(self):
    return len(self._anexados)
  
  def alPulsarTecla(self, evento):
    if evento.tecla == 'tab':
      if self.teclado.shiftPulsado():
        try:
          self.anterior()
        except StopIteration:
          self.ultimo()
      else:
        try:
          self.siguiente()
        except StopIteration:
          self.primero()
      
      self.leerElementoEnfocado()
      self.elemento.focoConTab()
  
  def leerElementoEnfocado(self, interrumpir=True):
    self.iku.leer(self.elemento, interrumpir)
  
  def ultimo(self):
    self._index = self.total()-1
  
  def siguiente(self):
    x = self._index+1
    if x < self.total():
      self._index = x  
    else:
      raise StopIteration("No hay siguiente elemento.")
  
  def primero(self):
    self._index=0
  
  def anterior(self):
    x = self._index-1
    if x >= 0:
      self._index = x
    else:
      raise StopIteration("No hay siguiente elemento.")
  