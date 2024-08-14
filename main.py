import pygame
import sys

from Particle import Particle
from Grid import Grid
from Stone import Stone
from Water import Water
from Sand import Sand
from Barrier import Barrier
from Lava import Lava
from Cloud import Cloud



win_width = 1000
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))
pygame.font.init()


grid = Grid(win_width,win_height,10)

# create barrier(s) border
for row in range(grid.row_number):
    grid.add_particle(Barrier(0, row*grid.cell_size, grid.cell_size))
    grid.add_particle(Barrier((grid.col_number-1)*grid.cell_size, row*grid.cell_size, grid.cell_size))
for col in range(grid.col_number):
    grid.add_particle(Barrier(col*grid.cell_size, 0, grid.cell_size))
    grid.add_particle(Barrier(col*grid.cell_size-1, (grid.row_number-1)*grid.cell_size, grid.cell_size))






space=False

particle_type = 0
particle_type_list = [Sand,Water,Lava,Stone,Cloud,Barrier]

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
            


            
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                particle_type=0                        
            if event.key == pygame.K_2:
                particle_type=1
            if event.key == pygame.K_3:
                particle_type=2
            if event.key == pygame.K_4:
                particle_type=3
            if event.key == pygame.K_5:
                particle_type=4
            if event.key == pygame.K_0:
                particle_type=-1
            

            if event.key == pygame.K_x:
                for cell in grid.cell_list:
                    mouse_pos = pygame.mouse.get_pos()
                    if cell.rect.collidepoint(mouse_pos):
                        if not grid.spatial_hash[cell.col, cell.row]:
                            grid.add_particle(particle_type_list[particle_type](cell.rect.x, cell.rect.y, grid.cell_size))
                            print (len(grid.particle_list))

            if event.key == pygame.K_y:
                mouse_pos = pygame.mouse.get_pos()
                for cell in grid.cell_list:
                    if cell.rect.collidepoint(mouse_pos):
                        particles = grid.spatial_hash[cell.col, cell.row]
                        if particles:
                            # Remove all particles in the cell (if desired)
                            for particle in particles:
                                grid.delete_particle(particle)
                            print(len(grid.particle_list))
                            


    space_pressed = pygame.key.get_pressed()[pygame.K_SPACE]
    shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT
    

                                    
    if space_pressed:
        for cell in grid.cell_list:
            mouse_pos = pygame.mouse.get_pos()
            if cell.rect.collidepoint(mouse_pos):
                if not grid.spatial_hash[cell.col, cell.row]:
                    #add particle to Grid particle list
                    grid.add_particle(particle_type_list[particle_type](cell.rect.x, cell.rect.y, grid.cell_size))
                    print (len(grid.particle_list))

    if shift_pressed:
        mouse_pos = pygame.mouse.get_pos()
        for cell in grid.cell_list:
            if cell.rect.collidepoint(mouse_pos):
                particles = grid.spatial_hash[cell.col, cell.row]
                if particles:
                    # Remove all particles in the cell (if desired)
                    for particle in particles:
                        if particle.type != "Barrier":
                            grid.delete_particle(particle)
                    print(len(grid.particle_list))

   



    screen.fill((0,0,0))
    grid.draw(screen)
    

    for particle in grid.particle_list:
        particle.update(grid)
        particle.draw(screen)
    
    

    
    
    
    
    pygame.display.flip()
