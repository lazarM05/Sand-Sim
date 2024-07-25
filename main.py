import pygame
import sys

from Particle import Particle
from Grid import Grid


win_width = 500
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))


grid = Grid(win_width,win_height,10)
space=False

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
            
            
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                space=True
            if event.key == pygame.K_z:
                
                for cell in grid.cell_list:
                    mouse_pos = pygame.mouse.get_pos()
                    if cell.rect.collidepoint(mouse_pos):
                        grid.add_particle(Particle(cell.rect.x, cell.rect.y, 0 , cell.cell_size))
                        print (len(grid.particle_list))
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space=False
            
                
        
                
    if space:
        for cell in grid.cell_list:
            mouse_pos = pygame.mouse.get_pos()
            if cell.rect.collidepoint(mouse_pos):
                
                #add particle to Grid particle list
                grid.add_particle(Particle(cell.rect.x, cell.rect.y, 0 , cell.cell_size))
                print (len(grid.particle_list))



   
    screen.fill((0,0,0))
    grid.draw(screen)
    

    for particle in grid.particle_list:
        particle.update(grid)
        particle.draw(screen)
    
    
    
    
    
    
    
    
    
    
    pygame.display.flip()
