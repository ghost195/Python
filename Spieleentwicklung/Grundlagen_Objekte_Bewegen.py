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

FPS = 30
imgx = 10
imgy = 10

pixMove = 5
movment = "down"

fpsTime = pygame.time.Clock()

while True:
    setDisplay.fill(black)
    
    
    if movment == "down":
        imgy += pixMove
        if imgy > 500:
            movment = "right"
    
    elif movment == "right":
        imgx += pixMove
        if imgx > 700:
            movment = "up"
            
    elif movment == "up":
        imgy -= pixMove
        if imgy < 40:
            movment = "left"
    
    elif movment == "left":
        imgx -= pixMove
        if imgx < 40:
            movment = "down"
            
            
    
    setDisplay.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        #print (event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
          
           
        
    pygame.display.update()
    fpsTime.tick(FPS)
    