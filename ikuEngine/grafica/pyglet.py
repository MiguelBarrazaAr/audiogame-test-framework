#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

from enum import Enum
import time
import pyglet
pyglet.options['shadow_window']=False
from pyglet.window import key

class PygletEngine():
  def __init__(self, iku, titulo, ancho, alto):
    self.iku = iku
    # iniciamos el motor pyglet:
    self.ventana= pyglet.window.Window(1280, 720, "mi juego", resizable=True, style=pyglet.window.Window.WINDOW_STYLE_DIALOG)
    self.ventana.set_minimum_size(400,300)
    self.ventana.on_key_press = self._on_key_press
    self.ventana.on_key_release = self._on_key_release
    self.ventana.on_close = self._on_close
  
  def codigoDeTeclas(self):
    return Teclas
  
  def ejecutar(self):
    pyglet.clock.schedule_interval(self._actualizar, 1 / self.iku.fps)
    pyglet.app.run()
  
  def _on_key_press(self, symbol, modifiers):
    if symbol == key.ESCAPE:
      self.iku.eventos.pulsaEscape.emitir(tecla=self.iku.teclado.tecla(symbol), tipo="pulsaEscape")
    else:
      self.iku.eventos.pulsaTecla.emitir(tecla=self.iku.teclado.tecla(symbol), representacion=self.symbolToChar(symbol))
  
  def _on_key_release(self, symbol, modifiers):
    self.iku.eventos.sueltaTecla.emitir(tecla=self.iku.teclado.tecla(symbol), representacion=self.symbolToChar(symbol))
  
  def _on_close(self):
    self.iku.eventos.usuario.emitir(accion="salir")
    self.iku.finalizar()
  
  def symbolToChar(self, symbol):
    if symbol < 256 and symbol > 31:
      return chr(symbol)
    else:
      return ''
  
  def definirTitulo(self, titulo):
    pass  
  
  def finalizar(self):
    pyglet.app.exit()
  
  def _actualizar(self, tick):
    # metodo que se llama al actualizar cada tick del reloj:
    self.iku._timestamp = time.time()
    self.iku.teclado.actualizar(key.KeyStateHandler())
    self.iku.tareas.actualizar(tick)
    self.iku.escenas.escenaActual.actualizar(tick)
  
  def cargarImagen(self, ruta):
    pass


class Teclas(Enum):
    """constantes de teclas"""
    abajo = key.DOWN
    arriba = key.UP
    derecha= key.RIGHT
    izquierda= key.LEFT
    alt = key.LALT
    altGr = key.RALT
    aplicacion = key.MENU
    controlDerecha = key.RCTRL
    controlIzquierda = key.LCTRL
    insert = key.INSERT
    inicio = key.HOME
    fin = key.END
    mayus = 65509
    pagRetroceder = key.PAGEUP
    pagAvanzar = key.PAGEDOWN
    shiftDerecha = key.RSHIFT
    shiftIzquierda = key.LSHIFT
    f1 = key.F1
    f2 = key.F2
    f3 = key.F3
    f4 = key.F4
    f5 = key.F5
    f6 = key.F6
    f7 = key.F7
    f8 = key.F8
    f9 = key.F9
    f10 = key.F10
    f11 = key.F11
    f12 = key.F12
    f13 = key.F13
    f14 = key.F14
    f15 = key.F15
    acento = key.BRACKETLEFT
    admiracion = 949187772416
    cerrarAdmiracion = key.EXCLAMATION
    cerrarInterrogacion = key.QUESTION
    arroba = key.AT
    guionBajo = key.UNDERSCORE
    comillas = key.DOUBLEQUOTE
    numero = key.HASH
    dolar = key.DOLLAR
    ampersand = key.AMPERSAND
    abrirParentesis = key.PARENLEFT
    cerrarParentesis = key.PARENRIGHT
    asterisco = key.ASTERISK
    mas = key.PLUS
    apostrofe = 39
    coma = key.COMMA
    cedilla = 820338753536
    borrar = key.BACKSPACE
    enter = key.RETURN
    espacio = key.SPACE
    guion = 45
    suma = key.BRACKETRIGHT
    suprimir = key.DELETE
    punto = key.PERIOD
    tab = key.TAB
    tilde = 798863917056
    altGR2 = key.LALT
    help = key.HELP
    print = key.PRINT
    sysReq = key.SYSREQ
    teclaBreak = 188978561024
    a = key.A
    b = key.B
    c = key.C
    d = key.D
    e = key.E
    f = key.F
    g = key.G
    h = key.H
    i = key.I
    j = key.J
    k = key.K
    l= key.L
    m = key.M
    n = key.N
    nTilde = 824633720832
    menorQue = 60
    #mayorQue = key.GREATER
    o = key.O
    p = key.P
    q = key.Q
    r = key.R
    s = key.S
    t = key.T
    u = key.U
    v = key.V
    w = key.W
    x = key.X
    y = key.Y
    z = key.Z
    ordinal = 944892805120
    alfa1 = key._1
    alfa2 = key._2
    alfa3 = key._3
    alfa4 = key._4
    alfa5 = key._5
    alfa6 = key._6
    alfa7 = key._7
    alfa8 = key._8
    alfa9 = key._9
    alfa0 = key._0
    dosPuntos = key.COLON
    #igual = key.EQUAL
    numLock = key.NUMLOCK
    numDivide = key.NUM_DIVIDE
    numMultiplica = key.NUM_MULTIPLY
    numMenos = key.NUM_SUBTRACT
    numSuma = key.NUM_ADD
    numEnter = key.ENTER
    numPunto = 65454
    num0 = key.NUM_0
    num1 = key.NUM_1
    num2 = key.NUM_2
    num3 = key.NUM_3
    num4 = key.NUM_4
    num5 = key.NUM_5
    num6 = key.NUM_6
    num7 = key.NUM_7
    num8 = key.NUM_8
    num9 = key.NUM_9
    limpiar = key.CLEAR
    pausa = key.PAUSE
    escape = key.ESCAPE
