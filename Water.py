import pygame
import sys
from Particle import Particle

class Water(Particle):
    
    def __init__(self, x,y, size=10,):
        super().__init__(x,y, size)
        self.color = (30,144,255) # water
        self.old_neighbours = None
        self.solid = True
        
        
    def update(self, grid):
        
        neighbours = self.get_neighbours(grid)
        
        if self.old_neighbours == None:
            self.old_neighbours = neighbours
        
        
        if len(self.old_neighbours) == len(neighbours) > 0 and neighbours[0].rect.x == self.rect.x:
            if all(self.old_neighbours[n] == neighbours[n] for n in range(len(neighbours))):
                #print("SAME")
                return
    
    
        # falls If neighbours is empty or there isnt a neighbour underneath of the particle(just left or right)
        if len(neighbours)==0 or  len(neighbours)>0 and  neighbours[0].rect.x != self.rect.x:
            
            if self.rect.bottom != grid.row_number * grid.cell_size:
                self.rect.y += grid.cell_size
                print("Down")
                
            
            
            
        # it cant be emty and it must be underneath
        elif isinstance(neighbours[0], Water) and  neighbours[0].rect.x == self.rect.x:
            print("cp 1")
            self.left_water  = neighbours[0]
            self.right_water = neighbours[0]
            
            print("cp 2")
            
            self.left_neighbours  = self.left_water.get_neighbours(grid)
            self.right_neighbours = self.left_water.get_neighbours(grid)
            
            
            print("cp 3")
            
            
            
            def check_left(right_stuck=False):
                print("Check  left")
                
                # if there isnt a neighbour on left side of the "left_water" 
                if not any(neighbour.rect.topright == self.left_water.rect.topleft for neighbour in self.left_neighbours):
                    self.rect.x = self.left_water.rect.x - grid.cell_size
                    self.rect.y = self.left_water.rect.y
                    print("L empty")
                    return
                    
                print("cp 4")
                for neighbour in self.left_neighbours:
                    
                    if neighbour.rect.topright == self.left_water.rect.topleft:
                        
                        if isinstance(neighbour, Water):
                            
                            self.left_water = neighbour
                            self.left_neighbours = self.left_water.get_neighbours(grid) 
                            check_right()
                        else:
                            if right_stuck:
                                return
                            else: check_right(True)
                            
                        
                        
                                            
                    
            
            def check_right(left_stuck=False):
                print("Check  right")    
                
                                
                # if there isnt a neighbour on left side of the "right_water" 
                if not any(neighbour.rect.topleft == self.right_water.rect.topright for neighbour in self.right_neighbours):
                    self.rect.x = self.right_water.rect.x + grid.cell_size
                    self.rect.y = self.right_water.rect.y
                    return
                    
                    
                for neighbour in self.right_neighbours:
                    
                    if neighbour.rect.topleft == self.right_water.rect.topright:
                        
                        if isinstance(neighbour, Water):
                            
                            self.right_water = neighbour
                            self.right_neighbours = self.right_water.get_neighbours(grid) 
                            check_left()
                        else:
                            if left_stuck:
                                return
                            else: check_left(True)
            
            check_left()
            
        self.old_neighbours = neighbours
        grid.update_spatial_hash(self)

            
    
    def get_neighbours(self, grid):
        neighbours = []
        neighbours.extend(grid.spatial_hash[self.cell_index[0] + 0, self.cell_index[1] + 1]) # Down
        neighbours.extend(grid.spatial_hash[self.cell_index[0] + 1, self.cell_index[1] + 0]) # Right
        neighbours.extend(grid.spatial_hash[self.cell_index[0] + -1, self.cell_index[1] + 0]) # Left

        return neighbours
