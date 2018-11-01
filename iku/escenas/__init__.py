#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import iku as ikuEngine
from .escena import Escena
from .normal import EscenaNormal

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
    #self.iniciarEscenasBase()
    self.iniciarEscenaDefault()
    
  @classmethod
  def registrar(cls, escenaClass):
    """Registra una escena personalizada"""
    # Se asegura de que la escena no fue vinculada anteriormente.
    nombre = escenaClass.__name__
    if getattr(cls, nombre, None):
      raise Exception("Error, ya existe una escena vinculada con el nombre: " + nombre)
    else:
      def crearEscena(self, *k, **kw):
        nuevaEscena = escenaClass(ikuEngine.instancia(), *k, **kw)
        self.apilar(nuevaEscena)
        nuevaEscena.iniciar(*k, **kw)
      
      # Vincula la clase anexando el metodo constructor.
      setattr(cls, nombre, crearEscena)
    
    cls.nombresDeEscenasPersonalizadas.append(nombre)
  
  def activar(self, id):
    """Activa una escena pasando la id de registro
    Si se pasan valores negativos contará desde atrás,
    por ejemplo: id=-1 activará la ultima escena de la listaEscenas."""
    if abs(id) >= len(self._listaEscenas):
      pass#raise Exception("La Id de la escena es invalida.")
    
    self._definirComoEscenaActual(self._listaEscenas[id])
  
  def buscarId(self, nombreDeLaEscena):
    """busca la ID de una escena apilada.
    se debe pasar el nombre de una escena previamente activada."""
    for id in range(len(self._listaEscenas)):
      if self._listaEscenas[id].nombre == nombreDeLaEscena:
        return id

    raise Exception("no existe ninguna escena cargada con el nombre '"+nombreDeLaEscena+"'")

  def actualizar(self):
    # actualiza la escena actual:
    self._escenaActual.actualizar()
  
  def _definirComoEscenaActual(self, escena):
    """Cambia de escena.
    se debe pasar como escena una escena válida que esté cargada en la lista_escena.
    este es un metodo privado. """
    self._escenaActual.guardarPosicionCamara()
    del self._escenaActual
    self._escenaActual = escena
    self._escenaActual.recuperarPosicionCamara()
    self.iku.log("Definiendo como activa la escena", escena)
  
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
    escena.alActivarEscena()
  
  def desapilar(self, escena):
    """elimina la escena de la pila de escenas cargadas.
    Si es la escenaActual: quedará como activa la ultima escena.
    precondición: en la pila de escenas tiene que haber almenos una"""
    if len(self._listaEscenas) <= 1:
      raise Exception("No puede ser eliminada la ultima escena de la pila.")
    
    self._listaEscenas.remove(escena)
    if self._escenaActual is escena:
      self.activar(-1)
