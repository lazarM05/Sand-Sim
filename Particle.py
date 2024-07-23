import pygame
import sys


class Particle():
    
    def __init__(self, x,y, type, size=10):
        
        self.state = 1
        self.type = type   
            
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
        
        
        
        if self.type == 0:
            self.color = (255,140,0) # sand
        elif self.type == 1:
            self.color = (30,144,255) # water
        else: 
            self.color == (255,255,255) # default
    
    
    
    def update(self, grid):
        
        self.state = 1
        
        stable=0
       
        for particle in grid.particle_list:
            # particle on top
            if self.rect.bottomleft==particle.rect.topleft and particle.state == 0 and particle!=self:
                
                if any(particle.rect.topleft == p.rect.topright and p!=particle  for p in grid.particle_list):
                    stable=1
                    if any(particle.rect.topright == p.rect.topleft and stable==1  and p!=particle   for p in grid.particle_list):
                        stable=0
                        self.state = 0
                
                else: stable =-1
                
            # particle inside
            if self.rect.topleft == particle.rect.topleft and particle!=self and particle.state == 0:
                self.rect.y -= grid.cell_size
                
           
                
    
                
            
            
                
          
        #grid bounderies      
        if self.rect.bottom == grid.row_number * grid.cell_size:
            self.state = 0
            stable = 0
            
        if stable == -1:
            self.rect.x -= grid.cell_size
            
        elif stable == 1:
            self.rect.x += grid.cell_size
            
            
        if self.state == 1:
            self.rect.y += grid.cell_size
            
        
             
            
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        
    
    
     