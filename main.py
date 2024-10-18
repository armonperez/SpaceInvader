import pygame 
import random
import math

#game file is the vertual machine 

#game window

#initializes the pygame
pygame.init()

#creates the screen
screen = pygame.display.set_mode((800, 600)) #(width, height)

#Backgound
background = pygame.image.load("hubble-ngc5248-potw2441a.png.webp")
DEFAULT_IMAGE_SIZE = (800,600)
background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)

#Title and Icon of window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


#Player
playerImg = pygame.image.load("spaceship.png")
DEFAULT_IMAGE_SIZE = (70,70)  #resizes the player image
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE) #transforms the player image
playerX = 370 
playerY = 480
playerX_change = 0



#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    original_img = pygame.image.load("space-ship.png")
    DEFAULT_IMAGE_SIZE = (70,70)  #resizes the player image
    enemyChar = pygame.transform.scale(original_img, DEFAULT_IMAGE_SIZE) #transforms the player image
    enemyImg.append(enemyChar)
    enemyX.append(random.randint(0,729)) #spawn in different places
    enemyY.append (random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append (40)



#bullet 
bulletImg = pygame.image.load("bullet.png")
DEFAULT_IMAGE_SIZE = (70,70)  
bulletImg = pygame.transform.scale(bulletImg, DEFAULT_IMAGE_SIZE) #transforms the player image
bulletX = 0 
bulletY = 480
bulletX_change = 0 
bulletY_change = 10
bullet_state = "ready" 
#ready state means you cant see the bullet 
#fire stare means the bullet is currently moving


#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x,y):
    #render the text for the score
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))





def player(x,y):
    #draws the player (player img, coordinate x, coordinate y)
    screen.blit(playerImg, (x, y)) 

def enemy(x,y, i):
    #draws the player (player img, coordinate x, coordinate y)
    screen.blit(enemyImg[i], (x, y)) 

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x , y ))


def isCollision(enemyX, enemyY, bulletX, bulletY):

    distance =  math.sqrt((math.pow(enemyX- bulletX, 2)) + ( math.pow(enemyY - bulletY, 2)))

    if distance < 27:
        return True
    
    return False




#Game loop
running  = True
while running:

    #RGB - Red ,green , or blue
    screen.fill((0, 0, 0)) #black color

    #background image
    screen.blit(background,(0,0))
    


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check wheather it is left or right
        #adds player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key  == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key  == pygame.K_RIGHT:
                playerX_change = 0

    
    #anything you want to appear continusly
    # 
    #  
    playerX += playerX_change
    
    #prevent the spaceship to go beyond the game window (800 - 70 = 730)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730


    enemyX += enemyX_change
    
    #prevent the enemy to go beyond the game window (800 - 70 = 730)
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change [i]= 1
            enemyY[i] += enemyY_change[i]
        elif enemyX [i]>= 730:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]




        collision = isCollision(enemyX[i],enemyY[i], bulletX, bulletY )
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,729) 
            enemyY [i]= random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)


    # bullet movement 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    player(playerX, playerY)


    show_score(textX, textY)
    #always need the update the dispplay
    pygame.display.update()

   

