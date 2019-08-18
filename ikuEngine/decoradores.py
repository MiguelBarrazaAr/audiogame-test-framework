#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# iku engine: Motor para videojuegos en python (3.7)
#
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
# Copyright 2018 - 2019: Miguel Barraza

class SingletonDecorator():
  def __init__(self, klass):
    self.klass = klass
    self.instance = None
  
  def __call__(self, *args, **kwds):
    if self.instance == None:
      self.instance = self.klass(*args, **kwds)
    return self.instance
