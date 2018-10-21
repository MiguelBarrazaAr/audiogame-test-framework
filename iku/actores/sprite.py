﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import iku as ikuEngine

class Sprite(object):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, iku, *k, **kv):
    if not iku:
      raise Exception(u"tienes que enviar 'iku' como argumento del actor al crearlo.")
    
    if not isinstance(iku, ikuEngine.Iku):
      raise Exception(u"Tienes que enviar el objeto 'iku' al actor al crearlo, pero llego esto: " +str(iku))
    
    self.iku = iku
    
    self._vivo = True
    self.actualizable = True
    self.activo = False
    self.colisionable = True
    
    self.anexados = []
    
    self._acciones = self.iku.eventos.crear()
    self._iniciar(*k, **kv)
  
  def __str__(self):
    return     self.__class__.__name__
  
  @property
  def escena(self):
    """Referencia a la escena actual."""
    return self.iku.escenas.escenaActual
  
  @property
  def tipo(self):
    return     self.__class__.__name__
  
  def actualizar(self):
    pass
  
  def _iniciar(self, *k, **kv):
    self.preIniciar(*k, **kv)
    self.iniciar(*k, **kv)
    self.posIniciar(*k, **kv)
    self.iku.escenas.escenaActual.agregarActor(self)
  
  def preIniciar(self, *k, **kv):
    pass
  
  def iniciar(self, *k, **kv):
    pass
  
  def posIniciar(self, *k, **kv):
    pass
  
  def eliminar(self):
    self.iku.escenas.escenaActual.eliminarActor(self)
    # eliminamos los anexados:
    for x in reversed(self.anexados):
      x.eliminar()
    del self
  
  def anexar(self, actor):
    self.anexados.append(actor)
  
  def desanexar(self, actor):
    self.anexados.remove(actor)
  
  def eliminarAnexados(self):
    for x in reversed(self.anexados):
      x.eliminar()
    self.anexados = []
  
  def habilitar(self):
    self.iku.eventos.pulsaTecla.conectar(self._alPulsarTecla)
    self.activo = True
    self._acciones.emitir(tipo="habilitar", actor=self)
    self._alHabilitar()
    self.iku.log("Actor {tipo} habilitado.".format(tipo=self.tipo))
  
  def _alHabilitar(self):
    pass
  
  def deshabilitar(self):
    self.iku.eventos.pulsaTecla.desconectar(self._alPulsarTecla)
    self.activo = False
    self._acciones.emitir(tipo="deshabilitar", actor=self)
    self._alDeshabilitar()
    self.iku.log("Actor {tipo} deshabilitado.".format(tipo=self.tipo))
  
  def _alDeshabilitar(self):
    pass
  
  def _alPulsarTecla(self, evento):
    pass
  
  def conectar(self, respuesta):
    self._acciones.conectar(respuesta)
  
  def desconectar(self, respuesta):
    self._acciones.desconectar(respuesta)
  
  def mover(self, x=0, y=0):
    self.figura.move_ip(x,y)
  
