#imports 
import pygame
import random


def display(text, x, y, size):
    set_my_font = pygame.font.SysFont("timesnewroman", 30)
    textSurface = set_my_font.render(text, True, "#000000")

screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Memory Game")

display()