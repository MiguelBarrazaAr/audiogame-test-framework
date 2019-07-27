#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from enum import IntEnum  

class Cardinal(IntEnum):
  norte=0
  noreste=1
  este=2
  sureste=3
  sur=4
  suroeste=5
  oeste=6
  noroeste=7

def invertir(coord):
  return Cardinal((coord.value+4)%8)

def mover(posicion, cardinal, pasos=1):
  x, y = posicion
  if cardinal.name == 'norte':
    y+=pasos
  elif cardinal.name == 'sur':
    y-=pasos
  elif cardinal.name == 'este':
    x+=pasos
  elif cardinal.name == 'oeste':
    x-=pasos
  if cardinal.name == 'noreste':
    y+=pasos
    x+=pasos
  if cardinal.name == 'noroeste':
    y+=pasos
    x-=pasos
  if cardinal.name == 'sureste':
    y-=pasos
    x+=pasos
  if cardinal.name == 'suroeste':
    y-=pasos
    x-=pasos
  return (x, y)
