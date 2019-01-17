#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import iku as ikuEngine
from .escena import Escena
from .normal import EscenaNormal

class EscenaNoCargada(Exception):
  pass

class Escenas():
  """Representa la propiedad iku.escenas
  
  Este objeto se encarga de hacer accesibles
  todas las escenas que incluye iku.
  y de gestionarlas: actualizarlas.
  """
  nombresDeEscenasPersonalizadas = []
  
  def __init__(self, iku):
    self.iku = iku
    self._listaEscenas = []
    self._escenaActual = None
    
    # inicia las escenas base:
    self.iniciarEscenaDefault()
    
  @classmethod
  def registrar(cls, escenaClass, eliminable=False):
    """Registra una escena personalizada"""
    # Se asegura de que la escena no fue vinculada anteriormente.
    nombre = escenaClass.__name__
    if getattr(cls, nombre, None):
      raise Exception("Error, ya existe una escena vinculada con el nombre: " + nombre)
    else:
      def crearEscena(self, *k, **kw):
        try:
          self.activar(escenaClass.__name__)
        except EscenaNoCargada as e:
          # si la escena no esta cargada, la iniciamos:
          nuevaEscena = escenaClass(ikuEngine.instancia(), *k, **kw)
          self.apilar(nuevaEscena)
          nuevaEscena.iniciar(*k, **kw)
      
      # Vincula la clase anexando el metodo constructor.
      setattr(cls, nombre, crearEscena)
    
    cls.nombresDeEscenasPersonalizadas.append(nombre)
  
  def buscar(self, nombreDeLaEscena):
    """busca por nombre una escena apilada."""
    for escena in self._listaEscenas:
      if escena.nombre == nombreDeLaEscena:
        return escena

    raise EscenaNoCargada(f"no existe ninguna escena cargada con el nombre '{nombreDeLaEscena}'")
  
  def actualizar(self):
    # actualiza la escena actual:
    self._escenaActual.actualizar()
  
  def _definirComoEscenaActual(self, escena):
    """Cambia de escena. (método parcial)
    se debe pasar como escena una escena válida que esté cargada en la lista_escena."""
    self._escenaActual.suspender()
    self._escenaActual = escena
    self.iku.log(f"Definiendo como activa la escena: {escena}")
    self.iku.log(f"Hay {len(self._listaEscenas)} escenas activas.")
    self._escenaActual.activar()
    return escena
  
  def activar(self, nombreDeLaEscena):
    """Si la escena esta cargada, la pone como activa."""
    for escena in self._listaEscenas:
      if escena.nombre == nombreDeLaEscena:
        return self._definirComoEscenaActual(escena)
    raise EscenaNoCargada(f"no existe ninguna escena cargada con el nombre '{nombreDeLaEscena}'")
  
  @property
  def escenaActual(self):
      """Retorna la escena actual o None si no hay escena definida."""
      return self._escenaActual
  
  def iniciarEscenaDefault(self):
    """determina escenaNormal como predeterminada."""
    # invariante: esta escena no se puede eliminar.
    normal = EscenaNormal(self.iku)
    self._listaEscenas.append(normal)
    self._escenaActual=normal
  
  def limpiar(self):
    """Elimina todas las escenas del gestor."""
    pass
    #for x in self.escenas:
    #x._limpiar()
    #self.escenas = []
  
  def es_escena_vinculada(self, nombre_de_la_escena):
    respuesta = False
    return respuesta
  
  def apilar(self, escena):
    """Apila y activa una escena"""
    self._listaEscenas.append(escena)
    self._definirComoEscenaActual(escena)
  
  def desapilar(self, escena):
    """elimina la escena de la pila de escenas cargadas.
    Si es la escenaActual: quedará como activa la ultima escena.
    precondición: en la pila de escenas tiene que haber almenos una"""
    if len(self._listaEscenas) <= 1:
      raise Exception("No puede ser eliminada la ultima escena de la pila.")
    
    self._eliminar(escena)
    if self._escenaActual is escena:
      self._definirComoEscenaActual(self._listaEscenas[-1])
  
  def _eliminar(self, escena):
        self._listaEscenas.remove(escena)
