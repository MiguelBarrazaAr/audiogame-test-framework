#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

def iniciar(iku, motor, *args, **kwargs):
  if motor == 'pygame':
    from .pygame import PygameEngine
    return PygameEngine(iku, *args, **kwargs)
  elif motor == 'pyglet':
    from .pyglet import PygletEngine
    return PygletEngine(iku, *args, **kwargs)
  else:
    raise Exception("'{}' no es un motor gráfico valido para IkuEngine.".format(motor))