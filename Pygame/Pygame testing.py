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
counter = 0

pointlist = [(100, 100), (450, 100), (450, 450), (100, 450)]

x = pointlist [counter][0]
y = pointlist [counter][1]

coordinates = (x, y)
size = (50, 50)



while loop == 1:
    for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        if event.type == pygame.QUIT:
            loop = 0
    
    # Grid lines
    pygame.draw.lines(screen, (100, 255, 100), False, [(100, 0), (100, 600)], 1) # Left vertical
    pygame.draw.lines(screen, (100, 255, 100), False, [(450, 0), (450, 600)], 1) # Right vertical
    pygame.draw.lines(screen, (100, 255, 100), False, [(0, 100), (600, 100)], 1) # Upper horizontal
    pygame.draw.lines(screen, (100, 255, 100), False, [(0, 450), (600, 450)], 1) # Lower horizontal
    
    clock.tick(10)
    if x != pointlist[counter+1][0]:
        x += 5
    
    
    
    coordinates = (x, y)
    
    screen.fill(color)
    pygame.draw.rect(screen, rect_color, (coordinates, size), 0)
    
    pygame.display.update()

print ("done")