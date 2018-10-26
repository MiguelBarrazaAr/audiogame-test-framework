#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

class Mensaje(object):
  """representa a un diálogo de interacción con el jugador"""
  def __init__(self, texto):
    self.texto = texto
  
  def ejecutar(self, dialogo):
    dialogo.iku.leer(self.texto)