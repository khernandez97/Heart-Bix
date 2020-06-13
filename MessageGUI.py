import pygame
from Visuals import Setup as setup
from Visuals import Drawing as doodle
from FirebaseUpload import FBUsage as Fb
from Notifications import Notify as notify
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bblue = (0,255,255)
purple = (255,0,255)
        
setup.ready()
screen = setup.ready()
current_color = black

while True:
        for event in pygame.event.get():
             #print(event.type)
             key = pygame.key.get_pressed()
             imgRect = pygame.Rect(100,0,500,650)
             eraseRect = pygame.Rect(100,0,500,650)
             viewRect = pygame.Rect(100,0,500,650)
             #backRect = pygame.Rect(100,0,500,600)
             #back = pygame.Rect(0,100,200,600)

             erssub = screen.subsurface(eraseRect)
             imgsub = screen.subsurface(imgRect)
             viewsub = screen.subsurface(viewRect)
             #backsub = screen.subsurface(backRect)
             
             view = pygame.Surface((600,650))
             img = pygame.Surface((500,650))
             ers = pygame.Surface((600,650))
            # bck = pygame.Surface((500,600))
             
            # textFont = pygame.font.Font("freesansbold.ttf",30)
            # back_view = textFont.render("Back",True,purple,green)
            # screen.blit(back_view,back)
             
             if event.type == pygame.MOUSEBUTTONDOWN: 
                  x,y = doodle.getPos()
                  #print("X,Y: {},{}".format(x,y))
                  if(0<x<100):
                      if(0<y<80):
                            current_color = red
                            
                      if(80<y<160):
                            current_color = black
                            print(current_color)
                          
                            
                      if(160<y<240):
                            current_color = green
                            print(current_color)
                            
                            
                      if(240<y<320):
                            current_color = blue
                            print(current_color)
                           
                            
                      if(320<y<400):
                            current_color = bblue
                            print(current_color)
            
                            
                      if(400<y<480):
                            current_color = purple
                            print(current_color)
                            
                      if(500<y<550):
                              img.blit(imgsub,(0,0))
                              pygame.image.save(img, "C:/Users/khern/Desktop/Python/Practice.jpg")
                              Fb.Post()
                              status = notify.Send()
                              print(status)
                              if(status == 0):
                                      message = "Message Sent"
                                      setup.PopUp(message,screen)
                                      
                                      
                              else:
                                  print("Error sending  email")
                                  
                              
                              
                      if(550<y<600):
                              ers.blit(erssub,(0,0))
                              setup.ready()
                              
                      if(600<y<650):
                              view.blit(viewsub,(0,0))
                              newImg = Fb.Retrieve()
                              print(newImg)
                              if(newImg == True):
                                      screen.fill(white)
                                      imgLoad = pygame.image.load("Image.jpg")
                                      screen.blit(imgLoad,(0,0))
                                      #bck.blit(backsub,(0,0))
                                      pygame.display.update()
                                      Fb.Reset()
                                      
                              else:
                                      message = "No new messages"
                                      setup.PopUp(message,screen)                                  
                                      print("No new messages")
                      else:
                          if(current_color == None):
                             current_color = black
                             print(current_color)
                             
             if(key[pygame.K_RSHIFT]):
                        #print("A")
                        setup.ready()
                        pygame.display.update()
                
                      
                
             if(key[pygame.K_LSHIFT]):
                        if(event.type == pygame.MOUSEMOTION):
                            x,y = doodle.getPos()
                            if(x>100 and y<650):
                                    doodle.drawCircle(screen,x,y,current_color)
                            #print("Motion X,Y: {},{}".format(x,y))       
                  #if(100<x):
                  #      doodle.drawCircle(screen,x,y,current_color)
                        #while(event.type == pygame.MOUSEBUTTONDOWN):
                        #pygame.draw.circle(gameDisplay, current_color,[x,y],penradius)
        
