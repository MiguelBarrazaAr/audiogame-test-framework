#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku_engine: Motor para Audio Juegos en python (3.7)
#
# Copyright 2019 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class Tecla():
  def __init__(self, tecla):
    self.tecla = tecla
  
  def __eq__(self, obj):
    return self.tecla == obj or self.tecla.name == obj or self.tecla.value == obj
  
  def __hash__(self):
    return self.tecla
  
  @property
  def name(self):
    return self.tecla.name
  
  @property
  def value(self):
    return self.tecla.value

class Teclado():
  def __init__(self, iku):
    self.iku = iku
    self._teclas = [] # lista de teclas pulsadas.
  
  def actualizar(self, teclas):
    self._teclas = teclas
  
  def tecla(self, cod):
    return Tecla(self.iku.tecla(cod))
  
  def estaPulsado(self, nombre):
    try:
      return self._teclas[self.iku.tecla[nombre].value]
    except KeyError:
      raise ValueError("'{tecla}' no es un codigo de tecla valido.".format(tecla=nombre))
  
