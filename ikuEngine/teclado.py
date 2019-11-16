#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku_engine: Motor para Audio Juegos en python (3.7)
#
# Copyright 2019 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
from enum import Enum
import pygame

class KEY(Enum):
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
    num7 = pygame.K_KP6
    num8 = pygame.K_KP8
    num9 = pygame.K_KP9
    limpiar = pygame.K_CLEAR
    pausa = pygame.K_PAUSE
    escape = pygame.K_ESCAPE
    

class Tecla():
  def __init__(self, tecla):
    self.tecla = tecla
  
  def __eq__(self, obj):
    return self.tecla.name == obj or self.tecla.value == obj
  
  def __hash__(self):
    return self.tecla
  
  @property
  def name(self):
    return self.tecla.name
  
  @property
  def value(self):
    return self.tecla.value

class Teclado():
  def tecla(self, cod):
    return Tecla(KEY(cod))
  
  def shiftPulsado(self):
    """retorna True si se pulso alguno de los 2 shifts"""
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LSHIFT or mod_bitmask == pygame.KMOD_RSHIFT
  
  def shiftIzqPulsado(self):
    """retorna si esta pulsado el shift izquierdo. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LSHIFT
  
  def shiftDerPulsado(self):
    """retorna si esta pulsado el shift derecho. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_RSHIFT
  
  def controlPulsado(self):
    """retorna si se pulso algún control. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LCTRL or mod_bitmask == pygame.KMOD_RCTRL
  
  def controlIzqPulsado(self):
    """retorna si esta pulsado el control izquierdo. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LCTRL
  
  def controlDerPulsado(self):
    """retorna si esta pulsado el control derecho. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_RCTRL
  
  def altPulsado(self):
    """retorna si se pulso el alt. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LALT
  
  def altGrPulsado(self):
    """retorna si se pulso el alt grafico o e(alt derecho). """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_RALT
  
  def mayusPulsado(self):
    """retorna si se pulso el blockeo de mayusculas. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_CAPS
  
  def numPulsado(self):
    """retorna si se pulso el blockeo numerico. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_NUM
  
  def tabPulsado(self):
    """retorna si se pulso el tab. """
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.K_TAB
