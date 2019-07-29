#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .UiNavegable import UiNavegable

class UiIngresaTexto(UiNavegable):
  """representa a un cuadro de texto de la interface invisible. """
  def iniciar(self, *args, **kwargs):
    self.soloLetrasYNumeros() # filtro activo por default.
    self.activarConTab = True
  
  @property
  def tipo(self):
    return "cuadro de edición"
  
  def __str__(self):
    return "{etiqueta} {tipo}: {texto}".format(etiqueta=self.etiqueta, tipo=self.tipo, texto=self.texto)
  
  @property
  def texto(self):
    return "".join(self._lista)
  
  @property
  def etiqueta(self):
    return self._texto
  
  def ejecutar(self):
    self._foco = not self._foco
    if self._foco:
      self.leer(self.__str__())
      self.leer(self.texto, False)
    else:
      try:
        self.respuesta()
      except AttributeError:
        pass
  
  def tecla(self, evento):
    if self._foco:
      if evento.tecla == "borrar":
        self.borrar(1)
      if evento.tecla == "suprimir":
        self.borrar()
      elif self._filtro(evento.representacion):
        self.insertar(self._index, evento.representacion)
        self._index+=1
  
  def borrar(self, desplazamiento=0):
    try:
      self._index-=desplazamiento
      self.leer(self._lista.pop(self._index))
    except IndexError:
      pass
  
  def derecha(self):
    try:
      self.siguiente()
    except:
      self._index = self.cantidadDeOpciones()
    else:
      self.leer(self.opcion)
  
  def izquierda(self):
    try:
      self.anterior()
    except StopIteration:
      pass
    if self.cantidadDeOpciones() > 0:
      self.leer(self.opcion)
  
  def abajo(self):
    if self._foco:
      self.leer(self.__str__())
    return not self._foco
  
  def arriba(self):
    self.abajo()
  
  # filtros que se pueden usar:
  def cualquierCaracter(self):
    self._filtro = CualquierCaracter()
  
  def soloNumeros(self):
    self._filtro = SoloNumeros()
  
  def soloLetras(self):
    self._filtro = SoloLetras()
  
  def soloLetrasYNumeros(self):
    self._filtro = SoloLetrasYNumeros()



# filtros:
class Filtro():
  def __str__(self):
    return self.__class__.__name__


class SoloLetras(Filtro):
  def __call__(self, simbolo):
    return simbolo.isalpha()

class SoloLetrasYNumeros(Filtro):
  def __call__(self, simbolo):
    return simbolo.isalnum()

class SoloNumeros(Filtro):
  def __call__(self, simbolo):
    return simbolo.isdigit()

class CualquierCaracter(Filtro):
  def __call__(self, simbolo):
    return simbolo != "" and simbolo.isprintable()