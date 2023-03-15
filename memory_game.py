#imports 
import pygame
import random


def display(text, x, y, size):
    set_my_font = pygame.font.SysFont("timesnewroman", 30)
    textSurface = set_my_font.render(text, True, "#0000FF")


screen = pygame.display.set_mode((800,800))
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
blue_image = pygame.image.load("Python/Repositories/Final-Project-2023/big_blue_2.png")
blue_image = pygame.transform.flip(blue_image, True, False)
blue_image = pygame.transform.scale(blue_image, (200,200))
def blue_picture(x,y):
   screen.blit(blue_image, (200,100))



blue_picture()
random.randint(1,4)

