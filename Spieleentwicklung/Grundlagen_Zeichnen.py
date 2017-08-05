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

setDisplay.fill(cyan)

singlePixel = pygame.PixelArray(setDisplay)
singlePixel[3][30] = black

pygame.draw.line(setDisplay,blue,(389,200),(300,710),4)         #Linie Zeichnen

pygame.draw.circle(setDisplay,red,(50,50),20,20)                #Kreis Zeichnen

pygame.draw.rect(setDisplay,purple,(100,100,200,100))           #Rechteck Zeichnen

pygame.draw.polygon(setDisplay, green, ((150,210),(130,140),(60,100),(250,350)))    #Polygon Zeichnen




while True:
    for event in pygame.event.get():
        #print (event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
          
           
        
    pygame.display.update()
    