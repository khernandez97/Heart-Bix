import pygame
import time
import random
from PySide2.QtWidgets import QErrorMessage

class Setup():
    
    def ready():

        pygame.init()
        size = (600,650)
        
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        bblue = (0,255,255)
        purple = (255,0,255)
        
        rect1 = pygame.Rect(0,0,100,80)
        rect2 = pygame.Rect(0,80,100,80)
        rect3 = pygame.Rect(0,160,100,80)
        rect4 = pygame.Rect(0,240,100,80)
        rect5 = pygame.Rect(0,320,100,80)
        rect6 = pygame.Rect(0,400,100,80)

        done = pygame.Rect(0,500,200,650)
        erase = pygame.Rect(0,550,200,650)
        view = pygame.Rect(0,600,200,650)
        #back = pygame.Rect(0,100,200,600)
        
        penradius = 5

        gameDisplay = pygame.display.set_mode(size)
        gameDisplay.fill(white)

        pygame.display.set_caption("Drawing Time")
        clock = pygame.time.Clock()

        pygame.draw.rect(gameDisplay, red, rect1)
        pygame.draw.rect(gameDisplay, black, rect2)
        pygame.draw.rect(gameDisplay, green, rect3)
        pygame.draw.rect(gameDisplay, blue, rect4)
        pygame.draw.rect(gameDisplay, bblue, rect5)
        pygame.draw.rect(gameDisplay, purple, rect6)

        textFont = pygame.font.Font("freesansbold.ttf",30)
        done_text = textFont.render("Done ",True,black,red)
        gameDisplay.blit(done_text,done)

        erase_text = textFont.render("Erase",True,purple,green)
        gameDisplay.blit(erase_text,erase)

        view_image = textFont.render("New   ",True,bblue,blue)
        gameDisplay.blit(view_image,view)
        
        
        #pygame.draw.rect(gameDisplay, red, done)
        current_color = None
        
        pygame.display.update()
        return gameDisplay

    def PopUp(message,screen):
        blue = (0,0,255)
        bblue = (0,255,255)
        textFont = pygame.font.Font("freesansbold.ttf",30)
        msg = pygame.Rect(275,275,50,100)
        disp_msg = textFont.render(message,True,bblue,blue)
        screen.blit(disp_msg,msg)
        pygame.display.update()
    
class Drawing():

    def getPos():
        x,y = pygame.mouse.get_pos()
        return (x,y)
            
    def drawCircle(screen,touchX,touchY,current_color):
        pygame.draw.circle(screen, current_color, (touchX,touchY),3)
        pygame.display.update()


