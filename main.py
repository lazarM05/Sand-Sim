import pygame
import sys

from Particle import Particle
from Grid import Grid
from Water import Water
from Sand import Sand


win_width = 1000
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))


grid = Grid(win_width,win_height,10)
space=False
particle_type = 0
particle_type_list = [Sand,Water]

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
            
            
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                space=True
            if event.key == pygame.K_x:
                
                for cell in grid.cell_list:
                    mouse_pos = pygame.mouse.get_pos()
                    if cell.rect.collidepoint(mouse_pos):
                        grid.add_particle(particle_type_list[particle_type](cell.rect.x, cell.rect.y, cell.cell_size))
                        print (len(grid.particle_list))
                        
            if event.key == pygame.K_1:
                particle_type=0                       
            if event.key == pygame.K_2:
                particle_type=1
                    
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space=False
            
                
        
                                    
    if space:
        for cell in grid.cell_list:
            mouse_pos = pygame.mouse.get_pos()
            if cell.rect.collidepoint(mouse_pos):
                
                #add particle to Grid particle list
                grid.add_particle(particle_type_list[particle_type](cell.rect.x, cell.rect.y, cell.cell_size))
                print (len(grid.particle_list))



   
    screen.fill((0,0,0))
    grid.draw(screen)
    

    for particle in grid.particle_list:
        particle.update(grid)
        particle.draw(screen)
    
    
    
    
    
    
    
    
    
    
    pygame.display.flip()
