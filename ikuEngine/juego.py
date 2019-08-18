#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class Juego(object):
  """representa al modelo del juego, todo lo que no es parte de una escena, pero puede ser consultado y es actualizable. """
  def __init__(self, iku):
    self.iku = iku
    self.evento = iku.eventos.crear('eventoJuego')
    self.activo = False
  
  def actualizar(self):
    pass