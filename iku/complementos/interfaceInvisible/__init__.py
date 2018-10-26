#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

from .dialogo import Dialogo
from .menu import Menu

class Complemento(object):
  def __init__(self, iku):
    iku.actores.vincular(Dialogo)
    iku.actores.vincular(Menu)
  