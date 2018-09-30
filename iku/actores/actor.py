#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import iku as ikuEngine

class Actor(object):
  """Representa un objeto del juego que es parte de una escena, algo que se puede interactuar y tiene una posicion.
  """
  def __init__(self, iku, *k, **kv):
    if not iku:
      raise Exception(u"tienes que enviar 'iku' como argumento del actor al crearlo.")
    
    if not isinstance(iku, ikuEngine.Iku):
      raise Exception(u"Tienes que enviar el objeto 'iku' a la escena al crearla, pero llego esto: " +str(iku))
    
    self.iku = iku
    
    x = kv.get('x', 0)
    y = kv.get('y', 0)
    z = kv.get('z', 0)
    
    self._posicion = iku.posicion(x=x, y=y, z=z)
    self.radio_de_colision = 2
    self._vivo = True
    self.visible = True
    self.actualizable = True
    self.activo = False
    
    self.anexados = []
    
    self._image = None
    self.imagen = kv.get('imagen', None)
    self._acciones = self.iku.eventos.crear()
    self._iniciar(*k, **kv)
  
  def __str__(self):
    return     self.__class__.__name__
  
  @property
  def escena(self):
    """Referencia a la escena actual."""
    return self.iku.escenas.escenaActual
  
  @property
  def imagen(self):
    return self._image
  
  @imagen.setter
  def imagen(self, ruta):
    print("configurando imagen", ruta)
    if ruta is None:
      self._image = None
    else:
      self._image = self.iku.imagen(ruta)
      self.rect = self._image.get_rect()
      self.rect.centerx = self.iku.x
      self.rect.centery = self.iku.y
      print("coordenadas", self.rect.centerx, self.rect.centery)
      print("pantalla", self.iku.x, self.iku.y)
  
  @property
  def posicion(self):
    return self.iku.posicion(self.rect.centerx-self.iku.x, self.rect.centery-self.iku.y, self._z)
  
  @posicion.setter
  def posicion(self, pos):
    """Asigna la posición."""
    self.rect.centerx = pos.x
    self.rect.centery = pos.y
    self._z = pos.z
  
  @property
  def tipo(self):
    return     self.__class__.__name__
  
  @property
  def x(self):
    return self.rect.centerx
  
  @x.setter
  def x(self, n):
    self.rect.centerx = n
  
  @property
  def y(self):
    return self.rect.centery
  
  @y.setter
  def y(self, n):
    self.rect.centery = n
  
  @property
  def z(self):
    return self._posicion.z
  
  @z.setter
  def z(self, n):
    self._posicion.actualizar(z=n)
  
  
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

  def redimencionar(self,ancho,alto):
    self._image = self.iku.grafica.escalar(self._image, (ancho, alto))


  #def escala(self,escala):
    #self._image = self.iku.grafica.escalar(self._image,(self._image. *escala,*escala) )
