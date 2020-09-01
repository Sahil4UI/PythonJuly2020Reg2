#importing the pygame
import pygame,random
#pygame initialization
pygame.init()

width = 1000
height = 500


frogImage = pygame.image.load("frog.png")
frogWidth = frogImage.get_width()
frogHeight = frogImage.get_height()

sound = pygame.mixer.Sound("point.wav")

gameBoard = pygame.display.set_mode((width,height))

#R(REd)G(Green)B(blue) FORMAT -> 0-255
red = 255,0,0
blue = 0,0,255
green = 0,255,0
black = 0,0,0
white = 255,255,255
color = 150,50,150
gameBg = pygame.image.load("StartBackground.png")
gameBg = pygame.transform.scale(gameBg,(width,height))
def homeScreen():
    msg = "PRESS 'SPACE' to Start the Game"
    font = pygame.font.SysFont(None,60)
    #text = font.render(TEXT,ANTILIASING Property,COLOR)
    text = font.render(msg,True,red)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainGame()

        gameBoard.blit(gameBg,(0,0))
        gameBoard.blit(text,(50,450))
        pygame.display.flip()            
    
def mainGame():
    x=0
    y=0
    w=50
    h=50
    movex = 0
    movey = 0

    frogX = random.randint(0,width-frogWidth)
    frogY = random.randint(0,height-frogHeight)
    

    while True:
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    movex=5
                    movey=0
                elif event.key == pygame.K_LEFT:
                    movex=-5
                    movey=0
                elif event.key == pygame.K_UP:
                    movex=0
                    movey=-5
                elif event.key == pygame.K_DOWN:
                    movex=0
                    movey=5

        gameBoard.fill(white)
        gameBoard.blit(frogImage,(frogX,frogY))
        myRect = pygame.draw.rect(gameBoard,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(x,y,w,h))
        frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
        x+=movex
        y+=movey

        if frogRect.colliderect(myRect):
            frogX = random.randint(0,width-frogWidth)
            frogY = random.randint(0,height-frogHeight)
            sound.play()
            

        

        if x>width-w:
            movex=-5
        elif x <0:
            movex=5

        if y>height-h:
            movey=-5
        elif y<0:
            movey=5
        
       

        pygame.display.flip() #update


homeScreen()
