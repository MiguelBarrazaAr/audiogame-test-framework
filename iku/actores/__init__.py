﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import inspect

from .actor import Actor

class Actores():
  """Representa la propiedad iku.actores
  
  Este objeto se encarga de hacer accesibles
  todos los actores que incluye iku.
  y de gestionarlos: actualizarlos.
  """
  nombresDeActoresPersonalizados = []
  
  def __init__(self, iku):
    self.iku = iku
    self.iniciarActoresDefault()
  
  @classmethod
  def registrar(cls, actorClass, personalizado=True):
    """Registra un actor
    Si personalizado es true, lo agrega a la lista de nombresDeActoresPersonalizados."""
    # Se asegura de que el actor no fue vinculado anteriormente.
    nombre = actorClass.__name__
    if getattr(cls, nombre, None):
      raise Exception("Error, ya existe un actor vinculado con el nombre: " + nombre)
    else:
      def crearActor(self, *k, **kv):
        return actorClass(*k, **kv)
      
      # Vincula la clase anexando el metodo constructor.
      setattr(cls, nombre, crearActor)
    
    if personalizado:
      cls.nombresDeActoresPersonalizados.append(nombre)
  
  def iniciarActoresDefault(self):
    self.vincular(Dialogo)
    self.vincular(Menu)
    self.vincular(NavegadorDeElementos)
  
  def limpiar(self):
    """Elimina todos los actores personalizados."""
    pass
  
  def vincular(self, actorClass):
    self.registrar(actorClass, False)
  