#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import iku

class Sprite(object):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, visible=True, actualizable=False, colisionable=False, *k, **kv):
    self.iku = iku.instancia()
    self._vivo = True
    self.visible = visible
    self.actualizable = actualizable
    self.activo = False
    self.colisionable = colisionable
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
  
  def actualizar(self, tick):
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
  
  def dibujarEn(self, superficie):
    pass
  
  @property
  def x(self):
    return self.figura.centerx
  
  @property
  def y(self):
    return self.figura.centery
  
  @property
  def posicion(self):
    return self.figura.center
  
  @property
  def posicion3d(self):
    return (self.figura.centerx, self.figura.centery, 0)
  
  @posicion.setter
  def posicion(self, tupla):
    self.figura.center = tupla   
  
  @property
  def ancho(self):
    return self.figura.w
  
  @property
  def alto(self):
    return self.figura.h
  
  def mover(self, x=0, y=0):
    self.figura.move_ip(x,y)
  
  def coordenadaAlMover(self, x=0, y=0):
    return (self.x+x, self.y+y)
  
  def __getattr__(self, nombre):
    return eval(f"self.iku.{nombre}")
