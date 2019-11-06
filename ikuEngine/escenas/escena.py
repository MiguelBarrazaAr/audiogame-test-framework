#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

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
    self.pausables = [] # elementos que se tienen que pausar al perder el foco.
    self.eliminable = False # si esta propiedad esta en True se auto elimina al perder el foco.
    # iniciamos los eventos:
    self.mueveCamara = iku.eventos.crear("mueveCamara")
    self.pulsaTecla = iku.eventos.crear("pulsaTecla")
    self.sueltaTecla = iku.eventos.crear("sueltaTecla")
    self.pulsaEscape = iku.eventos.crear("pulsaEscape")
    self.clickMouse = iku.eventos.crear("clickMouse")
    self.sueltaClickMouse = iku.eventos.crear("sueltaClickMouse")
    self.mueveMouse = iku.eventos.crear("mueveMouse")
    self.cuandoActualiza = iku.eventos.crear("cuandoActualiza")
    # conectamos el cerrar con escape
    self.pulsaEscape.conectar(self.alPulsarEscape)
    self.nombre = self.__class__.__name__
  
  def __repr__(self):
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
  
  def actualizar(self, tick):
    for actor in self.actores:
      actor.actualizar(tick)
  
  def iniciar(self, *k, **kw):
    pass
  
  def eliminar(self):
    """limpia la escena y se elimina del gestor."""
    self.limpiar()
    self.iku.log(f"Eliminada la escena: '{self.nombre}'")
    self.iku.escenas.desapilar(self)
  
  def eliminarActores(self):
    """Elimina todos los actores de la escena."""
    for actor in reversed(self.actores):
      actor.eliminar()
    for p in reversed(self.pausables):
      p.pausar()
      del p
  
  def activar(self):
    self.alActivar()
    for ac in self.pausables:
      ac.continuar()
  
  def suspender(self):
    """Suspende la escena.
    Si 'eliminable' es True se auto elimina."""
    self.alSuspender()
    if self.eliminable:
      self.limpiar()
      self.iku.escenas._eliminar(self)
    else:
      # al suspender tiene que suspender sus elementos pausables:
      for ac in self.pausables:
        ac.pausar()
  
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
  
  def esEliminable(self):
    return self.eliminable
  
  def registrarPausable(self, actor):
    self.pausables.append(actor)
  
  def __getattr__(self, nombre):
    return eval(f"self.iku.{nombre}")
