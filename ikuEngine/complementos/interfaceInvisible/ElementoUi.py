#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine

class ElementoUi(ikuEngine.actores.Elemento):
  """elemento de interface de usuario invisible,.
  clase abstracta.
  """
  def __init__(self, texto, respuesta=None, *args, **kwargs):
    self._texto = texto
    self._foco = False
    self.visibleConTab = True
    self.activarConTab = False
    self.leerAlActualizar = False
    if respuesta is None:
      self._respuesta = lambda: None
    else:
      self._respuesta = respuesta
    self.args = args
    self.kwargs = kwargs
    ikuEngine.actores.Elemento.__init__(self)
  
  @property
  def texto(self):
    return self._texto
  
  @texto.setter
  def texto(self, nuevoTexto):
    self._texto = nuevoTexto
    if self.leerAlActualizar:
      self.iku.leer(self._texto)
  
  @property
  def foco(self):
    return self._foco
  
  @foco.setter
  def foco(self, bool):
    self._foco = bool
  
  def __str__(self):
    return "{texto} {tipo}".format(texto=self._texto, tipo=self.tipo)
  
  def ejecutar(self):
    self._respuesta(*self.args, **self.kwargs)
  
  def pulsaEspacio(self):
    self.ejecutar()
  
  #controles con flechas: si retorna true pasa al siguiente elemento de la ui.
  def arriba(self):
    return True
  
  def abajo(self):
    return True
  
  def izquierda(self):
    pass
  
  def derecha(self):
    pass
  
  def tecla(self, tecla):
    return False
  
  def focoConTab(self):
    if self.activarConTab:
      self.foco = True
  