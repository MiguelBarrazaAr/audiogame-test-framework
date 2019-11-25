#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine

# mixin
class Conectable():
  def __init__(self, tipo='accion', iku=None):
    if iku is None:
      self.iku = ikuEngine.instancia()
    else:
      self.iku = iku
    self._acciones = self.iku.eventos.crear(tipo)
    self.conectar = self._acciones.conectar
    self.desconectar = self._acciones.desconectar
    self.emitir= self._acciones.emitir
