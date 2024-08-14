import pygame
import sys

from Particle import Particle

class Barrier(Particle):

    def __init__(self, x,y, size=10):
        
        super().__init__(x,y, size)
                
        self.type = "Barrier"
        self.state = "solid"

        self.color = (255) # white
    
    
    
     