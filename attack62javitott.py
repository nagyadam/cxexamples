#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module 6.2_attack
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Nagy Adam PRRICI'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
import pylab
import igraph
import cxnet

class Network(igraph.Graph):
    def attack(self):
        li = []
        comp = []
        cc = self.components()
 #       cn = len(cc.sizes())
        giant = max(cc.sizes())
        i = 0
 #       while cn != 0:
        while giant > 1:
            deg = self.degree()
            d = deg.index(max(deg))
            self.delete_vertices(d)
            cc = self.components()
 #           cn = len(cc.sizes())
            giant = max(cc.sizes())
 #           comp.append(cn)
            comp.append(giant/self.vcount())
            i = i+1
            li.append(i)
        pylab.plot(li, comp)
        pylab.xlabel("tamadasok szama")
        pylab.ylabel("legnagyobb komponens")

