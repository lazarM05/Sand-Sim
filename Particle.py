import pygame
import sys


class Particle():
    
    def __init__(self,x ,y, size=10, type = None, state =""):
        
        self.type = type
        self.state = state

        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
        
        self.cell_index = (x//size, y//size)
        self.old_cell_index = None

        self.color = (0,0,0) # default
        self.pressure = 1

        self.font = pygame.font.Font(None, 18)  
    
    
    
    def update(self, grid):
        grid.update_spatial_hash(self)
            
        
             
    def get_neighbours(self, grid):
        neighbours = {}
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:                
                # Compute the neighbor's cell index
                neighbour_index = (self.cell_index[0] + dx, self.cell_index[1] + dy)
                # Get the particles in the neighbor cell
                new_neighbour = grid.spatial_hash.get(neighbour_index, [])

                #particles in the same position as this particle
                if dx == 0 and dy == 0:
                    neighbours[(dx, dy)] = new_neighbour

                # Store the one particle in the dictionary with the offset as the key
                else: neighbours[(dx, dy)] = new_neighbour[0] if new_neighbour else 0
        return neighbours


    
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        #self.display_pressure(screen)
        
        
    def display_pressure(self,screen):
        pressure_text = self.font.render(str(self.pressure), True, (0,0,0))  # black color text
        text_rect = pressure_text.get_rect(center=self.rect.center)
        screen.blit(pressure_text, text_rect)
    

     