'''Events'''
'''LOOK UP ENUMERATE FIRST'''
import pygame, sys
pygame.init()

loop = 1
screen = pygame.display.set_mode((600, 600))
color = (0, 0, 0)
rect_color = (255, 100, 100)
clock = pygame.time.Clock()
screen.fill(color)

pointlist = [(100, 100), (450, 100), (450, 450), (100, 450)]

x = 100
y = 100

coordinates = (x, y)
size = (50, 50)

counter = 0


while loop == 1:
    for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        if event.type == pygame.QUIT:
            loop = 0
    
    coordinates = pointlist[counter]
    counter += 1
    if counter == 4:
        counter = 0
    
    screen.fill(color)
    pygame.draw.rect(screen, rect_color, (coordinates, size), 0)
    
    pygame.display.update()

print ("done")