import tkinter

# If possible implement menu with eraser
class Main:
    def __init__(self, x):
        self.frame = tkinter.Frame(x,
                                   pady=10,
                                   padx=10)
        self.frame.grid()
        
        self.canvas = tkinter.Canvas(self.frame,
                                     height = 1000,
                                     width = 1000)
        self.canvas.grid(row=0,
                         column=0)
        
        self.canvas.bind ('<Button-1>', self.getcoords)
        self.canvas.bind ('<B1-Motion>', self.draw)
    
    # Get coordinates of current mouse position. This is just for the start when the mouse is pressed
    def getcoords(self, event):
        self.lastx = event.x
        self.lasty = event.y
    
    # Draw a line, using the previous mouse position, to the current mouse position. Continously updates itself
    def draw(self, coords):
        
        # | Starting x point | Starting y point | Draw to x point | Draw to y point |
        self.canvas.create_line (self.lastx, self.lasty, coords.x, coords.y, width=5, fill='black')

        self.lastx = coords.x
        self.lasty = coords.y                                       




root = tkinter.Tk()
root.title ("Sketchpad")
run = Main(root)
root.mainloop()