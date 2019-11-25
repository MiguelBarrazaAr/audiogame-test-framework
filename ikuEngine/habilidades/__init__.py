#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

from .moverConFlechas import MoverConFlechas
from .emitirSonido import emitirSonido

skills = {'emitirsonido':emitirSonido,
  'moverconflechas':MoverConFlechas}

class Habilidades():
  """ Gestor de habilidades disponibles para actores en ikuEngine.
  las habilidades son funcionalidades que aprenden los actores.
  """
  def get(self, nombre):
    try:
      return skills[nombre.lower()]
    except KeyError:
      raise Exception("'{}' no es una habilidad valida.".format(nombre))