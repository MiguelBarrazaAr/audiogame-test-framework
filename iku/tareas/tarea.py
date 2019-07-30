#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018: Miguel Barraza

class Tarea(object):
  def __init__(self, gestor, tiempo, demoraInicio, funcion, *args, **kwargs):
    self.gestor = gestor
    self.tiempo = tiempo
    self.demora = 0
    self.funcion = funcion
    self.args, self.kwargs = args, kwargs
  
  def ejecutar(self):
    self.tiempo += self.demora
    return self.funcion(*self.args, **self.kwargs)
  
  def eliminar(self):
    "Quita la tarea del gestor para que no se vuelva a ejecutar."
    self.gestor.eliminar(self)
  
  def terminar(self):
    "Termina la tarea (alias de eliminar)."
    self.eliminar()

class TareaCondicional(Tarea):
  """Representa una tarea con la particularidad que solo se sigue ejecutando si El
  retorno de la función a ejecutar devuelve True.
  """
  def ejecutar(self):
    """Se elimina si devuelve False."""
    if Tarea.ejecutar(self) == False:
      self.eliminar()

class TareaUnaVez(Tarea):
  """Representa una tarea que se ejecuta solo una vez."""
  def ejecutar(self):
    Tarea.ejecutar(self)
    self.eliminar()
