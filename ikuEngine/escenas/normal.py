#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from .escena import Escena

class EscenaNormal(Escena):
  """Representa una escena principal que se carga al iniciar el juego.
  Sin actores ni funcionalidad,
  limpia para poder hacer pruebas o diseñar una pantalla principal.
  si no se define escena al iniciar Iku, esta es la que queda por defecto.
  """
  pass
