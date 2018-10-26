#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

from iku.actores.actorInvisible import ActorInvisible

class Menu(ActorInvisible):
  """Representa un menu invisible de opciones navegable con flechas.
  """
  def __init__(self, iku, nombre="menú", opciones=[], mensaje= "(pulse flechas para navegar por el menú)", habilitado=True):
    self._opciones = opciones
    self.nombre = nombre
    self.mensajeBienvenida = mensaje
    self.cantOpciones = len(opciones)
    self.indice = 0
    ActorInvisible.__init__(self, iku=iku)
    if habilitado:
      self.habilitar()
  
  def _alHabilitar(self):
    """inicia el menú.
    este metodo puede ser llamado para reiniciar el menú y volverlo a presentar."""
    self.indice=0
    self.iku.leer(self.nombre+": "+self.mensajeBienvenida, False)
    self.iku.leer(self._opciones[self.indice][0], False)
    self._acciones.emitir(tipo="iniciar",
      actor=self,
      indice=self.indice,
      opcion=self._opciones[self.indice][0])
  
  def opcion(self, texto, respuesta):
    """incorpora una opcion nueva al menu."""
    self.opciones.append((texto, respuesta))
    self.cantOpciones+=1
  
  def _alPulsarTecla(self, evento):
    if evento.tecla == self.iku.tecla.arriba:
      self.seleccionar_anterior()
      self._acciones.emitir(tipo="mover",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
    elif evento.tecla == self.iku.tecla.abajo:
      self.seleccionar_siguiente()
      self._acciones.emitir(tipo="mover",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
    elif evento.tecla == self.iku.tecla.enter:
      self._acciones.emitir(tipo="seleccionar",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
      if len(self._opciones[self.indice]) == 3:
        self._opciones[self.indice][1](*self._opciones[self.indice][2])
      else:
        self._opciones[self.indice][1]()
  
  def seleccionar_anterior(self):
    if self.indice > 0:
      self.indice -= 1
    self.leer_opcion_actual()
  
  def seleccionar_siguiente(self):
    self.indice += 1
    if self.indice == self.cantOpciones:
      self.indice -= 1
    self.leer_opcion_actual()
  
  def leer_opcion_actual(self):
    self.iku.leer(self._opciones[self.indice][0])
  
  def eliminar(self):
    self.deshabilitar()
    super().eliminar()
