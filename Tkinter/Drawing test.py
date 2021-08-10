import tkinter

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
        
        self.canvas.bind ('<Button-1>', self.draw)
        self.canvas.bind ('<B1-Motion>', self.draw)
        
    def draw(self, coords):
        self.x = coords.x
        self.y = coords.y 
        self.canvas.create_rectangle ((self.x-1), (self.y-1), (self.x+1), (self.y+1), width=1, fill='black')




root = tkinter.Tk()
root.title ("Sketchpad")
run = Main(root)
root.mainloop()