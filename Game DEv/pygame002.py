#importing the pygame
import pygame,random
#pygame initialization
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

snakeImg = pygame.image.load("snake.png")
snakeImg = pygame.transform.scale(snakeImg,(100,100))
#R(REd)G(Green)B(blue) FORMAT -> 0-255
red = 255,0,0
blue = 0,0,255
green = 0,255,0
black = 0,0,0
white = 255,255,255
color = 150,50,150
x=0
y=0
w=70
h=70
radius = 100
movex = 0
movey = 0

gameSound=pygame.mixer.Sound('point.wav')
#-1 for infinite times
gameSound.play(-1)

while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movex=random.randint(1,10)
                movey=0
            elif event.key == pygame.K_LEFT:
                movex=-random.randint(1,10)
                movey=0
            elif event.key == pygame.K_UP:
                movex=0
                movey=-random.randint(1,10)
            elif event.key == pygame.K_DOWN:
                movex=0
                movey=random.randint(1,10)
    pygame.draw.rect(gameBoard,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(x,y,w,h))
    gameBoard.blit(snakeImg,(0,0))

    x+=movex
    y+=movey

    

    if x>width-w:
        movex=-random.randint(1,10)
    elif x <0:
        movex=random.randint(1,10)

    if y>height-h:
        movey=-random.randint(1,10)
    elif y<0:
        movey=random.randint(1,10)
    
    #pygame.draw.circle(gameBoard,color,(x+200,y+200),radius)
    #pygame.draw.line(gameBoard,green,(300,300),(300,500))

    pygame.display.flip() #update
