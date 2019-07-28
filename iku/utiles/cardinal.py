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

def destino(p1, p2):
  """ dado 2 puntos determina hacia que destino se encuentra el segundo tomando como origen el primero. """
  x1, y1 = p1
  x2, y2 = p2
  if x1 == x2 and y1 < y2:
    return Cardinal.norte
  elif x1 == x2 and y1 > y2:
    return Cardinal.sur
  elif x1 < x2 and y1 == y2:
    return Cardinal.este
  elif x1 > x2 and y1 == y2:
    return Cardinal.oeste
  elif x1 < x2 and y1 < y2:
    return Cardinal.noreste
  elif x1 > x2 and y1 < y2:
    return Cardinal.noroeste
  elif x1 < x2 and y1 > y2:
    return Cardinal.sureste
  elif x1 > x2 and y1 > y2:
    return Cardinal.suroeste
  else:
    raise ValueError("los puntos son iguales.")

def esCompuesto(c):
  """ dado un cardinal retorna True si es un cardinal compuesto. """
  return (c.value % 2)==1

def descomponer(c):
  """ dado un cardinal compuesto lo descompone en simples. """
  if c is Cardinal.noreste:
    return (Cardinal.norte, Cardinal.este)
  elif c is Cardinal.sureste:
    return (Cardinal.sur, Cardinal.este)
  elif c is Cardinal.suroeste:
    return (Cardinal.sur, Cardinal.oeste)
  elif c is Cardinal.noroeste:
    return (Cardinal.norte, Cardinal.oeste)
  else:
    raise ValueError("'{}' No es un cardinal compuesto.".format(c))

def puntosHacia(posicion, destino, pasos):
  return [mover(posicion, destino, 1+n) for n in range(pasos)]

def verbalizarDestino(p1, p2, distancia):
  """ dado 2 puntos, retorna un texto para ser verbalizado donde explica la distancia entre esos 2 puntos.
  se debe pasar cual va a ser la distancia maxima a visualizar. """
  if all(x>distancia for x in (sum(y) for y in zip(p1, p2))):
    return "al {}".format(destino(p1,p2).name)
  else:
    return "cerquita."
  