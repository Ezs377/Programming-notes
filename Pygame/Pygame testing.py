'''Animation time!!!!'''


import pygame
pygame.init()

loop = 1 # For looping program
screen = pygame.display.set_mode((700,700)) # Set display Surface, with width and height tuple size
color = (5, 5, 5) # Color RGB tuple, represents a RGB color value
color_line = (255, 100, 100) # Color RGB tuple for line drawing
color_rect = (100, 255, 100) # Color RGB tuple for rectangle drawing
color_circ = (100, 100, 255) # Color RGB tuple for circle drawing
color_arc = (100, 100, 100) # COlor RGB tuple for circle drawing

def point (x, y):
    return (x, y)
x = 0
y = 0

# Fill screen display Surface
screen.fill(color)


while loop == 1: # Pygame loop
    for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        if event.type == pygame.QUIT:
            loop = 0
    if x or y != 700:
        x += 2
        y += 1
    
        
    pygame.draw.lines(screen, color_line, False, [point(x,y), point(x+1,y+1)], 4)
    
    pygame.display.update() # Call this for every edit to the screen (e.g. Animations)
    


print ("done")