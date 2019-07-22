#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# 2019 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

class TTS(object):
  """Controlador del habla."""
  def __init__(self, engine):
    self.engine = engine
    self.historial = True
    self.limite = 3000
    self.eliminar = 1500
    self.msg = []
    self.index = 0
  
  def hablar(self, texto, interrumpir, registrar):
    self.engine.speak(texto, interrumpir)
    if registrar:
      self.msg.append(texto)
      self.index+=1
      if self.index >= self.limite:
        # eliminamos mensajes, se lleno el buffer.
        self.msg = self.msg[self.eliminar:]
  
  def texto(self, indice):
    return self.msg[indice]

def iniciar(tipo=None):
  """ si no se pasa ningun tipo de engine se toma como determinado el accesible_output2. """
  if tipo is None:
    import accessible_output2.outputs.auto
    engine = accessible_output2.outputs.auto.Auto()
  elif tipo == 'tolk':
    from .complementos  import tolk
    tolk.load()
    engine = tolk
  else:
    raise ValueError("'{tipo}' no es un motor válido para el habla.".format(tipo=tipo))
  
  return TTS(engine)
