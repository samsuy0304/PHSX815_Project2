#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from Random import Random
from CosmicRays import CosmicRays

#################################
# Decay Class
#################################

class Decay():
    #Initialize Class
    def __init__(self, seed = 5555, events = 1000, p = [0.5,0.5], time_neg = 2.2, time_pos = 2.4):
        self.p = p
        self.seed = seed
        self.rand = Random(self.seed)
        self.events = events
        self.muon_n = p[0]*self.events
        self.muon_p = p[1]*self.events
        self.time_n = time_neg
        self.time_p = time_pos

    def Update_Distribution(self,PD):
        self.p = PD
        self.muon_n =PD[0]*self.events
        self.muon_p =PD[1]*self.events

    def Time(self):
        life_n = []
        life_p = []
        
        for i in range(self.muon_n):
            t1 = self.rand.Exponential(time_n)
            life_n.append(t1)

        for _ in range(self.muon_p):
            t2= self.rand.Exponential(time_p)
            life_p.append(t2)

        lifetimes = life_n + life_p

        return life_n, life_p, lifetimes

    def Plot(self
