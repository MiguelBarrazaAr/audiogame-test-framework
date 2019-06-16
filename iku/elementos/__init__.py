#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import inspect


from .elemento import Elemento

class elementos():
  """Representa la propiedad iku.elementos
  
  Este objeto se encarga de hacer accesibles
  todos los elementos que incluye iku.
  y de gestionarlos.
  """
  nombresDeElementosPersonalizados = []
  
  def __init__(self, iku):
    self.iku = iku
    self.iniciarElementosDefault()
  
  @classmethod
  def registrar(cls, elementoClass, personalizado=True):
    """Registra un elemento
    Si personalizado es true, lo agrega a la lista de nombresDeElementosPersonalizados."""
    # Se asegura de que el elemento no fue vinculado anteriormente.
    nombre = elementoClass.__name__
    if getattr(cls, nombre, None):
      raise Exception("Error, ya existe un elemento vinculado con el nombre: " + nombre)
    else:
      def crearelemento(self, *k, **kv):
        return elementoClass(*k, **kv)
      
      # Vincula la clase anexando el metodo constructor.
      setattr(cls, nombre, crearelemento)
    
    if personalizado:
      cls.nombresDeElementosPersonalizados.append(nombre)
  
  def iniciarElementosDefault(self):
    #self.vincular(NavegadorDeElementos)
    pass
  
  def limpiar(self):
    """Elimina todos los elementos personalizados."""
    pass
  
  def vincular(self, elementoClass):
    self.registrar(elementoClass, False)
  
