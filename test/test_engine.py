# -*- encoding: utf-8 -*-
import unittest
import iku

class TestEngine(unittest.TestCase):
  """
  Validamos la inicialización del engine
  """
  def setUp(self):
    self.iku = iku.iniciar(modoTest=True)
  
  def test_AlIniciarConLosParametrosDefaultElAnchoEsDe640YElAltoEsDe480(self):
    self.assertEquals(self.iku.dimension, (640, 480), "Iku inicia con una pantalla redimensionada en 640x480.")
