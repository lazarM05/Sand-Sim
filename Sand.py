import pygame
import sys

from Particle import Particle

class Sand(Particle):

    def __init__(self, x,y, size=10):
        
        super().__init__(x,y, size)
                
        self.type = "Sand"
        self.state = "solid"

        self.color = (255,140,0) # sand
    
    
    
    def update(self, grid):
        neighbours = self.get_neighbours(grid)

        

        # falls If there isnt a neighbour underneath of the particle...
        if neighbours[(0, 1)] == 0:
            self.rect.y += grid.cell_size

        else:
            # if bellow particle is solid...
            if neighbours[(0, 1)].state=="solid":


                #print("cp 1")
                #... check left
                # Check if sand can fall left

                if all(neighbours[n] == 0 or (neighbours[n] and neighbours[n].state != "solid") for n in [(-1, 0), (-1, 1)]):
                    self.rect.x -= grid.cell_size
                    self.rect.y += grid.cell_size

                elif all(neighbours[n] == 0 or (neighbours[n] and neighbours[n].state != "solid") for n in [(1, 0), (1, 1)]):
                    self.rect.x += grid.cell_size
                    self.rect.y += grid.cell_size
          
                ### if  inside a particle ###
                if len(neighbours[(0, 0)]) > 1 and any((n.state == "solid") and (n != self) for n in neighbours[(0, 0)]):
                    self.rect.y -= grid.cell_size
                


            # falls down if the on top of a liquid
            if neighbours[(0, 1)].state=="liquid":
                self.rect.y += grid.cell_size

            
        
            
            
        
            
        grid.update_spatial_hash(self)
            
        
        
        
        
    
    
     