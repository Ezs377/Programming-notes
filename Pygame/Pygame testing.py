'''Events'''
'''LOOK UP ENUMERATE FIRST'''
import pygame, sys
pygame.init()


# While loop is still going i.e. program is still running
while loop == 1:
    # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If Pygame detects program shutdown
            loop = 0
    
    '''Do stuff here'''

print ("done") # Indicate finish