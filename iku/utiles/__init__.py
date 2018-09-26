#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
from .posicion import Posicion

class AttrDict(dict):
  """Envoltorio para que el diccionario de eventos
  se pueda acceder usando como si tuviera attributos
  de objeto."""
  def __init__(self, *args, **kwargs):
    dict.__init__(self, *args, **kwargs)
  
  def __getattr__(self, name):
    return self[name]

