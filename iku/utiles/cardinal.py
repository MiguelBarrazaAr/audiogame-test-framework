#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from enum import IntEnum  

class Cardinal(IntEnum):
  norte=0
  n=0
  noreste=1
  ne=1
  este=2
  e=2
  sureste=3
  se=3
  sur=4
  s=4
  suroeste=5
  so=5
  oeste=6
  o=6
  noroeste=7
  no=7

def invertir(coord):
  return Cardinal((coord.value+4)%8)
