import pygame
import sys
from Particle import Particle
from Sand import Sand
from Lava import Lava

class Water(Particle):
    
    def __init__(self, x,y, size=10):
        super().__init__(x,y, size)
        self.color = (30,144,255) # water
        self.old_neighbours = None
        self.state = "liquid"
        self.type = Water 
        


    def update(self, grid):
        neighbours = self.get_neighbours(grid)
    
        # falls If there isnt a neighbour underneath of the particle...
        if neighbours[0]==0:
            # ...and particle isnt at the bottom row(bottom of the screen)
            if self.rect.bottom != grid.row_number * grid.cell_size:
                self.rect.y += grid.cell_size
                #print("Down")
                
            
            
        # if there is particle bellow... 
        else:
            #print("cp 1")
            # if no neighbours change nothing needs to be done so function returns
            if self.old_neighbours and all(self.old_neighbours[n] == neighbours[n] for n in range(len(neighbours))):
                #print("cp 2")
                return
            
             
            # ... if particle is solid..
            if neighbours[0].state=="solid":
                #print("cp 3")

                # ..if left and downleft neighbours are air, move left
                if neighbours[1] == 0 and (neighbours[1+2] == 0 or neighbours[1+2].state == "liquid"):
                    self.rect.x -= grid.cell_size
                    #print("cp 4")

                # .. if right and downright neighbours are air, move right
                elif neighbours[2] == 0 and (neighbours[2+2] == 0 or neighbours[2+2].state == "liquid"):
                    self.rect.x += grid.cell_size
                    #print("cp 5")


            # ... if particle is liquid..
            elif  neighbours[0].state == "liquid":
                #print("cp 6")

                if neighbours[0].type == Water:
                    #print("cp 7")
                    # water collision
                    self.check_water_collision(grid, neighbours)
                
                if neighbours[0].type == Lava:
                    #print("cp 9")
                    # do_lava_collision() 
                    pass

            
        self.old_neighbours = neighbours
        grid.update_spatial_hash(self)

            


    

    def check_water_collision(self, grid, neighbours):
        self.left_water  = neighbours[0]
        self.right_water = neighbours[0]
        
        
        
        self.left_neighbours  = self.left_water.get_neighbours(grid)
        self.right_neighbours = self.left_water.get_neighbours(grid)
        
                
        
        
        def check_left(right_stuck=False):
            #print("Check  left")
            
            # if there is air left of "left_water" 
            if  self.left_neighbours[1] == 0:
                self.rect.x = self.left_water.rect.x - grid.cell_size
                self.rect.y = self.left_water.rect.y
                return
                
            # if thereis a particle left of "left_water"...
            else:
                # ...if that particle is water
                if self.left_neighbours[1].type == Water:     
                    self.left_water = self.left_neighbours[1]
                    self.left_neighbours = self.left_water.get_neighbours(grid) 
                    check_right()
                
                # ...if that particle is lava
                elif self.left_neighbours[1].type == Lava:
                    # do_lava_collision() 
                    pass

                # ...if that particle is solid
                else:
                    if right_stuck:
                        return
                    else: check_right(True)
                        
                    
                    
                                        
                
        
        def check_right(left_stuck=False):
            #print("Check  right")    
            
                            
            # if there isnt a neighbour on left side of the "right_water" 
            if self.right_neighbours[2] == 0:
                self.rect.x = self.right_water.rect.x + grid.cell_size
                self.rect.y = self.right_water.rect.y
                return
                
                
            # if thereis a particle right of "rightt_water"...
            else:
                # ...if that particle is water
                if self.right_neighbours[2].type == Water:   
                        self.right_water = self.right_neighbours[2]
                        self.right_neighbours = self.right_water.get_neighbours(grid) 
                        check_left()

                # ...if that particle is lava
                elif self.right_neighbours[1].type == Lava:
                    # do_lava_collision() 
                    pass
                
                # ...if that  particle is solid
                else:
                    if left_stuck:
                        return
                    else: check_left(True)
        
        check_left()





    def get_neighbours(self, grid):
        neighbours = []
        down_neighbours = grid.spatial_hash[self.cell_index[0] + 0, self.cell_index[1] + 1]
        left_neighbours = grid.spatial_hash[self.cell_index[0] + -1, self.cell_index[1] + 0]
        right_neighbours = grid.spatial_hash[self.cell_index[0] + 1, self.cell_index[1] + 0]

        down_left_neighbours = grid.spatial_hash[self.cell_index[0] + -1, self.cell_index[1] + 1]
        down_right_neighbours = grid.spatial_hash[self.cell_index[0] + 1, self.cell_index[1] + 1]
        


        neighbours.extend(down_neighbours if down_neighbours else [0]) # Down
        neighbours.extend(left_neighbours if left_neighbours else [0]) # Left
        neighbours.extend(right_neighbours if right_neighbours else [0]) # Right

        neighbours.extend(down_left_neighbours if down_left_neighbours else [0]) # Down-Left
        neighbours.extend(down_right_neighbours if down_right_neighbours else [0]) # Down-Right
        

        return neighbours
