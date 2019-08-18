#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine

class Complemento():
  """de esta clase derivan todos los complementos que pueden ser vinculado al engine, como un engine plugin
  """
  
  def __init__(self, *args, **kwargs):
    self.iku = None
    self.iniciar(*args, **kwargs)
  
  def iniciar(self, *args, **kwargs):
    pass
  
  def _modificarMotor(self):
    """ acciones que se realiza al motor de iku cuando se inicializa con este complemento. """
    pass
  
  def requiereComplemento(self, nombre):
    """ verifica si se puede cargar el siguiente complemento. """
    ikuEngine.importarComplemento(nombre)