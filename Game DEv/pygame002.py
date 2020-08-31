#importing the pygame
import pygame
#pygame initialization
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

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
 
while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(gameBoard,color,(x,y,w,h))
    x+=movex
    y+=movey

    if x>width-w:
        movex=-3
    elif x <0:
        movex=3

    if y>height-h:
        movey=-3
    elif y<0:
        movey=3
    
    #pygame.draw.circle(gameBoard,color,(x+200,y+200),radius)
    #pygame.draw.line(gameBoard,green,(300,300),(300,500))

    pygame.display.flip() #update
