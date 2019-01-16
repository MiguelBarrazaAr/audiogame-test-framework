#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from ..eventos.evento import *

class Escena():
  """Representa una escena del juego"""
  
  def __init__(self, iku, *k, **kw):
    # iniciamos las propiedades comunes de todas las escenas:
    self.iku = iku
    self.colorFondo = (0,0,0)
    self._imagenFondo = None
    self._rutaFondo = None
    self.camara = iku.camara
    self.actores = []
    # iniciamos los eventos:
    self.mueveCamara = EventoControl()
    self.pulsaTecla = EventoControl()
    self.sueltaTecla = EventoControl()
    self.pulsaEscape = EventoControl()
    self.clickMouse = EventoControl()
    self.finalizaClickMouse = EventoControl()
    self.mueveMouse = EventoControl()
    self.cuandoActualiza = EventoControl()
    # conectamos el cerrar con escape
    self.pulsaEscape.conectar(self.alPulsarEscape)
  
  def __str__(self):
    return self.nombre
  
  @property
  def fondo(self):
    return self._rutaFondo
  
  @fondo.setter
  def fondo(self, ruta):
    if ruta is None:
      # elimina el fondo.
      self._imagenFondo = None
      self._rutaFondo = None
    else:
      self._imagenFondo = self.iku.imagen(ruta)
      self._rutaFondo = ruta
  
  def alPulsarEscape(self, evento):
    self.iku.finalizar()
  
  def noCerrarConEscape(self):
    self.pulsaEscape.desconectar(self.alPulsarEscape)
  
  @property
  def nombre(self):
    return self.__class__.__name__
  
  def actualizar(self, tick):
    for actor in self.actores:
      actor.actualizar(tick)
  
  def iniciar(self, *k, **kw):
    pass
  
  def eliminar(self):
    """elimina la escena de la pila de escenas cargadas
    queda como activa la ultima escena de la pila."""
    self.eliminarActores()
    self.iku.log(f"Eliminada la escena: '{self.nombre}'")
    self.iku.escenas.desapilar(self)
  
  def eliminarActores(self):
    """Elimina todos los actores de la escena."""
    for actor in reversed(self.actores):
      actor.eliminar()
  
  def activar(self):
    self.alActivar()
  
  def suspender(self):
    self.alSuspender()
  
  def limpiar(self):
    self.eliminarActores()
  
  def alActivar(self):
    """Metodo que se ejecuta al activar la escena."""
    pass
  
  def alSuspender(self):
    """Metodo que se ejecuta al cambiar de escena, y esta queda suspendida."""
    pass
  
  def agregarActor(self, actor):
    self.actores.append(actor)
    self.iku.log("ingresa en", self, "el actor", actor)
    self.iku.log("hay", len(self.actores), "actores en la escena", self)
  
  def eliminarActor(self, actor):
    self.actores.remove(actor)
    self.iku.log("se elimina en", self, "el actor", actor)
    self.iku.log("hay", len(self.actores), "actores en la escena", self)
  
  def dibujarEn(self, ventana):
    ventana.fill(self.colorFondo)
    if self._imagenFondo is not None:
      ventana.blit(self._imagenFondo, (0,0))
    # dibujamos actores:
    for actor in self.actores:
      actor.dibujarEn(ventana)
  
  def __getattr__(self, nombre):
    return eval(f"self.iku.{nombre}")
