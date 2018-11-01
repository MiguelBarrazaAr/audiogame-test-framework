#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

class Pregunta(object):
  """representa a un diálogo de pregunta."""
  def __init__(self, texto, opciones):
    self.texto = texto
    self.opciones= []
    for texto,respuesta in opciones:
      self.opciones.append((texto, self.finalizar, [respuesta]))
  
  def ejecutar(self, dialogo):
    dialogo.deshabilitar()
    self.dialogo = dialogo
    mensaje=self.texto+". (pulse las flechas para seleccionar una opción y enter para confirmar)."
    self.menu = dialogo.iku.actores.Menu("Pregunta", self.opciones, mensaje=mensaje)
  
  def finalizar(self, respuesta):
    respuesta()
    self.dialogo.habilitar()
    self.dialogo.continuar()
    self.menu.eliminar()