#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# 2019 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import datetime
from .utiles.Conectable import Conectable

class Log(Conectable):
  def __init__(self, iku):
    Conectable.__init__(self, iku=iku, tipo="accionLog")
    self.habilitar()
  
  def __imprimir__(self, datos):
    print(":: {hora} :: {tipo} :: {texto}".format(**datos))
  
  def habilitar(self):
    self.print = self.__imprimir__
  
  def deshabilitar(self):
    self.print = lambda *m: None
  
  def fecha(self):
    return datetime.datetime.now().strftime("%H:%M:%S")
  
  def __call__(self, *m):
    return self.__loggear__(tipo="info", texto=self.__process__(*m))
  
  def __loggear__(self, texto, tipo="info"):
    msg={"hora":self.fecha(), "texto":texto, "tipo":tipo}
    self.emitir(**msg)
    self.print(msg)
    return msg
  
  def __process__(self, *m):
    l = map(lambda x: repr(x), m)
    return " ".join(l)
  
  def __getattr__(self, clave):
    return lambda *m: self.__loggear__(tipo=clave, texto=self.__process__(*m))

class Mensaje():
  def __init__(self, hora, texto, tipo):
    self.hora = hora
    self.tipo = tipo
    self.texto = texto
  
  def __str__(self):
    return ":: {} :: {} :: {}".format(self.hora, self.tipo, self.texto)