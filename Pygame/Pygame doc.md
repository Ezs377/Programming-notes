# Pygame module

Pygame is a module created for Python to generate a game with Python programming. `pygame.init()` initializes Pygame and allows the pygame module to run within the program. THere are several modules available within Pygame:
- `cdrom`: Lets you access the CD and DVD drives of a computer to load things, such as audio recordings and etc. Outdated  
- `cursors`: Lets you use and display cursors in your program for any purpose, such as menu selection  
- `display`: Lets you create a display (screen) for your game. Called a 'surface' by Pygame, this is where you display your game to the user  
- `draw`: Lets you 'draw' shapes onto a surface (display)  
- `event`: Lets you manage events and the event queue    
- `font`: Lets you create and render custom TrueType fonts for your program  
- `image`: Lets you save and load images  
- `joystick`: Lets you use a joystick in your game  
- `key`: Lets you bind events to keyboard buttons and perform other functions with the keyboard  
- `mouse`: Lets you bind events to the mouse movement and state and perform other mouse functions  
- `sndarray`: Use the NumPy module to convert Sound objects with a NumPy array. Allows manipulation of sound values and functions to manipulate sound  
- `surfarray`: Use the NumPy module to convert pixels to a NumPy array. Allows manipulation of image pixels and colours.  
- `time`: Lets you handle program timings in milliseconds  
- `transform`: Lets you manipulate images and sprites on the display. Note that some data can be lost if an image is resized over and over, resulting in a more blurry image  

### Steps to start with Pygame:  
1. Import pygame. This can be done by simply writing `import pygame` in python. Note that Pygame has to be installed in order to use it, you can install it using pip and command prompt. If the `import` command doesn't run in your python window, then Pygame probably isn't installed.  
2. Use `pygame.init()` to initialize Pygame functions and modules. This ensures everything is up and running for Pygame. If an error occurs that means either that function/module is uninitialized, or not installed, which measn you need to re-install Pygame. Using `pygame.get_init` will return either True or False, and determines if Pygame is fully initialized or not.  
3. To create a display, use `pygame.display.init()` to initialize a display. A display is referred to as a Surface by Pygame. A display sets the coordinates of (0,0) at the **top left** of the screen. So X=0 and Y=0 when at the top left of the display, like a tkinter canvas. Only one display be opened by Pygame at a time.
