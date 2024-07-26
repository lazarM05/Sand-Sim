import pygame
import sys


class Sand():

    def __init__(self, x,y, size=10):
        
        self.gravity = 1
            
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
        
        self.cell_index = (x//size, y//size)
        
        
        self.color = (255,140,0) # sand
    
    
    
    def update(self, grid):
        self.gravity = 1
        stable=0
        neigbours = self.get_neighbours(grid)
        
        
        
        for particle in neigbours:
            
            # particle on top
            if self.rect.bottomleft==particle.rect.topleft and particle.gravity == 0 and particle!=self:
                
                if any(particle.rect.topleft == p.rect.topright and p!=particle  for p in neigbours):
                    stable=1
                    if any(particle.rect.topright == p.rect.topleft and stable==1  and p!=particle   for p in neigbours):
                        stable=0
                        self.gravity = 0
                
                else: stable =-1
                
            # particle inside
            if self.rect.topleft == particle.rect.topleft and particle!=self and particle.gravity == 0:
                self.rect.y -= grid.cell_size            
        
           
          
        #grid bounderies      
        if self.rect.bottom == grid.row_number * grid.cell_size:
            self.gravity = 0
            stable = 0
            
        if stable == -1:
            self.rect.x -= grid.cell_size
            
        elif stable == 1:
            self.rect.x += grid.cell_size
            
        if self.gravity == 1:
            self.rect.y += grid.cell_size
            
            
        
            
        grid.update_spatial_hash(self)
            
        
             
    def get_neighbours(self, grid):
        neighbours = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                neighbours.extend(grid.spatial_hash[self.cell_index[0] + dx, self.cell_index[1] + dy])
        return neighbours
        
    
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        
        
        
    
    
     