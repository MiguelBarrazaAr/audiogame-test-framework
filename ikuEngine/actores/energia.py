#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine
from .elemento import Elemento

class Energia(Elemento):
  """ Actor que simula carga de energía temporal.
  al mantener pulsado una tecla va contando el tiempo basado en ticks y lanza el evento al soltar la tecla. """
  def iniciar(self, *args, **kwargs):
    self.tecla = "espacio"
    self.contar = False
    self.ticks = 0
  
  def alPulsarTecla(self, evento):
    if evento.tecla == self.tecla:
      if evento.tipo == "pulsaTecla":
        self.contar=True
      else:
        self.contar=False
        self.ejecutar()
        self.ticks = 0
  
  def alHabilitar(self):
    self.eventos.sueltaTecla.conectar(self.alPulsarTecla)
  
  def alDeshabilitar(self):
    self.eventos.sueltaTecla.desconectar(self.alPulsarTecla)
  
  def actualizar(self, tick):
    if self.contar:
      self.ticks += 1
  
  def ejecutar(self):
    self.emitir(accion="energia", poder=self.ticks)