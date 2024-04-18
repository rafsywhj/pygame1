# Import the pygame module
import pygame,sys
import time
# Import random for random numbers
import random
# Import pygame.locals for easier access to key coordinates
from pygame.locals import *


# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Initialize pygame
pygame.init()
# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        self.rect.x = 1
        self.rect.y = 500
        #this determines tafrget has to moveLeft or right
        self.moveLeft=False



all_sprites = pygame.sprite.Group()



def createPlayerTarget():
    # Create player ,add to group
    player = Player()
    all_sprites.add(player)
    #create target,add to group
    target=Target()
    all_sprites.add(target)
    return player,target
    

def startgame():
    player,target=createPlayerTarget()
    #draw sprites
    all_sprites.draw(screen)
    pygame.display.update()


startgame()


          
        
