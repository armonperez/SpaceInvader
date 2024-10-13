import pygame 

#game file is the vertual 

#game window

#initializes the pygame
pygame.init()
#creates the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon of window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Game loop
running  = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    #anything you wont to appear continusly 
    #RGB - Red ,green , or blue
    screen.fill((0, , 0))