import pygame
import sys


class Particle():
    
    def __init__(self, x,y, size=10):
        
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
        self.cell_index = (x//size, y//size)
        
        self.color = (100,100,100) # default
    
        self.solid = True
    
    
    def update(self, grid):
        pass
            
        
             
    def get_neighbours(self, grid):
        neighbours = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                neighbours.extend(grid.spatial_hash[self.cell_index[0] + dx, self.cell_index[1] + dy])
        return neighbours
        
    
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        
        
        
    
    
     