#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

from .ElementoNavegable import ElementoNavegable

class Contenedor(ElementoNavegable):
  """Contenedor de elemetnos de interface de usuario."""
  def __init__(self, *k, **kv):
    ElementoNavegable.__init__(self)
    self._accessKey = {}
    self.leerAlHabilitar = True
    self.interrumpirLecturaAlHabilitar = True
    self.mostrar = self.habilitar
  
  def alPulsarTecla(self, evento):
    try:
      # si tiene una tecla rápida la ejecutamos:
      if evento.tecla.name  in self._accessKey:
        self._accessKey[evento.tecla.name]()
      
      self.elemento.tecla(evento)
      if evento.tecla == 'enter':
        self.elemento.ejecutar()
        return True
      elif evento.tecla == 'espacio':
        self.elemento.pulsaEspacio()
        return True
      elif evento.tecla == 'abajo':
        if self.elemento.abajo():
          try:
            self.siguiente()
          except StopIteration:
            self.leerElementoEnfocado()
          else:
            self.leerElementoEnfocado()
        return True
      elif evento.tecla == 'arriba':
        if self.elemento.arriba():
          try:
            self.anterior()
          except StopIteration:
            self.leerElementoEnfocado()
          else:
            self.leerElementoEnfocado()
        return True
      elif evento.tecla == 'derecha':
        self.elemento.derecha()
        return True
      elif evento.tecla == 'izquierda':
        self.elemento.izquierda()
        return True
      else:
        return super().alPulsarTecla(evento)
    except Warning as error:
      self.manejarAdvertencias(*error.args)
  
  def manejarAdvertencias(self, tipo, *args):
    pass
  
  def alHabilitar(self):
    self._index=0
    self.elemento.focoConTab()
    if self.leerAlHabilitar:
      self.leerElementoEnfocado(self.interrumpirLecturaAlHabilitar)
  
  def limpiar(self):
    if self.estaHabilitado:
      self.deshabilitar()
    self.eliminarAnexados()
  
  def borrar(self, elemento):
    self.desanexar(elemento)
    elemento.eliminar()
  
  def teclaRapida(self, tecla, funcion, *args, **kwargs):
    self._accessKey[tecla] = self.iku.llamadaAFuncion(funcion, *args, **kwargs)
  
  # métodos constructores de elementos de la interface de usuario:
  def boton(self, texto, *args, **kwargs):
    elemento = self.iku.actores.UiBoton(texto, *args, **kwargs)
    self.anexar(elemento)
    return elemento
  
  def ingresaTexto(self, texto, *args, **kwargs):
    elemento = self.iku.actores.UiIngresaTexto(texto, *args, **kwargs)
    return self.anexar(elemento)
  
  def lista(self, texto, respuesta=None, *args, **kwargs):
    """ se puede pasar como segundo parámetro una lista de opciones o una función de respuesta. """
    elemento = self.iku.actores.UiLista(texto, respuesta, *args, **kwargs)
    self.anexar(elemento)
    return elemento
  
  def selector(self, texto, *args, **kwargs):
    elemento = self.iku.actores.UiSelector(texto, *args, **kwargs)
    self.anexar(elemento)
    return elemento
  
  def texto(self, texto, *args, **kwargs):
    elemento = self.iku.actores.UiTexto(texto, *args, **kwargs)
    self.anexar(elemento)
    return elemento
  