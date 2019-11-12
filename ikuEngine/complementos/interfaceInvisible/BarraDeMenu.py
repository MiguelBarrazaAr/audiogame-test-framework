#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2019 - Miguel Barraza

import ikuEngine

class Menu():
  def __init__(self, nombre):
    self.nombre = nombre
    self.items = []
  
  @property
  def total(self):
    return len(self.items)
  
  def agregar(self, nombre, respuesta):
    self.items.append(Item(nombre, respuesta))
  
  def get(self, id):
    return self.items[id]


class Item():
  def __init__(self, nombre, respuesta):
    self.nombre = nombre
    self.respuesta = respuesta
  
  def __str__(self):
    return self.nombre


class Modo():
  def __init__(self, ctrl):
    self.ctrl = ctrl
  def abajo(self):
    pass
  def arriba(self):
    pass
  def derecha(self):
    pass
  def izquierda(self):
    pass
  def enter(self):
    pass
  def escape(self):
    return False

class ModoBarra(Modo):
  def derecha(self):
    self.ctrl.siguiente()
    self.ctrl.leerMenu()
  def izquierda(self):
    self.ctrl.anterior()
    self.ctrl.leerMenu()
  def enter(self):
    self.ctrl.seleccionarMenu()
  def abajo(self):
    self.ctrl.seleccionarMenu()
  def arriba(self):
    self.ctrl.seleccionarMenu(True)
  def escape(self):
    self.ctrl.cerrarMenu()
    return True

class NavegarMenu(Modo):
  def __init__(self, ctrl):
    self.ctrl = ctrl
    self.menu = ctrl.menu
    self.index=0
    self.total = self.menu.total
    self.leer = ctrl.iku.leer
  
  def leerItem(self, interrumpir=True):
    self.leer(self.menu.get(self.index), interrumpir)
  
  def ultimo(self):
    self.index = self.total-1
  
  def enter(self):
    self.ctrl.deshabilitar()
    self.menu.opcion = self.menu.get(self.index)
    self.menu.opcion.respuesta()
  
  def derecha(self):
    self.ctrl.siguiente()
    self.ctrl.seleccionarMenu()
  
  def izquierda(self):
    self.ctrl.anterior()
    self.ctrl.seleccionarMenu()
  
  def abajo(self):
    if self.total != 0:
      self.index = (self.index+1) % self.total
      self.leerItem()
  
  def arriba(self):
    if self.total != 0:
      self.index = (self.index+self.total-1)%self.total
      self.leerItem()
  
  def escape(self):
    self.ctrl.modo = ModoBarra(self.ctrl)
    self.ctrl.leerBarra()
    return True



class BarraDeMenu(ikuEngine.actores.Elemento):
  """Representa a una barra de menú invisible de opciones navegable con flechas.
  """
  def __init__(self):
    ikuEngine.actores.ActorInvisible.__init__(self)
    self.menus = []
    self.total = 0
    self.index = 0
    self.modo = ModoBarra(self)
    self.menu = None # el menú seleccionado.
    self.cuandoDeshabilita = lambda: None
  
  def alHabilitar(self):
    """inicia el menú.
    este metodo puede ser llamado para reiniciar el menú y volverlo a presentar."""
    self.index = 0
    self.leerBarra()
    self.iku.escena.pulsaEscape.conectar(self.alPulsarEscape)
    self._acciones.emitir(accion="iniciar",
      actor=self,
      indice=self.index)
  
  def alDeshabilitar(self):
    self.iku.escena.pulsaEscape.desconectar(self.alPulsarEscape)
    self.cuandoDeshabilita()
  
  def alPulsarEscape(self, evento):
    return self.modo.escape()
  
  def nuevoMenu(self, nombre):
    """incorpora un menu a la barra."""
    menu = Menu(nombre)
    self.menus.append(menu)
    self.total+=1
    return menu
  
  def leerBarra(self):
    self.iku.leer('Barra de menú:')
    self.leerMenu(False)
  
  def alPulsarTecla(self, evento):
    if evento.tecla == "arriba":
      self.modo.arriba()
      return True
    elif evento.tecla == "abajo":
      self.modo.abajo()
      return True
    elif evento.tecla == "derecha":
      self.modo.derecha()
      return True
    elif evento.tecla == "izquierda":
      self.modo.izquierda()
      return True
    elif evento.tecla == "enter":
      self.modo.enter()
      return True
  
  def leerMenu(self, interrumpir=True):
    self.iku.leer(self.menus[self.index].nombre, interrumpir)
  
  def eliminar(self):
    self.deshabilitar()
    super().eliminar()
  
  def seleccionarMenu(self, ultimoItem=False):
    self.menu = self.menus[self.index]
    self.iku.leer("barra de menú: {}".format(self.menu.nombre))
    self.modo = NavegarMenu(self)
    if ultimoItem:
      self.modo.ultimo()
    try:
      self.modo.leerItem(False)
    except IndexError:
      self.iku.leer("No hay elementos.", False)
  
  def cerrarMenu(self):
    self.deshabilitar()
    self.iku.leer("saliendo del menú.")
  
  def siguiente(self):
    self.index = (self.index+1) % self.total
  
  def anterior(self):
    self.index = (self.index+self.total-1) % self.total
