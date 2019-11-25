#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

def mover(self, ev, func):
  if ev.tecla == self.tecla.izquierda:
    self.mover(x=-self._mf_paso)
    return True
  elif ev.tecla == self.tecla.derecha:
    self.mover(x=self._mf_paso)
    return True
  elif ev.tecla == self.tecla.arriba:
    self.mover(y=self._mf_paso)
    return True
  elif ev.tecla == self.tecla.abajo:
    self.mover(y=-self._mf_paso)
    return True
  else:
    func(ev)


def MoverConFlechas(actor, paso=1, mirada=0):
  actor._mf_paso=paso
  actor._mf_mirada=mirada
  func=getattr(actor, "alPulsarTecla")
  setattr(actor, "alPulsarTecla", lambda evento: mover(actor, evento, func))
