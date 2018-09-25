#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IkuEngine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

import sound_lib
from sound_lib import output
from sound_lib import stream

o=output.Output()

class Sonido(object):

    def __init__(self,nombre_de_archivo):
        self.load(nombre_de_archivo)

    def load(self,filename=""):
        self.handle =stream.FileStream(file=filename)

    def reproducir(self, continuo=False):
        self.handle.looping=continuo
        self.handle.play()

    def reproducir_esperando(self):
        self.handle.looping=False
        self.handle.play_blocking()

    def reproducirContinuo(self):
        self.handle.looping=True
        self.handle.play()

    def detener(self):
        if not self.handle is None:
            self.handle.stop()
            self.handle.set_position(0)

    @property
    def paneo(self):
        return self.handle.pan

    @paneo.setter
    def paneo(self, valor):
        self.handle.pan = valor

    @property
    def volumen(self):
        return self.handle.volume

    @volumen.setter
    def volumen(self, valor):
        self.handle.volume = valor

