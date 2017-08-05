import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game")


img = pygame.image.load("Pacman2.png")
imgx = 10
imgy = 10



while True:
    setDisplay.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        #print (event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
          
           
        
    pygame.display.update()
    