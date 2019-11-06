#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .UiNavegable import UiNavegable

class UiLista(UiNavegable):
  """representa a una lista de opciones de la interface invisible. """
  def __str__(self):
    if self.anunciarIndice:
      texto = "{texto}: presentación en lista. {opcion} {anuncio}".format(texto=self._texto, opcion=self.opcion, anuncio=self.anuncioDeIndice())
    else:
      texto = "{texto}: presentación en lista. {opcion}".format(texto=self._texto, opcion=self.opcion)
    return texto
  
  def derecha(self):
    try:
      self.siguiente()
    except:
      pass
    self.leer(self.opcion)
    if self.anunciarIndice:
      self.leer(self.anuncioDeIndice(), False)
    self.emitir(accion='mover', opcion=self.opcion, actor=self)
  
  def izquierda(self):
    try:
      self.anterior()
    except:
      pass
    self.leer(self.opcion)
    if self.anunciarIndice:
      self.leer(self.anuncioDeIndice(), False)
    self.emitir(accion='mover', opcion=self.opcion, actor=self)
  
  def abajo(self):
    if self._foco:
      self.derecha()
    return not self._foco
  
  def arriba(self):
    if self._foco:
      self.izquierda()
    return not self._foco
  
  def ejecutar(self):
    self._foco = not self._foco
    if self._foco:
      self.leer(self.__str__())
    else:
      self.leer("{opcion} (seleccionado)".format(opcion=self.opcion))
      self.emitir(accion='seleccionar', opcion=self.opcion, actor=self)
      self._respuesta(*self.args, **self.kwargs)
  
  def anuncioDeIndice(self):
    return "({n} de {m})".format(n=self._index+1, m=self.cantidadDeOpciones())
