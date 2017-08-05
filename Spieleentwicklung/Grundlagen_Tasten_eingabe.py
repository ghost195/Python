import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
bg = black

fps = 1
dispWidth = 800
dispHeight = 600
cellSize = 10

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

def runGame():
    startx = 3
    starty = 3
    coords = [{'x': startx, 'y': starty}]

    
    direction = "RIGHT"
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = 'LEFT'
                elif event.key == K_RIGHT:
                    direction = 'RIGHT'
                elif event.key == K_UP:
                    direction = 'UP'
                    
                elif event.key == K_DOWN:
                    direction = 'DOWN'
                    
                    
        print(direction)
        if direction == 'UP':
            
            newCell = {'x':coords[0]['x'],'y':coords[0]['y']-1 } 
            
        elif direction == 'DOWN':
                  
            newCell = {'x':coords[0]['x'],'y':coords[0]['y']+1 }
                
        elif direction == 'LEFT':
            
            newCell = {'x':coords[0]['x']-1,'y':coords[0]['y']}
                
        elif direction == 'RIGHT':
            
            newCell = {'x':coords[0]['x']+1,'y':coords[0]['y']}
            
        print(newCell)   
        del coords[-1]
            
        coords.insert(0, newCell)
        setDisplay.fill(bg)
        drawCell(coords)
        pygame.display.update()
        fpsTime.tick(fps)
        
            
def drawCell(coords):
   
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize,cellSize)
        pygame.draw.rect(setDisplay,white,makeCell)
        

while True:
    global fpsTime
    global setDisplay
    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
    pygame.display.set_caption("Mein Spiel")
    runGame()
    