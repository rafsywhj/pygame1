# Import the pygame module
import pygame,sys
import time
# Import random for random numbers
import random
# Import pygame.locals for easier access to key coordinates
from pygame.locals import *

pygame.init()
# Set the height and width of the screen
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])



# Define the Player sprite
#Player starts at (0,0) by deafult
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()

#Target sprite of player 
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('target.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.center=pygame.mouse.get_pos()
        #this determines tafrget has to moveLeft or right
        self.moveLeft=False
#CREATE TARGET PLAYER AND SPRITE GROUP
allsprites = pygame.sprite.Group()
player = Player()
allsprites.add(player)
target=Target()
allsprites.add(target)
    
playing= True

while playing:
    #refresh 60 times in a second
    #can be used to control speed
    #quit the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            playing=False
        #place the background
        background = pygame.image.load("background.jpg")
        bg = pygame.transform.scale(background, (screen_width,screen_height))
        screen.blit(bg,(0,0))
        #move Target with mouse 
        if event.type==pygame.MOUSEMOTION:
            x,y=pygame.mouse.get_pos()
            target.rect.x=x
            target.rect.y=y
            
            
        #move the sprite as per key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: # UP
            if player.rect.y> 0:     
                 player.rect.y -= 5
        if keys[pygame.K_DOWN] : # DOWN
            if player.rect.y <630:
                player.rect.y += 5 
        
        if keys[pygame.K_LEFT] : # LEFT
            if player.rect.x> 0:    
                 player.rect.x -= 5 
        
        if keys[pygame.K_RIGHT] : # RIGHT
             if player.rect.x <850:
                 player.rect.x += 5  
        # Draw the spite to the screen 
        allsprites.draw(screen)
       
    pygame.display.update()
        
pygame.quit()

          
        
