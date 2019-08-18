#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .ElementoUi import ElementoUi

class UiNavegable(ElementoUi):
  """ representa un elemento que se puede navegar, se puede avanzar y retroceder en sus elementos. . """
  def __init__(self, texto, opciones=None, *args, **kwargs):
    self.limite = -1
    if opciones is None:
      opciones = []
    
    if isinstance(opciones, list):
      ElementoUi.__init__(self, texto, *args, **kwargs)
      self._lista = opciones
    else:
      ElementoUi.__init__(self, texto, opciones, *args, **kwargs)
      self._lista = []
    self._index=0
    self.circular = False
    self.anunciarIndice = False
    ElementoUi.__init__(self, texto, *args, **kwargs)
  
  @property
  def opcion(self):
    return self._lista[self._index]
  
  def agregar(self, opcion):
    self._lista.append(opcion)
  
  def insertar(self, indice, opcion):
    if self.limite != -1:
      if self.cantidadDeOpciones()+1 > self.limite:
        raise Warning("limite superado", self)
    self._lista.insert(indice, opcion)
  
  def agregarTodos(self, opciones):
    if isinstance(opciones, list):
      self._lista.extend(opciones)
    else:
      self.lanzarError(opciones)
  
  def lanzarError(self, obj):
    reporte = "Se esperaba una lista y se recibió un: "+obj.__class__.__name__
    raise TypeError(reporte)
  
  def cantidadDeOpciones(self):
    return len(self._lista)
  
  def siguiente(self):
    x = self._index+1
    if x < self.cantidadDeOpciones():
      self._index = x
    else:
      if self.circular:
        self.irAlPrimero()
      else:
        raise StopIteration("No hay siguiente elemento.")
  
  def anterior(self):
    x = self._index-1
    if x >= 0:
      self._index = x
    else:
      if self.circular:
        self.irAlUltimo()
      else:
        raise StopIteration("No hay siguiente elemento.")
  
  def irAlPrimero(self):
    self._index=0
  
  def irAlUltimo(self):
    self._index = self.cantidadDeOpciones()-1
  
  def pulsaEspacio(self):
    if not self._foco:
      super().pulsaEspacio()
  
  def limpiar(self):
    """ elimina todos los elementos listados. """
    self._lista.clear()
    self._index=0
