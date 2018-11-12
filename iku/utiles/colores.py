#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from enum import Enum

class Cardinal(Enum):
  # colores principales.
  negro = (0, 0, 0)
  blanco = (255, 255, 255)
  rojo = (255, 0, 0)
  verde = (0, 255, 0)
  azul = (0, 0, 255)
  gris = (128, 128, 128)
  
  # Colores secundarios
  amarillo = (255, 255, 0)
  magenta = (255, 0, 255)
  cyan = (0, 255, 255)
  grisClaro = (192, 192, 192)
  grisOscuro = (100, 100, 100)
  verdeOscuro = (0, 128, 0)
  azulOscuro = (0, 0, 128)
  naranja = (255, 200, 0)
  rosa = (255, 175, 175)
  violeta = (128, 0, 255)
  marron = (153, 102, 0)
