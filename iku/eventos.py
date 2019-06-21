#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import weakref
import types
import inspect

from iku.utiles import AttrDict

class Eventos(object):
  """Representa la propiedad iku.eventos
  
  Este objeto se encarga de gestionar y propagar eventos.
  """
  def __init__(self, iku):
    self.iku = iku
    # eventos genericos:
    self.usuario = self.crear()
    self.juego = self.crear()
    self.servidor = self.crear()
  
  def crear(self):
    """Crea un nuevo evento"""
    return EventoControl()
  
  @property
  def pulsaTecla(self):
    return self.iku.escena.pulsaTecla
  
  @property
  def sueltaTecla(self):
    return self.iku.escena.sueltaTecla
  
  @property
  def pulsaEscape(self):
    return self.iku.escena.pulsaEscape
  
  @property
  def clickMouse(self):
    return self.iku.escena.clickMouse
  
  @property
  def finalizaClickMouse(self):
    return self.iku.escena.finalizaClickMouse
  
  @property
  def mueveMouse(self):
    return self.iku.escena.mueveMouse
  
  @property
  def cuandoActualiza(self):
    return self.iku.escena.cuandoActualiza
  
  @property
  def mueveCamara(self):
    return self.iku.camara.evento


class EventoControl(object):
  """Representa a un controlador de evento, el objeto que gestiona la observación de un evento."""
  def __init__(self):
    self.respuestas = []
  
  def conectar(self, respuesta, id=None):
    if inspect.isfunction(respuesta):
      self.respuestas.append(ProxyFuncion(respuesta, id))
    elif inspect.ismethod(respuesta):
      self.respuestas.append(ProxyMetodo(respuesta, id))
    else:
      raise ValueError("Solo se permite conectar nombres de funciones o metodos.")
  
  def desconectar(self, respuesta):
    for res in self.respuestas:
      if res.func == respuesta:
        self.eliminar(res)
  
  def eliminar(self, respuesta):
    """Elimina una respuesta de este evento."""
    try:
      self.respuestas.remove(respuesta)
    except:
      raise ValueError("La funcion indicada no estaba agregada como respuesta del evento.")
  
  def desconectar_por_id(self, id):
    """busca por una id una respuesta agregada y la elimina"""
    a_eliminar = []
    for respuesta in self.respuestas:
      if respuesta.id == id:
        a_eliminar.append(respuesta)
    
    for x in a_eliminar:
      self.eliminar(x)
  
  def emitir(self, **kwargs):
    for respuesta in self.respuestas:
      try:
        respuesta(Evento(kwargs))
      except Exception as e:
        self.desconectar(respuesta)
        raise e

class ProxyFuncion(object):
  """Representa a una función de repuesta pero usando
  una referencia débil.
  extraido de pilas engine 1.4."""
  def __init__(self, cb, id):
    self.func = weakref.ref(cb)
    self.id = id
    self.nombre = str(cb)
    self.receptor = str('modulo actual')
  
  def __call__(self, evento):
    f = self.func()
    
    if f is not None:
      f(AttrDict(evento))
    else:
      raise ReferenceError("La funcion dejo de existir")

class ProxyMetodo(object):
  """Permite asociar funciones pero con referencias débiles, que no incrementan el contador de referencias.
  Este proxy funciona tanto con funciones como con métodos enlazados a un objeto.
  @organization: IBM Corporation
  @copyright: Copyright (c) 2005, 2006 IBM Corporation
  @license: The BSD License"""
  def __init__(self, cb, id):
    try:
      try:
        self.inst = weakref.ref(cb.im_self)
      except TypeError:
        self.inst = None
      self.func = cb.im_func
      self.klass = cb.im_class
    except AttributeError:
      self.inst = None
      try:
        self.func = cb.im_func
      except AttributeError:
        self.func = cb
      
      self.klass = None
    
    self.id = id
    self.nombre = str(cb.__name__)
    self.receptor = self.klass
  
  def __call__(self, evento):
    if self.inst is not None and self.inst() is None:
      ## WARN TODO: informar que el metodo ha dejado de existir
      #raise ReferenceError("El metodo ha dejado de existir")
      return
    elif self.inst is not None:
      mtd = types.MethodType(self.func, self.inst())
    else:
      mtd = self.func
    
    return mtd(evento)
  
  def __eq__(self, other):
    try:
      return self.func == other.func and self.inst() == other.inst()
    except Exception:
      return False
  
  def __ne__(self, other):
    return not self.__eq__(other)

class Evento(AttrDict):
    pass

