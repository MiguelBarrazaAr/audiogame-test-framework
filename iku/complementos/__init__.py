#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import inspect
import os.path
import importlib

class Complementos(object):
  """Representa la propiedad iku.complementos
  
  Este objeto se encarga de hacer accesibles todos los complementos que incluye iku, también de gestionarlos y actualizarlos.
  """
  
  def __init__(self, iku, cargarComplementos=False):
    self.iku = iku
    self.plugins = []
    if cargarComplementos:
      self._cargarComplementos()
  
  def activar(self, modulo):
    """Registra y activa un complemento."""
    # Se asegura de que el plugin no fue vinculado anteriormente.
    nombre = modulo.__name__
    if nombre in self.plugins:
      raise Exception("Error, ya existe un complemento vinculado con el nombre: " + nombre)
    else:
      # cargamos el plugin:
      setattr(self, nombre, modulo.Complemento(self.iku))
      self.plugins.append(nombre)
  
  def _cargarComplementos(self):
    self._cargarComplementosDe(__path__[0])
    self.iku.log("Se cargaron", len(self.plugins), "complementos.")
  
  def _cargarComplementosDe(self, ruta):
    for nombre in self.iku.listarDirectorio(ruta):
      if os.path.isdir(ruta+"/"+nombre) and nombre[0:2] != "__":
        modulo = importlib.import_module("iku.complementos."+nombre)
        self.activar(modulo)
  
  def instalar(self, complemento):
    if type(complemento) == str:
      modulo = importlib.import_module("iku.complementos."+nombre)
    else:
      modulo = complemento
    self.activar(modulo)
