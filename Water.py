import pygame
import sys
from Particle import Particle

import random

class Water(Particle):
    
    def __init__(self, x,y, size=10):
        super().__init__(x,y, size)
        self.color = (30,144,255) # water
        self.state = "liquid"
        self.type = "Water" 

        self.old_neighbours = None
        

    def update(self, grid):

        
        neighbours = self.get_neighbours(grid)


        # remove this  to fix the glitch  with  water not flowing after being deleted
        
        if self.old_cell_index == self.cell_index:
                if self.old_neighbours and all(
                    self.old_neighbours[key] == neighbours[key] for key in neighbours):
                    return
                else:
                    pass
                            #pass #FUCK you!!!!!
                    
                

    
        # falls If there isnt a neighbour underneath of the particle...
        if neighbours[(0,1)]==0:
            self.rect.y += grid.cell_size
            #print("Down") 
            
        # if there is particle bellow... 
        else:
            
            
            

            if any((neighbours[n]!=0) and (neighbours[n].type=="Lava") for n in [(-1,0),(1,0),(0,-1),(0,1)]):
                grid.delete_particle(self)
                
                
            ### if  inside a particle ###
            elif len(neighbours[(0, 0)])>1 and any(n.state in ["solid","liquid"]  and n!=self for n in neighbours[(0, 0)]):
                self.rect.y -= grid.cell_size

            
             
            # ... if particle is solid..
            elif neighbours[(0,1)].state=="solid":
                #print("cp 3") 

                # ..if left and downleft neighbours are air, move left
                if neighbours[(-1,0)] == 0 and (neighbours[(-1,1)] == 0 or neighbours[(-1,1)].type== "Water"):
                    self.rect.x -= grid.cell_size
                    #print("cp 4")

                # .. if right and downright neighbours are air, move right
                elif neighbours[(1,0)] == 0 and (neighbours[(1,1)] == 0 or neighbours[(1,1)].type== "Water"):
                    self.rect.x += grid.cell_size
                    #print("cp 5")


            # ... if particle is liquid..
            elif  neighbours[(0,1)].state == "liquid":
                #print("cp 6")

                if neighbours[(0,1)].type == "Water":
                    #print("cp 7")
                    # water collision
                    
                    
                    self.check_water_collision(grid, neighbours)
                
                elif neighbours[(0,1)].type == "Lava":
                    #print("cp 9")
                    # do_lava_collision() 
                    pass
        
        
        
        self.old_neighbours = neighbours
        grid.update_spatial_hash(self)
    
        self.old_cell_index = self.cell_index

            


    

    def check_water_collision(self, grid, neighbours):
        self.left_water  = neighbours[(0,1)]
        self.right_water = neighbours[(0,1)]
        
        
        
        self.left_neighbour  = self.left_water.get_neighbours(grid)[(-1,0)]
        self.right_neighbour = self.left_water.get_neighbours(grid)[(1,0)]
        
                
        
        
        def check_left(right_stuck=False):
            #print("Check  left")
            
            # if there is air left of "left_water" 
            if  self.left_neighbour == 0:
                self.rect.x = self.left_water.rect.x - grid.cell_size
                self.rect.y = self.left_water.rect.y
                return
            
            # if that particle is solid
            elif self.left_neighbour.state == "solid":
                if right_stuck:
                    return
                else: check_right(True)
                

            # particle is not  = 0 and its not solid ()
            elif self.left_neighbour.state == "liquid":

                # ...if that particle is water
                if self.left_neighbour.type == "Water":     
                    self.left_water = self.left_neighbour
                    self.left_neighbour = self.left_water.get_neighbours(grid) [(-1,0)]
                    check_right()
                
                # ...if that particle is lava
                elif self.left_neighbour.type == "Lava":
                    # do_lava_collision() 
                    pass
                    grid.delete_particle(self)

                
                        
                    
                    
                                        
                
        
        def check_right(left_stuck=False):
            #print("Check  right")    
            
                            
            # if there isnt a neighbour on left side of the "right_water" 
            if self.right_neighbour == 0:
                self.rect.x = self.right_water.rect.x + grid.cell_size
                self.rect.y = self.right_water.rect.y
                return
            
            # ...if that  particle is solid
            elif self.right_neighbour.state == "solid":
                if left_stuck:
                    return
                else: check_left(True)
                
                
            # if thereis a particle right of "rightt_water"...
            elif self.right_neighbour.state == "liquid":
                # ...if that particle is water
                if self.right_neighbour.type == "Water":   
                        self.right_water = self.right_neighbour
                        self.right_neighbour = self.right_water.get_neighbours(grid)[(1,0)]
                        check_left()

                # ...if that particle is lava
                elif self.right_neighbour.type == "Lava":
                    # do_lava_collision() 
                    pass
                    grid.delete_particle(self)
                
                
        
        check_left()


