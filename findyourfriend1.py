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


#Enemy sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()        
        self.image = pygame.transform.scale(self.image, (60,60))
        # The starting position is randomly generated
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)
        #speed is randomly generated
        self.speed = random.randint(1,7)

    
#obstacle sprites
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()                
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect=self.image.get_rect()
        # The starting position is randomly generated
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)


enemies=["enemy1.png","enemy2.png","enemy3.png","enemy4.png"]
obstacles=["obstacle1.png","obstacle2.png","obstacle3.png","obstacle4.png"]

# Create groups to hold sprites
enemy_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

def createEnemy():
    # Create enemy, and add to groups
    new_enemy = Enemy(random.choice(enemies))
    enemy_group.add(new_enemy)
    all_sprites.add(new_enemy)
    return new_enemy

def createObstacle():
    # Create obstacle, and add to groups
    new_obstacle = Obstacle(random.choice(obstacles))
    obstacle_group.add(new_obstacle)
    all_sprites.add(new_obstacle)
    return new_obstacle


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

    #need to be removed in next session
    createEnemy()
    createObstacle()
    #draw sprites
    all_sprites.draw(screen)
    pygame.display.update()
   


startgame()
pygame.quit()


          
        
