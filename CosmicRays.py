#! /usr/bin/env python3

import numpy as np
import time
from Random import Random

class CosmicRays():

    #Initialize the class
    def __init__(self,seed = 5555,events = 100, start = 0, end = 24, mode =0):
        self.start_time = start # Will be the hour of the day
        self.end_time = end
        self.seed = seed
        self.rand = Random(self.seed)
        self.events = events
        self.mode =  mode

    #If you choose to pick a random time of the day
    def Extract_time(self, N = 1):
        event_time = Extract_time(1)
        while event_time <self.start_time and event_time > self.end_time:
            event_time = Extract_time(1)
        return event_time

    

