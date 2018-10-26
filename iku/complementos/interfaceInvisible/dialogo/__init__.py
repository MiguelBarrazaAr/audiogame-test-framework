#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

from iku.actores.actorInvisible  import ActorInvisible
from .mensaje import Mensaje
from .pregunta import Pregunta

class Dialogo(ActorInvisible):
  """representa a un diálogo de interacción con el jugador"""
  def iniciar(self, alfinalizar=None):
    self.nombre = None
    self.acciones = []
    self.indice=0
    self.alFinalizar = alfinalizar
  
  @property
  def finalizado(self):
    return self.indice+1 == len(self.acciones)
  
  def ejecutar(self):
    """Activa el diálogo."""
    self.habilitar()
    self.reproducir()
  
  def continuar(self):
    if self.finalizado:
      self.finalizar()
    else:
      self.indice+=1
      self.reproducir()
  
  def finalizar(self):
    self.indice = 0
    self.deshabilitar()
    if self.alFinalizar is not None:
      self.alFinalizar()
    self.eliminar()
  
  def reproducir(self):
    self.acciones[self.indice].ejecutar(self)
  
  # control de teclado:
  def _alPulsarTecla(self, evento):
    if(evento.tecla == self.iku.tecla.enter):
      self._siguiente()
    elif(evento.tecla == self.iku.tecla.espacio):
      self.reproducir()
    elif(evento.tecla == self.iku.tecla.f1):
      self._ayuda()
  
  def _siguiente(self):
    if self.finalizado:
      self.finalizar()
    else:
      self.continuar()
  
  def _ayuda(self):
    self.iku.leer("pulsa enter para continuar, o espacio para repetir .")
  
  
  # acciones que se pueden agregar:
  def mensaje(self, texto):
    """Agrega un mensaje al diálogo"""
    self.acciones.append(Mensaje(texto))
  
  def decir(self, nombre, texto):
    """Agrega un mensaje dicho por alguien."""
    self.acciones.append(Mensaje(nombre+" dice: "+texto))
  
  def preguntar(self, texto, opciones):
    self.acciones.append(Pregunta(texto, opciones))