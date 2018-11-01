#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python 3.7
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku
from .actor import Actor

class Texto(Actor):
  """Representa un texto en pantalla.
  """
  def __init__(self, texto, *k, **kv):
    superficie = iku.instancia().fuente.render(texto, 0, (255, 255, 255))
    Actor.__init__(self, iku, imagen=superficie, **kv)
  