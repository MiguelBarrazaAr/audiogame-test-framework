# -*- encoding: utf-8 -*-
import unittest
import iku

class TestEngine(unittest.TestCase):
  """
  Validamos la inicialización del engine
  """
  def setUp(self):
    self.iku = iku.iniciar(modoTest=True, ancho=1280, alto=960)
  
  def test_alIniciarSeDeterminoUnAnchoDe1280YUnAltoDe960(self):
    self.assertEquals(self.iku.dimension, (1280, 960), "Iku inicia con una pantalla redimensionada en los parametros indicados 1280x960.")
  
  def test_ikuGuardaUnaReferenciaAlCentroDeLaPantalla(self):
    ancho, alto = self.iku.dimension
    self.assertEquals(self.iku.centro, (ancho/2, alto/2))
  
  def test_ikuIniciaConUnaVelocidadDeFramesPorSegundoDe25(self):
    self.assertEquals(self.iku.fps, 25)
