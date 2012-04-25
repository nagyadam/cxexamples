#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module 6.2
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Nagy Adam PRRICI'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
import attack62
import igraph
import cxnet

smallern = attack62.Network.Erdos_Renyi(20,0.2)
smallern.attack()

smallban = attack62.Network.Barabasi(20,4)
smallban.attack()

pylab.title("Celzott tamadas modellezese kis halozatokon")
pylab.legend(('Erdos-Renyi', 'Barabasi-Albert'), loc='upper left')


pylab.figure()

largerern = attack62.Network.Erdos_Renyi(100,0.2)
largerern.attack()

largeban = attack62.Network.Barabasi(100,4)
largeban.attack()

pylab.title("Celzott tamadas modellezese nagy halozatokon")
pylab.legend(('Erdos-Renyi', 'Barabasi-Albert'), loc='upper left')

