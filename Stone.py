import pygame
import sys

from Particle import Particle

class Stone(Particle):

    def __init__(self, x,y, size=10):
        
        super().__init__(x,y, size)
                
        self.type = "Stone"
        self.state = "solid"

        self.color = (110,110,110) # gray
    
    
    
    def update(self, grid):
        neighbours = self.get_neighbours(grid)


        

        # falls If there isnt a neighbour underneath of the particle...
        if neighbours[(0, 1)] == 0 or neighbours[(0, 1)].state=="liquid":
            self.rect.y += grid.cell_size
            
        
            
        grid.update_spatial_hash(self)
            
        
        
        
        
    
    
     