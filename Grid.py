import pygame
import sys

from Cell import Cell






class Grid():
    
    def __init__(self, width, height, cell_size):
        
        self.col_number = int(width/cell_size)
        self.row_number = int(height/cell_size)
        
        self.cell_size = cell_size
        
        self.cell_list = []
        self.particle_list=[]
        
        
        col = 0
        while col < self.col_number:
            row = 0
            while row < self.row_number:
                self.cell_list.append(Cell(col,row,cell_size))
                row += 1
            col += 1
            
            
    def draw(self, screen):
        for cell in self.cell_list:
            cell.draw(screen)
        
            
        
        