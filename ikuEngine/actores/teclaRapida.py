#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import ikuEngine
from .elemento import Elemento

class TeclaRapida(Elemento):
  """ Actor que gestiona pulsaciones de teclas, util para lanzar informacion del juego. """
  def iniciar(self, *args, **kwargs):
    self._teclas = {}
  
  def alPulsarTecla(self, evento):
    if evento.tecla.name in self._teclas:
      func, args, kwargs = self._teclas[evento.tecla.name]
      func(*args, **kwargs)
  
  def agregar(self, tecla, funcion, *args, **kwargs):
    self._teclas[tecla] = (funcion, args, kwargs)
  
  def borrar(self, tecla):
    del self._teclas[tecla]
  
  def borrarTodo(self):
    self._teclas.clear()
  
  def limpiar(self):
    """ alias de borrar todo. """
    self.borrarTodo()
  
  def tieneTecla(self, tecla):
    return tecla in self._tecla