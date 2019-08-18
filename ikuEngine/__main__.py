#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright    2019: Miguel Barraza

"""
iku-engine puede ser ejecutado como un script.

ejemplo: python -m iku --version
"""
from . import configuracion
import argparse  

if __name__ == "__main__":
  parser = argparse.ArgumentParser() 
  parser.add_argument("-v", "--version", help="Mostrar version de iku-engine", action="store_true") 
  args = parser.parse_args() 
  
  # Aquí procesamos lo que se tiene que hacer con cada argumento 
  if args.version:
    print("iku engine version {}".format(configuracion.VERSION))
  