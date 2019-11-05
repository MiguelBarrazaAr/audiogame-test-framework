#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import ikuEngine

class Menu(ikuEngine.actores.ActorInvisible):
  """Representa un menu invisible de opciones navegable con flechas.
  """
  def __init__(self, nombre="menú", opciones=[], mensaje= "(pulse flechas para navegar por el menú)", habilitado=True):
    self._opciones = opciones
    self.nombre = nombre
    self.mensajeBienvenida = mensaje
    self.cantOpciones = len(opciones)
    self.indice = 0
    ikuEngine.actores.ActorInvisible.__init__(self)
    if habilitado:
      self.habilitar()
  
  def alHabilitar(self):
    """inicia el menú.
    este metodo puede ser llamado para reiniciar el menú y volverlo a presentar."""
    self.indice=0
    self.iku.leer(self.nombre+": "+self.mensajeBienvenida, False)
    self.iku.leer(self._opciones[self.indice][0], False)
    self._acciones.emitir(accion="iniciar",
      actor=self,
      indice=self.indice,
      opcion=self._opciones[self.indice][0])
  
  def opcion(self, texto, respuesta):
    """incorpora una opcion nueva al menu."""
    self.opciones.append((texto, respuesta))
    self.cantOpciones+=1
  
  def alPulsarTecla(self, evento):
    if evento.tecla == "arriba":
      self.seleccionar_anterior()
      self._acciones.emitir(accion="mover",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
    elif evento.tecla == "abajo":
      self.seleccionar_siguiente()
      self._acciones.emitir(accion="mover",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
    elif evento.tecla == "enter":
      self._acciones.emitir(accion="seleccionar",
        actor=self,
        indice=self.indice,
        opcion=self._opciones[self.indice][0])
      if len(self._opciones[self.indice]) == 3:
        self._opciones[self.indice][1](*self._opciones[self.indice][2:])
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
