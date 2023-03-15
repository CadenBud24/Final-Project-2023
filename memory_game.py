import pygame
background_colour = (200,200,200)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Memory Game')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


blue_image = pygame.image.load("big_blue_2.png")
blue_image = pygame.transform.scale(blue_image, (200,200))

red_image = pygame.image.load("big_red.png")
red_image = pygame.transform.scale(red_image, (200,200))

yellow_image = pygame.image.load("big_yellow.png")
yellow_image = pygame.transform.scale(yellow_image, (200,200))

green_image = pygame.image.load("big_green.png")
green_image = pygame.transform.scale(green_image, (200,200))

purple_image = pygame.image.load("big_purple.png")
purple_image = pygame.transform.scale(purple_image, (200,200))

