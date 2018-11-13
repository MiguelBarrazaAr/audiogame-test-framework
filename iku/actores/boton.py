#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from iku.actores.actor import Actor

class Boton(Actor):
    def __init__(self,accion):
        """Un boton es un actor que al ser clickeado ejecuta una funcion.
        """
            Actor.__init__(self, imagen="imagenes/boton-estatico.png")
            self.iku.eventos.clickMouse.conectar(self.alClickiquearMouse)
            self.iku.eventos.mueveMouse.conectar(self.alEstarSobreElBoton)
            self.iku.eventos.finalizaClickMouse.conectar(self.alSoltarClick)
            self.accionAEjecutar = accion


    def alSoltarClick(self, evento):
        if(self.figura.collidepoint(evento["posicion"])):
            self.imagen = "imagenes/boton-sobre.png"


    def alClickiquearMouse(self, evento):
        if(self.figura.collidepoint(evento["posicion"])):
            self.imagen = "imagenes/boton-precionado.png"
            self.accionAEjecutar()

    def alEstarSobreElBoton(self,evento):
        if(self.figura.collidepoint(evento["posicion"])):
            self.imagen = "imagenes/boton-sobre.png"
        else:
            self.imagen = "imagenes/boton-estatico.png"