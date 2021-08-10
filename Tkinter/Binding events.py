import tkinter

class Main:
        
    def __init__(self, x):
        self.master = x
        self.frame = tkinter.Frame(x,
                                   pady=10,
                                   padx=10)
        self.frame.grid()
        
        self.text = tkinter.Label(self.frame,
                                  padx=10,
                                  pady=10,
                                  text="Press any keyboard button")
        self.text.grid(row=0,
                       columnspan=2)
        
        self.bindings() # Run the bindings code
    
    '''Bind keys to root not widgets'''
    def bindings(self):
        self.master.bind('a', lambda argument: print("A was pressed"))
        self.master.bind('w', lambda argument: print("W was pressed"))
        self.master.bind('s', lambda argument: print("S was pressed"))
        self.master.bind('d', lambda argument: print("D was pressed"))
        
        self.master.bind('<Key>', lambda argument: print("A random key was pressed"))
        
        self.text.bind ('<Enter>', lambda argument: print("In text"))
        

root = tkinter.Tk()
root.title ("Binding events")
run = Main(root)

root.mainloop()