#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from .cardinal import Cardinal

def moverAl(posicion, coord):
  """:param posicion, tipo Posicion.
  :param coord, tipo Cardinal."""
  paso=1
  p=posicion.copia()
  
  if coord == 0: # mueve al norte
    p.mover(y=paso)
  elif coord == 1: # mueve al noreste
    p.mover(x=paso, y=paso)
  elif coord == 2: # mueve al este
    p.mover(x=paso)
  elif coord == 3: # mueve al sureste
    p.mover(x=-paso, y=paso)
  elif coord == 4: # mueve al sur
    p.mover(y=-paso)
  elif coord == 5: # mueve al suroeste
    p.mover(x=-paso, y=-paso)
  elif coord == 6: # mueve al oeste
    p.mover(x=-paso)
  elif coord == 7: # mueve al noroeste
    p.mover(x=paso, y=-paso)
  return p