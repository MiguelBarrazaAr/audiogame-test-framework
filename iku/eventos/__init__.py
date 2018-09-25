#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from .evento import *

class Eventos(object):
  """Representa la propiedad iku.eventos
  
  Este objeto se encarga de gestionar y propagar eventos.
  """
  def __init__(self, iku):
    self.iku = iku
    # eventos genericos:
    self.finalizaMotor = self.crear()
    self.finalizaServidor = self.crear()
    self.servidor = self.crear()
  
  def crear(self):
    """Crea un nuevo evento"""
    return EventoControl()

  @property
  def pulsaTecla(self):
    return self.iku.escenas.escenaActual.pulsaTecla
  
  @property
  def pulsaEscape(self):
    return self.iku.escenas.escenaActual.pulsaEscape
  
  def __getattr__(self, at):
    print("recibo: "+at)
