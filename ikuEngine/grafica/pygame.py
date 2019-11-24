#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python 3
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

from enum import Enum
import time
import pygame
#from pygame.locals import *


class PygameEngine():
  def __init__(self, iku, titulo, ancho, alto):
    self.iku = iku
    # iniciamos el motor pygame:
    pygame.init()
    self.reloj = pygame.time.Clock()
    self._winLoop = True
    
    # iniciamos el motor gráfico:
    pygame.display.set_caption(titulo)
    self.ventana = pygame.display.set_mode(iku.configuracion.dimension)
    pygame.display.flip()
    # cargamos una fuente default:
    self.fuente = pygame.font.Font("freesansbold.ttf", 30)
  
  def codigoDeTeclas(self):
    return Teclas
  
  def ejecutar(self):
    while self._winLoop:
      self.iku._timestamp = time.time()
      # monitorizamos eventos:
      for event in pygame.event.get():
        self._procesarEvento(event)
      
      # controlamos el tiempo de refresco.
      tick=self.reloj.tick(self.iku.fps)
      self.iku.teclado.actualizar(pygame.key.get_pressed())
      self.iku.tareas.actualizar(tick)
      self.iku.escenas.escenaActual.actualizar(tick)
      self.iku.escenas.escenaActual.dibujarEn(self.ventana)
      pygame.display.flip()
      tick=self.reloj.tick(self.iku.fps)
  
  def _procesarEvento(self, event):
    if event.type == pygame.QUIT:
      self.iku.eventos.usuario.emitir(accion="salir")
      self.iku.finalizar()
    # pulsa una tecla:
    if event.type == pygame.KEYDOWN:
      # si pulsa escape, emitimos pulsaEscape
      if event.key == pygame.K_ESCAPE:
        self.iku.eventos.pulsaEscape.emitir(tecla=event.key, tipo=event.type)
      if event.key == pygame.K_F4 and self.altPulsado():
        self.iku.eventos.usuario.emitir(accion="salir")
        self.iku.finalizar()
      else:
        # emitimos el pulsa tecla:
        self.iku.eventos.pulsaTecla.emitir(tecla=self.iku.teclado.tecla(event.key, pygame.key.get_mods()), representacion=event.unicode)
    # suelta una tecla:
    if event.type == pygame.KEYUP:
      self.iku.eventos.sueltaTecla.emitir(tecla=self.iku.teclado.tecla(event.key, pygame.key.get_mods()))
    # si algún botón del mouse es presionado
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.iku.eventos.clickMouse.emitir(boton=event.button, posicion=event.pos)
    # si algún botón del mouse es soltado
    if event.type == pygame.MOUSEBUTTONUP:
      self.iku.eventos.finalizaClickMouse.emitir(boton=event.button, posicion=event.pos)
    # si el mouse es movido
    if event.type == pygame.MOUSEMOTION:
      self.iku.eventos.mueveMouse.emitir(botones=event.buttons, posicion=event.pos, movimiento=event.rel)
  
  def altPulsado(self):
    """retorna si se pulso el alt. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LALT
  
  def definirTitulo(self, titulo):
    pygame.display.set_caption(titulo)
  
  def finalizar(self):
    self._winLoop = False
    pygame.quit()
  
  def escalarSuperficie(self,superficie, ancho, alto):
    return pygame.transform.scale(superficie, (int(ancho), int(alto)))
  
  def cargarImagen(self, rutaImagen):
    """Carga una imagen y retorna una superficie."""
    return pygame.image.load(rutaImagen)

class Teclas(Enum):
    """constantes de teclas"""
    abajo = pygame.K_DOWN
    arriba = pygame.K_UP
    derecha= pygame.K_RIGHT
    izquierda= pygame.K_LEFT
    alt = pygame.K_LALT
    altGr = pygame.K_RALT
    aplicacion = pygame.K_MENU
    controlDerecha = pygame.K_RCTRL
    controlIzquierda = pygame.K_LCTRL
    insert = pygame.K_INSERT
    inicio = pygame.K_HOME
    fin = pygame.K_END
    mayus = pygame.K_CAPSLOCK
    scrolLock = pygame.K_SCROLLOCK
    metaDerecha = pygame.K_RMETA
    metaIzquierda = pygame.K_LMETA
    pagRetroceder = pygame.K_PAGEUP
    pagAvanzar = pygame.K_PAGEDOWN
    shiftDerecha = pygame.K_RSHIFT
    shiftIzquierda = pygame.K_LSHIFT
    f1 = pygame.K_F1
    f2 = pygame.K_F2
    f3 = pygame.K_F3
    f4 = pygame.K_F4
    f5 = pygame.K_F5
    f6 = pygame.K_F6
    f7 = pygame.K_F7
    f8 = pygame.K_F8
    f9 = pygame.K_F9
    f10 = pygame.K_F10
    f11 = pygame.K_F11
    f12 = pygame.K_F12
    f13 = pygame.K_F13
    f14 = pygame.K_F14
    f15 = pygame.K_F15
    acento = pygame.K_LEFTBRACKET
    admiracion = pygame.K_EQUALS
    cerrarAdmiracion = pygame.K_EXCLAIM
    cerrarInterrogacion = pygame.K_QUESTION
    arroba = pygame.K_AT
    guionBajo = pygame.K_UNDERSCORE
    comillas = pygame.K_QUOTEDBL
    numero = pygame.K_HASH
    dolar = pygame.K_DOLLAR
    ampersand = pygame.K_AMPERSAND
    abrirParentesis = pygame.K_LEFTPAREN
    cerrarParentesis = pygame.K_RIGHTPAREN
    asterisco = pygame.K_ASTERISK
    mas = pygame.K_PLUS
    apostrofe = pygame.K_MINUS
    coma = pygame.K_COMMA
    cedilla = pygame.K_BACKSLASH
    borrar = pygame.K_BACKSPACE
    enter = pygame.K_RETURN
    espacio = pygame.K_SPACE
    guion = pygame.K_SLASH
    suma = pygame.K_RIGHTBRACKET
    caret = pygame.K_CARET
    suprimir = pygame.K_DELETE
    suprDerecha = pygame.K_RSUPER
    suprIzquierda = pygame.K_LSUPER
    punto = pygame.K_PERIOD
    tab = pygame.K_TAB
    tilde = pygame.K_QUOTE
    altGR2 = pygame.K_MODE
    help = pygame.K_HELP
    printScreen = pygame.K_PRINT
    sysReq = pygame.K_SYSREQ
    teclaBreak = pygame.K_BREAK
    power = pygame.K_POWER
    euro = pygame.K_EURO
    a = pygame.K_a
    b = pygame.K_b
    c = pygame.K_c
    d = pygame.K_d
    e = pygame.K_e
    f = pygame.K_f
    g = pygame.K_g
    h = pygame.K_h
    i = pygame.K_i
    j = pygame.K_j
    k = pygame.K_k
    l= pygame.K_l
    m = pygame.K_m
    n = pygame.K_n
    nTilde = pygame.K_SEMICOLON
    menorQue = pygame.K_LESS
    mayorQue = pygame.K_GREATER
    o = pygame.K_o
    p = pygame.K_p
    q = pygame.K_q
    r = pygame.K_r
    s = pygame.K_s
    t = pygame.K_t
    u = pygame.K_u
    v = pygame.K_v
    w = pygame.K_w
    x = pygame.K_x
    y = pygame.K_y
    z = pygame.K_z
    ordinal = pygame.K_BACKQUOTE
    alfa1 = pygame.K_1
    alfa2 = pygame.K_2
    alfa3 = pygame.K_3
    alfa4 = pygame.K_4
    alfa5 = pygame.K_5
    alfa6 = pygame.K_6
    alfa7 = pygame.K_7
    alfa8 = pygame.K_8
    alfa9 = pygame.K_9
    alfa0 = pygame.K_0
    dosPuntos = pygame.K_COLON
    igual = pygame.K_KP_EQUALS
    numLock = pygame.K_NUMLOCK
    numDivide = pygame.K_KP_DIVIDE
    numMultiplica = pygame.K_KP_MULTIPLY
    numMenos = pygame.K_KP_MINUS
    numSuma = pygame.K_KP_PLUS
    numEnter = pygame.K_KP_ENTER
    numPunto = pygame.K_KP_PERIOD
    num0 = pygame.K_KP0
    num1 = pygame.K_KP1
    num2 = pygame.K_KP2
    num3 = pygame.K_KP3
    num4 = pygame.K_KP4
    num5 = pygame.K_KP5
    num6 = pygame.K_KP6
    num7 = pygame.K_KP7
    num8 = pygame.K_KP8
    num9 = pygame.K_KP9
    limpiar = pygame.K_CLEAR
    pausa = pygame.K_PAUSE
    escape = pygame.K_ESCAPE
