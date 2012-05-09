#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module 6.2
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Nagy Adam PRRICI'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
import attack62javitott
import igraph
import cxnet
import pylab

N=100
smallern = attack62javitott.Network.Erdos_Renyi(N, 8/N)
smallern.attack()

smallban = attack62javitott.Network.Barabasi(N, 4)
smallban.attack()

pylab.title("Celzott tamadas modellezese kis halozatokon")
pylab.legend(('Erdos-Renyi', 'Barabasi-Albert'), loc='upper right')
#pylab.show()


pylab.figure()

N=1000
largerern = attack62javitott.Network.Erdos_Renyi(N, 8/N)
print(largerern.ecount())
largerern.attack()

largeban = attack62javitott.Network.Barabasi(N, 4)
print(largeban.ecount())
largeban.attack()

pylab.title("Celzott tamadas modellezese nagy halozatokon")
pylab.legend(('Erdos-Renyi', 'Barabasi-Albert'), loc='upper left')

