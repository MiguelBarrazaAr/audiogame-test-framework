#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# MajPy: Motor para Audio Juegos en python (3.7)
#
# Copyright 2018 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
import pygame

class Tecla(object):
  """constantes de teclas"""
  def __init__(self):
    self.abajo = 274
    self.arriba= 273
    self.derecha= 275
    self.izquierda= 276
    self.alt = 308
    selfAltGr = 307
    self.aplicacion = 319
    self.controlDerecha = 305
    self.controlIzquierda = 306
    self.inicio = 278
    self.fin = 279
    self.mayus = 301
    self.pagRetroceder = 280
    self.pagAvanzar = 281
    self.shiftDerecha = 303
    self.shiftIzquierda = 304
    self.f1 = 282
    self.f2 = 283
    self.f3 = 284
    self.f4 = 285
    self.f5 = 286
    self.f6 = 287
    self.f7 = 288
    self.f8 = 289
    self.f9 = 290
    self.f10 = 291
    self.f11 = 292
    self.f12 = 293
    self.acento = 91
    self.admiracion = 61
    self.apostrofe = 45
    self.coma = 44
    self.cedilla = 92
    self.delete = 8
    self.enter = 13
    self.espacio= 32
    self.guion = 47
    self.suma = 93
    self.suprimir = 127
    self.punto = 46
    self.tab = 9
    self.tilde = 39
    self.a = 97
    self.b = 98
    self.c = 99
    self.d = 100
    self.e = 101
    self.f = 102
    self.g = 103
    self.h = 104
    self.i = 105
    self.j = 106
    self.k = 107
    self.l= 108
    self.m = 109
    self.n = 110
    self.nTilde = 59
    self.o = 111
    self.p = 112
    self.q = 113
    self.r = 114
    self.s = 115
    self.t = 116
    self.u = 117
    self.v = 118
    self.w = 119
    self.x = 120
    self.y = 121
    self.z = 122
    self.ordinal = 96
    self.alfa1 = 49
    self.alfa2 = 50
    self.alfa3 = 51
    self.alfa4 = 52
    self.alfa5 = 53
    self.alfa6 = 54
    self.alfa7 = 55
    self.alfa8 = 56
    self.alfa9 = 57
    self.alfa0 = 48
    self.numDivide = 267
    self.numMultiplica = 268
    self.numMenos = 269
    self.numSuma = 270
    self.numEnter = 271
    self.numPunto = 266
    self.num0 = 256
    self.num1 = 257
    self.num2 = 258
    self.num3 = 259
    self.num4 = 260
    self.num5 = 261
    self.num6 = 262
    self.num7 = 263
    self.num8 = 264
    self.num9 = 265
  
  def shiftPulsado(self):
    """retorna si se pulso alguno de los 2 shifts"""
    mod_bitmask = pygame.key.get_mods()
    return mod_bitmask == pygame.KMOD_LSHIFT or mod_bitmask == pygame.KMOD_RSHIFT
