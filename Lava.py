
import pygame
import sys
from Particle import Particle
from Stone import Stone


class Lava(Particle):
    
    def __init__(self, x,y, size=10):
        super().__init__(x,y, size)
        self.color = (250, 75, 5) # red-ish
        self.state = "liquid"
        self.type = "Lava" 

        self.old_neighbours = None


    def update(self, grid):

        
        neighbours = self.get_neighbours(grid)
    
        # falls If there isnt a neighbour underneath of the particle...
        if neighbours[(0,1)]==0:
            self.rect.y += grid.cell_size
            #print("Down")
                
        
            
        # if there is particle bellow... 
        else:
            #print("cp 1")
            # if no neighbours change nothing needs to be done so function returns
            if self.old_neighbours and all(
                self.old_neighbours[key] == neighbours.get(key, None)
                for key in self.old_neighbours
            ): return

            elif any((neighbours[n]!=0) and (neighbours[n].type=="Water") for n in [(-1,0),(1,0),(0,-1),(0,1)]):
                grid.delete_particle(self)
                grid.add_particle(Stone(self.rect.x, self.rect.y, grid.cell_size))


            ### if  inside a particle ###
            elif len(neighbours[(0, 0)])>1 and any(n.state in ["solid","liquid"]  and n!=self for n in neighbours[(0, 0)]):
                self.rect.y -= grid.cell_size
             
            # ... if particle is solid..
            elif neighbours[(0,1)].state=="solid":
                #print("cp 3") 

                # ..if left and downleft neighbours are air, move left
                if neighbours[(-1,0)] == 0 and (neighbours[(-1,1)] == 0 or neighbours[(-1,1)].state == "liquid"):
                    self.rect.x -= grid.cell_size
                    #print("cp 4")

                # .. if right and downright neighbours are air, move right
                elif neighbours[(1,0)] == 0 and (neighbours[(1,1)] == 0 or neighbours[(1,1)].state == "liquid"):
                    self.rect.x += grid.cell_size
                    #print("cp 5")


            # ... if particle is liquid..
            elif  neighbours[(0,1)].state == "liquid":
                #print("cp 6")

                if neighbours[(0,1)].type == "Lava":
                    #print("cp 7")
                    # water collision
                    
                    
                    self.check_lava_collision(grid, neighbours)
                
                elif neighbours[(0,1)].type == "Water":
                    #print("cp 9")
                    # do_lava_collision() 
                    pass
                    
        
            
        self.old_neighbours = neighbours
        grid.update_spatial_hash(self)

            


    

    def check_lava_collision(self, grid, neighbours):
        self.left_lava  = neighbours[(0,1)]
        self.right_lava = neighbours[(0,1)]
        
        
        
        self.left_neighbours  = self.left_lava.get_neighbours(grid)
        self.right_neighbours = self.left_lava.get_neighbours(grid)
        
                
        
        
        def check_left(right_stuck=False):
            #print("Check  left")
            
            # if there is air left of "left_lava" 
            if  self.left_neighbours[(-1,0)] == 0:
                self.rect.x = self.left_lava.rect.x - grid.cell_size
                self.rect.y = self.left_lava.rect.y
                return
                
            # if thereis a particle left of "left_lava"...
            else:
                # ...if that particle is lava
                if self.left_neighbours[(-1,0)].type == "Lava":     
                    self.left_lava = self.left_neighbours[(-1,0)]
                    self.left_neighbours = self.left_lava.get_neighbours(grid) 
                    check_right()
                
                # ...if that particle is lava
                elif self.left_neighbours[(-1,0)].type == "Water":
                    # do_Water_collision() 
                    pass

                # ...if that particle is solid
                else:
                    if right_stuck:
                        return
                    else: check_right(True)
                        
                    

                
        
        def check_right(left_stuck=False):
            #print("Check  right")    
            
                            
            # if there isnt a neighbour on left side of the "right_lava" 
            if self.right_neighbours[(1,0)] == 0:
                self.rect.x = self.right_lava.rect.x + grid.cell_size
                self.rect.y = self.right_lava.rect.y
                return
                
                
            # if thereis a particle right of "rightt_lava"...
            else:
                # ...if that particle is lava
                if self.right_neighbours[(1,0)].type == "Lava":   
                        self.right_lava = self.right_neighbours[(1,0)]
                        self.right_neighbours = self.right_lava.get_neighbours(grid) 
                        check_left()

                # ...if that particle is lava
                elif self.right_neighbours[(1,0)].type == "Water":
                    # do_water_collision() 
                    pass
                
                # ...if that  particle is solid
                else:
                    if left_stuck:
                        return
                    else: check_left(True)
        
        check_left()


