#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import iku

class Elemento(object):
  """Representa un elemento del juego que es parte de una escena, se actualiza en cada tick.
  """
  def __init__(self, actualizable=False, *k, **kv):
    self.iku = iku.instancia()
    self.actualizable = actualizable
    self._habilitado = False
    self._anexados = []
    
    self._acciones = self.iku.eventos.crear('accionActor')
    self.conectar = self._acciones.conectar
    self.desconectar = self._acciones.desconectar
    self.emitir= self._acciones.emitir
    self._iniciar(*k, **kv)
  
  def __repr__(self):
    """ es la información que se utiliza para imprimir el actor en el log. """
    return     self.__class__.__name__
  
  def __str__(self):
    """ es la información que se utiliza para que el tts lea el actor. """
    return     self.__class__.__name__
  
  @property
  def escena(self):
    """Referencia a la escena actual."""
    return self.iku.escena
  
  @property
  def tipo(self):
    return     self.__class__.__name__
  
  def dibujarEn(self, ventana):
    pass
  
  def actualizar(self, tick):
    pass
  
  def _iniciar(self, *k, **kv):
    self.preIniciar(*k, **kv)
    self.iniciar(*k, **kv)
    self.posIniciar(*k, **kv)
    self.escena.agregarActor(self)
  
  def preIniciar(self, *k, **kv):
    pass
  
  def iniciar(self, *k, **kv):
    pass
  
  def posIniciar(self, *k, **kv):
    pass
  
  def eliminar(self):
    self.iku.escena.eliminarActor(self)
    # eliminamos los anexados:
    for x in reversed(self._anexados):
      x.eliminar()
    del self
  
  def anexar(self, elemento):
    self._anexados.append(elemento)
    return elemento
  
  def desanexar(self, elemento):
    self._anexados.remove(elemento)
    return elemento
  
  def eliminarAnexados(self):
    for x in reversed(self._anexados):
      x.eliminar()
    self._anexados = []
  
  def buscarAnexado(self, filtro):
    for actor in self._anexados:
      if filtro(actor):
        return actor
    raise ValueError("No se encontro ningun elemento que cumpla con el filtro.")
  
  def habilitar(self):
    """ un elemento al ser habilitado se conecta al pulsa tecla. """
    if not self._habilitado:
      self.iku.eventos.pulsaTecla.conectar(self.alPulsarTecla)
      self._habilitado = True
      self._acciones.emitir(tipo="habilitar", actor=self)
      self.alHabilitar()
      self.iku.log("Actor {tipo} habilitado.".format(tipo=self.tipo))
    else:
      raise Exception("{tipo} no se puede habilitar porque ya está habilitado.".format(tipo=self.tipo))
  
  def alHabilitar(self):
    """ metodo que se invoca despues de habilitarlo. """
    pass
  
  def deshabilitar(self):
    """ deshabilita un elemento. """
    if self._habilitado:
      self.iku.eventos.pulsaTecla.desconectar(self.alPulsarTecla)
      self._habilitado = False
      self._acciones.emitir(tipo="deshabilitar", actor=self)
      self.alDeshabilitar()
      self.iku.log("Actor {tipo} deshabilitado.".format(tipo=self.tipo))
    else:
      raise Exception("No se puede deshabilitar el elemento {tipo} porque no fue habilitado.".format(self.tipo))
  
  def alDeshabilitar(self):
    pass
  
  @property
  def estaHabilitado(self):
    return self._habilitado
  
  def alPulsarTecla(self, evento):
    pass
  
  def __getattr__(self, nombre):
    try:
      return eval(f"self.iku.{nombre}")
    except AttributeError:
      raise AttributeError("el elemento '{type}' no conoce el atributo '{name}'".format(type=repr(self), name=nombre))    
