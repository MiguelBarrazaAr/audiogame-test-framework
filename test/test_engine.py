# -*- encoding: utf-8 -*-
import unittest
import iku

class TestEngine(unittest.TestCase):
  """
  Validamos la inicialización del engine
  """
  iku = iku.iniciar(modoTest=True)
  
  def test_AlIniciarTienePorDefaultUnAnchoDe640YUnAltoDe480(self):
    self.assertEquals(self.iku.dimension, (640, 480), "Iku inicia con una pantalla redimensionada en 640x480.")
  
  def test_ikuGuardaUnaReferenciaAlCentroDeLaPantalla(self):
    ancho, alto = self.iku.dimension
    self.assertEquals(self.iku.centro, (ancho/2, alto/2))
  
  def test_ikuIniciaConUnaVelocidadDeFramesPorSegundoDe25(self):
    self.assertEquals(self.iku.fps, 25)
