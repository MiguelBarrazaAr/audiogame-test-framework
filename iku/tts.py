#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# MajPy: Motor para Audio Juegos en python (3.7)
#
# Copyright 2017 - 2018 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import accessible_output2.outputs.auto

class TTS(object):
  """Controlador del habla."""
  def __init__(self):
    self.engine = accessible_output2.outputs.auto.Auto()
    self.historial = True
    self.limite = 3000
    self.eliminar = 1500
    self.msg = []
    self.index = 0
  
  def hablar(self, texto, interrumpir, registrar):
    self.engine.speak(texto, interrumpir)
    if registrar:
      self.msg.append(texto)
      self.index+=1
      if self.index >= self.limite:
        # eliminamos mensajes, se lleno el buffer.
        self.msg = self.msg[self.eliminar:]
  
  def texto(self, indice):
    return self.msg[indice]