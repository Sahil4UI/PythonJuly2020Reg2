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
movex = 3
 
while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(gameBoard,color,(x,y,w,h))
    x +=movex
    #pygame.draw.circle(gameBoard,color,(x+200,y+200),radius)
    #pygame.draw.line(gameBoard,green,(300,300),(300,500))

    pygame.display.flip() #update


