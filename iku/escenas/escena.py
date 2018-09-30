#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

#from ..Iku import Iku
from ..eventos.evento import *

class Escena():
  """Representa una escena del juego"""
  
  def __init__(self, iku, *k, **kw):
    if not iku:
      raise Exception(u"tienes que enviar 'iku' como argumento de la escena al crearla.")
    
    #if not isinstance(iku, Iku):
      #raise Exception(u"Tienes que enviar el objeto 'iku' a la escena al crearla, pero llego esto: " +str(iku))
    
    # iniciamos las propiedades comunes de todas las escenas:
    self.iku = iku
    self.colorFondo = (0,0,0)
    self.fondo = None
    self.camara = iku.camara
    self.actores = []
    
    # acomodamos la camara:
    self.camara.reiniciar()
    self.guardarPosicionCamara()
    
    # iniciamos los eventos:
    self.mueveCamara = EventoControl()
    self.pulsaEscape = EventoControl()
    self.pulsaTecla = EventoControl()
    # conectamos el cerrar con escape
    self.pulsaEscape.conectar(self.alPulsarEscape)
  
  def __str__(self):
    return self.nombre
  
  def alPulsarEscape(self, evento):
    self.iku.finalizar()
  
  def noCerrarConEscape(self):
    self.pulsaEscape.desconectar(self.alPulsarEscape)
  
  @property
  def nombre(self):
    return self.__class__.__name__
  
  def actualizar(self):
    pass
  
  def iniciar(self, *k, **kw):
    pass
  
  def eliminar(self):
    """elimina la escena de la pila de escenas cargadas
    queda como activa la ultima escena de la pila."""
    self.iku.log("Eliminada la escena:", self.nombre)
    self.iku.escenas.desapilar(self)
  
  def alActivarEscena(self):
    """Metodo que se ejecuta al activar la escena."""
    pass
  
  def AlRecargarEscena(self):
    """Metodo que se llama al retomar foco la escena
    cuando vuelve a ser escena_actual.
    nota: se debe redefinir."""
    pass
  
  def agregarActor(self, actor):
    self.actores.append(actor)
    self.iku.log("ingresa en", self, "el actor", actor)
    self.iku.log("hay", len(self.actores), "actores en la escena", self)
  
  def eliminarActor(self, actor):
    self.actores.remove(actor)
    self.iku.log("se elimina en", self, "el actor", actor)
    self.iku.log("hay", len(self.actores), "actores en la escena", self)
  
  def guardarPosicionCamara(self):
    """ Este método se llama cuando se cambia de escena y así poder
    recuperar la ubicación de la cámara en la escena actual
    """
    self.posicionCamara = self.camara.posicion
  
  def recuperarPosicionCamara(self):
    self.camara.posicion = self.posicionCamara
