# -*- encoding: utf-8 -*-
import unittest
import iku

class TestEngine(unittest.TestCase):
  """
  Validamos el funcionamiento del ActorInvisible
  """
  iku = iku.iniciar(modoTest=True)
  
  def test_alCrearElActorInvisibleSePuedeIndicarEl_x_DondeEstaraPosicionado(self):
    valor_de_x = 5
    actor=self.iku.actores.ActorInvisible(x=valor_de_x)
    self.assertEquals(actor.x, valor_de_x)
  
  def test_alCrearElActorInvisibleSePuedeIndicarEl_y_DondeEstaraPosicionado(self):
    valor_de_y = 10
    actor=self.iku.actores.ActorInvisible(y=valor_de_y)
    self.assertEquals(actor.y, valor_de_y)
  
  def test_unActorPuedeMoversePorElEje_x_sinAlterarElValorDe_y(self):
    valor_de_x = 5
    valor_de_y = 3
    pasos=10
    actor=self.iku.actores.ActorInvisible(x=valor_de_x, y=valor_de_y)
    actor.mover(x=pasos)
    self.assertEquals(actor.x, valor_de_x+pasos)
    self.assertEquals(actor.y, valor_de_y)
  
  def test_unActorPuedeMoversePorElEje_y_sinAlterarElValorDe_x(self):
    valor_de_x = 5
    valor_de_y = 3
    pasos=10
    actor=self.iku.actores.ActorInvisible(x=valor_de_x, y=valor_de_y)
    actor.mover(y=pasos)
    self.assertEquals(actor.x, valor_de_x)
    self.assertEquals(actor.y, valor_de_y+pasos)
  
  
