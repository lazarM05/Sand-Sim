import pygame
import sys

import random
from Particle import Particle



class Cloud(Particle):


    def __init__(self, x,y, size=10):
        
        super().__init__(x,y, size)
                
        self.type = "Cloud"
        self.state = "gas"

        self.color = (225,225,225) # white-ish
    
    
    
    def update(self, grid):
        neighbours = self.get_neighbours(grid)
        
        self.pressure = 1
        

        if neighbours[(0,-1)]==0:
            self.rect.y -= grid.cell_size
        
        valid_neighbors = [n for n in [(-1, 0), (1, 0)] if neighbours[n] == 0 or neighbours[n].state == "liquid"]
        # if list not empty
        if valid_neighbors:
            # Get a random item from the list
            random_neighbor = random.choice(valid_neighbors)
            self.rect.x += random_neighbor[0]*grid.cell_size


                
                    
        grid.update_spatial_hash(self)
            
        
        
        
        
    
    
     
