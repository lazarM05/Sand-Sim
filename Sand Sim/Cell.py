import pygame
import sys


class Cell():

    def __init__(self, col,row, size):
        self.col = col
        self.row = row
        self.cell_size = size
        self.empty = True
        self.rect = pygame.Rect(col*size, row*size, size, size)
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, (50,50,50), self.rect,1)
    