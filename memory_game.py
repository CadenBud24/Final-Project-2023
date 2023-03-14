#imports 
import pygame
import random


def display(text, x, y, size):
    set_my_font = pygame.font.SysFont("timesnewroman", 30)
    textSurface = set_my_font.render(text, True, "#000000")


screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Memory Game")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pass



    pygame.display.flip()

pygame.quit()