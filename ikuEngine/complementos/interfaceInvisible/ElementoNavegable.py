#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine

class ElementoNavegable(ikuEngine.actores.Elemento):
  """elemento navegable, permite anexar actores y moverse entre esos anexados con el tab."""
  def __init__(self, *k, **kv):
    ikuEngine.actores.Elemento.__init__(self)
    self._index=0
    self.leerAlTomarFoco = True
  
  @property
  def elemento(self):
    return self._anexados[self._index]
  
  def getElement(self, index):
    return self._anexados[index]
  
  @property
  def foco(self):
    return self._anexados[self._index]
  
  @foco.setter
  def foco(self, elemento):
    self._index = self._anexados.index(elemento)
    self.elemento.focoConTab()
    if self.leerAlTomarFoco:
      self.leerElementoEnfocado(False)
  
  def total(self):
    return len(self._anexados)
  
  def alPulsarTecla(self, evento):
    if evento.tecla == 'tab':
      try:
        if self.teclado.shiftPulsado():
          try:
            self.anterior(tab=True)
          except StopIteration:
            self.anterior(tab=True, index=self.total())
        else:
          try:
            self.siguiente(tab=True)
          except StopIteration:
            self.siguiente(tab=True, index=-1)
      except StopIteration:
        self.errorNoHayElementos()
        if self.elemento.visibleConTab:
          self.leerElementoEnfocado(False)
      else:
        self.elemento.focoConTab()
        self.leerElementoEnfocado()
      return True
  
  def leerElementoEnfocado(self, interrumpir=True):
    self.iku.leer(self.elemento, interrumpir)
  
  def ultimo(self):
    self._index = self.total()-1
  
  def siguiente(self, tab=False, index=None):
    index = index if index is not None else self._index
    index+=1
    if index >= self.total():
      raise StopIteration("No hay siguiente elemento.")
    
    elemento = self.getElement(index)
    if tab and not elemento.visibleConTab: # verificamos si es visible con tab:
      self.siguiente(tab, index)
    else:
      self._index = index  
  
  def primero(self):
    self._index=0
  
  def anterior(self, tab=False, index=None):
    index = index if index is not None else self._index
    index-=1
    if index < 0:
      raise StopIteration("No hay siguiente elemento.")
    
    elemento = self.getElement(index)
    if tab and not elemento.visibleConTab: # verificamos si es visible con tab:
      self.anterior(tab, index)
    else:
      self._index = index

  def errorNoHayElementos(self):
    self.iku.leer("No hay mas elementos.")