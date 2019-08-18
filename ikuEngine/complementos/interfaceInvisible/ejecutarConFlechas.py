#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - Miguel Barraza

import ikuEngine

class EjecutarConFlechas(ikuEngine.actores.Elemento):
  """Controla el movimiento de las flechas y ejecuta su acción."""
  def __init__(self, actor, *k, **kv):
    """Se debe pasar un actor que acepte los siguientes métodos: arriba, abajo, izquierda, derecha."""
    self.iku = iku.instancia()
    self._actor=actor
    actor.anexar(self)
    self.iku.eventos.pulsaTecla.conectar(self._alPulsarTecla)
  
  def _alPulsarTecla(self, evento):
    if evento.tecla == self.iku.tecla.derecha:
      self._actor.derecha()
    elif evento.tecla == self.iku.tecla.izquierda:
      self._actor.izquierda()
    elif evento.tecla == self.iku.tecla.arriba:
      self._actor.arriba()
    elif evento.tecla == self.iku.tecla.abajo:
      self._actor.abajo()
