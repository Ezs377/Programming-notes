import tkinter

'''Events include:
<Button-1>, <B1-Motion>, <ButtonRelease-1>, <Double-Button--1>, <Enter>, <Leave>,
<FocusIn>, <FocusOut>, <Return>, <Key>, <Shift-Up>, <Configure>, <Activate>, <Deactivate>,
<Destroy>, <Expose>, <KeyRelease>, <Map>, <Motion>, <MouseWheel>, <Unmap>, <Visibility>
Using '<any key>' will also bind to that specifc key, for example, 's' will bind an event 
to the s key'''
# <Button-1> = When left mouse button is clicked. Use other numbers to represent other buttons on the mouse, e.g. <Button-3> will use middle mouse button
# <B1-Motion> = When the button is pressed and the mouse is moved around. Same number rule applies, where <B3-Motion> means middle mouse button 
# <ButtonRelease-1> = When the specified button is released
# <Double-Button--1> = When the specified button is double clicked. Can also use Triple click
# <Enter> = When the cursor enters the widget. NOT WHEN THE ENTER BUTTON IS PRESSED!
# <FocusIn> = When the mouse/keyboard is focused on the widget
# <FocusOut> = Opposite of above
# 

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