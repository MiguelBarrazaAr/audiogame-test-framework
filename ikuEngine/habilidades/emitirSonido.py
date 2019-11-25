#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

import types
import ikuEngine

def emitirSonido(actor, ruta):
  iku = ikuEngine.instancia()
  actor._es_sound = iku.sonido(ruta)
  actor._es_sound.posicion = actor.posicion
  actor._es_continuo = True
  
  f1 = getattr(actor, "alHabilitar")
  def alHabilitar(self):
    self._es_sound.reproducir(self._es_continuo)
    f1()
    
  f2 = getattr(actor, "alDeshabilitar")
  def alDeshabilitar(self):
    self._es_sound.detener()
    f2()
  
  f3 = getattr(actor, "alCambiarPosicion")
  def alCambiarPosicion(self):
    self._es_sound.posicion = self.posicion
    f3()
  
  setattr(actor, "alHabilitar", types.MethodType(alHabilitar, actor))
  setattr(actor, "alDeshabilitar", types.MethodType(alDeshabilitar, actor))
  setattr(actor, "alCambiarPosicion", types.MethodType(alCambiarPosicion, actor))

