import pygame 

#game file is the vertual machine 

#game window

#initializes the pygame
pygame.init()

#creates the screen
screen = pygame.display.set_mode((800, 600)) #(width, height)

#Title and Icon of window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#player 
playerImg = pygame.image.load("spaceship.png")
DEFAULT_IMAGE_SIZE = (70,70)  #resizes the player image
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE) #transforms the player image
playerX = 370 
playerY = 480

playerX_change = 0


def player(x,y):
    #draws the player (player img, coordinate x, coordinate y)
    screen.blit(playerImg, (playerX, playerY)) 


#Game loop
running  = True
while running:

    #RGB - Red ,green , or blue
    screen.fill((255, 0, 0)) #red color

    


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check wheather it is left or right
        #adds player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key  == pygame.K_RIGHT:
                playerX_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key  == pygame.K_RIGHT:
                playerX_change = 0

    
    #anything you want to appear continusly 
    playerX += playerX_change
    
    #prevent the spaceship to go beyond the game window (800 - 70 = 730)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    player(playerX, playerY)

    #always need the update the dispplay
    pygame.display.update()

   

