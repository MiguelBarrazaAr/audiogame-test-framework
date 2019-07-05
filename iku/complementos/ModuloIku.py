#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

class ModuloIku():
  """de esta clase derivan todos los complementos que pueden ser vinculado al engine, como un engine plugin
  """
  
  def __init__(self, iku):
    self.iku = iku
    self.iniciar()
  
  def iniciar(self):
    pass