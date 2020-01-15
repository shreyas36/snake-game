import pygame
import random

pygame.init()

display_width=800
bsize=20
display_height=600
starting_length=0

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sdzero')

red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
grey=(128,128,128)
yellow=(255,255,0)
black=(0,0,0)

clock=pygame.time.Clock()
font1=pygame.font.SysFont(None, 80)
font2=pygame.font.SysFont(None,30)
#================    APPLE CLASS   ===========================================================================================
class cherry():
    def __init__(self):
        self.x=random.randrange(0,display_width-bsize,bsize)
        self.y=random.randrange(0,display_height-bsize,bsize)

    def randomize(self):
        self.x=random.randrange(0,display_width-bsize,bsize)
        self.y=random.randrange(0,display_height-bsize,bsize)

#================   SNAKE CLASS =============================================================================================
class snake_class():
    def __init__(self):
        self.length=0
        self.tail=[]

    def eaten(self,a,b):
        self.length+=1
        self.tail.append((a,b))
        apple.randomize()

    def snake_updater(self,a,b):
        self.tail.append((a,b))
        if len(self.tail)>starting_length:
            del self.tail[0]

    def drawsnake(self):
        for x,y in self.tail:
            pygame.draw.rect(gamedisplay,white,[x,y,bsize,bsize])
            pygame.draw.rect(gamedisplay,black,[x,y,bsize,bsize],1)

#====================================================================================================================
apple=cherry()
snake=snake_class()
#============  BUTTONS  ==========================================================================================
def retryandquit(x,y):
    if y>400 and y<448 :
        if x>100 and x<279:
            return 'retry'
        elif x>500 and x<679:
            return 'quit'


#================  TEXT  ============================================================================================
def message(msg,color,font,y_disp=0):
    textSurf=font.render(msg,True,color)
    textRect=textSurf.get_rect()
    textRect.center=display_width/2,display_height/2+y_disp
    gamedisplay.blit(textSurf,textRect)

#=================  MAINFUNCTION  =======================================================================================
def gameloop():

    gameon = True

    leadx=display_width/2
    leady=display_height/2
    speedx=0
    speedy=0
    speed=bsize
    FPS=10
    game_quit=pygame.image.load('quit.png')#image for quit button
    retry=pygame.image.load("retry.png")#image for retry button
    img=pygame.image.load('snakehead.png')#image for head of snake

#===================   MAINLOOP  ====================================================================================
    while gameon:

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameon=False
#=======================  MOVING  =======================================================================
            if event.type == pygame.KEYDOWN :
                if event.key== pygame.K_LEFT:
                    if speedx!=speed:
                        speedx=-speed
                        speedy=0
                elif event.key== pygame.K_RIGHT:
                    if speedx!=-speed:
                        speedx=speed
                        speedy=0
                elif event.key== pygame.K_UP:
                    if speedy!=speed:
                        speedy=-speed
                        speedx=0
                elif event.key== pygame.K_DOWN:
                    if speedy!=-speed:
                        speedy=speed
                        speedx=0
                elif event.key==pygame.K_p:
                    paused=True
                    message("Paused",black,font1)
                    pygame.display.update()
                    while paused:
                        clock.tick(5)
                        for event in pygame.event.get():
                            if event.type ==pygame.KEYDOWN:
                                if event.key==pygame.K_o:
                                    paused=False
#===================================================================================================================



        gamedisplay.fill(grey)
        snake.snake_updater(leadx,leady)
        leadx+=speedx
        leady+=speedy
        head=img
        if speedx>0:
            head=pygame.transform.rotate(img,270)
        elif speedx<0:
            head=pygame.transform.rotate(img,90)
        elif speedy>0:
            head=pygame.transform.rotate(img,180)

        if leadx<0 or leadx>display_width-bsize or leady<0 or leady>display_height-bsize:
            gameon=False
        elif (leadx,leady) in snake.tail:
            gameon =False
        else:
            gamedisplay.blit(head,(leadx,leady))
            snake.drawsnake()
            pygame.draw.rect(gamedisplay,green,[apple.x,apple.y,bsize,bsize])
            #pygame.draw.rect(gamedisplay,red,[leadx,leady,bsize,bsize])
            if leadx==apple.x and leady==apple.y:
                snake.eaten(leadx,leady)

        gamedisplay.blit(font2.render('Score :'+str(snake.length),True,yellow),(0,0))
        pygame.display.update()
        clock.tick(FPS)
#================    END SCREEN   ============================================================================================
    while gameon==False:
        gamedisplay.fill((50,200,50))
        message(f"Game Over Your score {snake.length}",yellow,font1,-100)
        message("Lost",red,font2,50)
        gamedisplay.blit(retry,(100,400))
        gamedisplay.blit(game_quit,(500,400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x,y)=pygame.mouse.get_pos()
                ans=retryandquit(x,y)
                if ans=='retry':
                    gameloop()
                elif ans =='quit':
                    gameon=True
    pygame.quit()
    quit()

gameloop()
