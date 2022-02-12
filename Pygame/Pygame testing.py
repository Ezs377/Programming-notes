'''FOR PYGAME TESTING'''
'''LOOK UP ENUMERATE FIRST'''
import pygame, sys
pygame.init() # initialize Pygame

'''Variables'''
screen = pygame.display.set_mode((600, 600))
bg_color = (0,0,0)

clock = pygame.time.Clock()

screen.fill(bg_color)


# While loop is still going i.e. program is still running
while True:
    # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If Pygame detects program shutdown
            sys.exit()
            
        
    
    '''Do program testing stuff here (e.g. drawings)'''
    
    

    clock.tick(10)
    screen.fill(bg_color)
    
    
 
    
    pygame.display.update()
    
print ("done") # Indicate finish