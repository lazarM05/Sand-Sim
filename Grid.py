import pygame
import sys

from Cell import Cell
from collections import defaultdict




class Grid():
    
    def __init__(self, width, height, cell_size):
        
        self.col_number = int(width/cell_size)
        self.row_number = int(height/cell_size)
        
        self.cell_size = cell_size
        
        self.cell_list = []
        self.particle_list=[]
        self.spatial_hash = defaultdict(list)
        
        
        for col in range(self.col_number):
            for row in range(self.row_number):
                self.cell_list.append(Cell(col,row,cell_size))
            
            
            
            
            
    def add_particle(self,particle):
        self.particle_list.append(particle)
        cell_index = (particle.rect.x // self.cell_size, particle.rect.y // self.cell_size)
        self.spatial_hash[cell_index].append(particle)
        
        
    def update_spatial_hash(self, particle):
        new_cell_index = (particle.rect.x // self.cell_size,  particle.rect.y // self.cell_size)
        if new_cell_index != particle.cell_index:
            self.spatial_hash[particle.cell_index].remove(particle)
            self.spatial_hash[new_cell_index].append(particle)
            particle.cell_index = new_cell_index
        
        
            
    def draw(self, screen):
        for cell in self.cell_list:
            cell.draw(screen)
        
            
        
        