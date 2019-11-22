#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

from .pygame import PygameEngine

def iniciar(iku, motor, *args, **kwargs):
  if motor == 'pygame':
    return PygameEngine(iku, *args, **kwargs)
  else:
    raise Exception("'{}' no es un motor gráfico valido para IkuEngine.".format(motor))