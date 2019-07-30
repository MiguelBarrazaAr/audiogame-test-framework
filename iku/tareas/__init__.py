#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018: Miguel Barraza

from .tarea import *

class Tareas(object):
  """Gestor de tareas a ejecutar por tiempo."""
  def __init__(self, iku):
    self.tareas = []
    self.iku = iku
  
  def cantidadDeTareas(self):
    return len(self.tareas)
  
  def actualizar(self, tick):
    #ejecutamos tareas:
    for tarea in self.tareas:
      if tarea.tiempo < self.iku._timestamp:
        tarea.ejecutar()
      else:
        break
  
  def _agregar(self, tarea):
    """Agrega una nueva tarea para ejecutarse luego.
    :param tarea: Referencia a la tarea que se debe agregar.
    """
    try:
      id = next((id for id,t in enumerate(self.tareas) if t.tiempo > tarea.tiempo))
    except StopIteration:
      self.tareas.append(tarea)
    else:
      self.tareas.insert(id, tarea)
  
  def eliminar(self, tarea):
    self.tareas.remove(tarea)
  
  def unaVez(self, tiempo, funcion, *args, **kwargs):
    """Genera una tarea que se ejecutará una sola vez.
    :param tiemmpo: Cantidad de segundos que deben transcurrir para ejecutar la tarea.
    :param funcion: Función a ejecutar para lanzar la tarea.
    :param parametros: Parámetros que tiene que recibir la función a ejecutar.
    """
    tarea = TareaUnaVez(self, self.iku._timestamp+tiempo, 0, funcion, *args, **kwargs)
    self._agregar(tarea)
    return tarea
  
  def siempre(self, tiempo, funcion, demora=0, *args, **kwargs):
    """Genera una tarea para ejecutar todo el tiempo, sin espiración.
    :param tiempo: Cantidad de segundos que deben transcurrir para ejecutar la tarea.
    :param funcion: Función a ejecutar para lanzar la tarea.
    :param demora: La demora en segundos que tiene para ejecutarse por primera vez.
    """
    tarea = Tarea(self, self.iku._timestamp+tiempo, demora, funcion, *args, **kwargs)
    self._agregar(tarea)
    return tarea
  
  def condicional(self, tiempo, funcion, demora=0, *args, **kwargs):
    """Genera una tarea que se puede ejecutar una vez o mas, pero que tiene una condición.
    La tarea se ejecutará hasta que la función a ejecutar devuelva False.
    :param tiempo: Cantidad de segundos que deben transcurrir para ejecutar la tarea.
    :param funcion: Función a ejecutar para lanzar la tarea.
    :param demora: La demora en segundos que tiene para ejecutarse por primera vez.
    """
    tarea = TareaCondicional(self, self.iku._timestamp+tiempo, demora, funcion, *args, **kwargs)
    self._agregar(tarea)
    return tarea
  
  def eliminarTodas(self):
    """Elimina todas las tareas."""
    self.tareas = []
