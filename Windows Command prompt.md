## Windows COMMAND PROMPT
### Command line basic commands (command prompt/Git): 
`cd` = Shows or changes the current directory  
`cls` = Clears the screen  
`cmd` = Restart command prompt  
`color` = Changes console color. Utilises 2 hexadecimal digits, the first is for the background, the second is for the text color. Hexadecimal digits ascend from 0 - 9, then ascends through A - F.  
`comp` = Compare two files  
`copy` = Copies files to another location  
`date` = Displayed current date, can be changed  
`del/erase` = Deletes files  
`dir` = Displays list of files and folders in a directory  
`echo` = Used to display written text or display inputted commands  
`exit` = Close command prompt  
`fc` = Compares files and displays differences  
`find` = Find a specified text string within files  
`findstr` = Find specified strings within files  
`help` = Lists all commands  
`help` (followed by name of command) = Gives more detail about command  
`md/mkdir` = Make a new directory  
`move` = Move files between directories (cut and paste)  
`path` = Displayed or searches for exe files  
`pause` = Stops current command  
`print` = Print a text file  
`time` = Displayed current time, can be changed  
`title` = Sets command prompt window title  
`tree` = Displays a graph of current directory path  
`type` = Display contents of a text file  
`ver` = Displays windows version 

### Changing directories:
1. Type main drive (`C:` or `D:` depending on your computer).
2. Alternatively type `cd`, followed by `/D`, followed by a drive, followed by directory path to immediately move drives and directories. A directory path typically looks something like `d:/EZ/download/Git`.
3. Use `cd` to navigate files/folders, by using slashes (\/) to separate folders. For example, `cd D:/download/Git` will first navigate to D drive, then to the `EZ` folder, then to the `download` folder, and finally the `Git` folder. 
4. Use `dir` to view files in a folder. For example, `dir Git` will show all files in that folder.
5. Use `cd..` to move back to previous folder/directory.
6. For files and folders that have a space in the name, use quotation marks ( " " ) to enclose the full name. For example, to navigate to the folder `Speeding camera assessment` the path would be `cd "Speeding camera assessment"`

### Using prompt for Python:
Set directory path to Python folder (E.g. `D:\EZ\Download\Python`). Then python commands are available. Python files can be opened by typing the name of the file as long as it is in the current folder. Use speech marks ( “ “ ) to close the full name of the file to run it, otherwise the command prompt will read the first word only and will raise an error. For example, to run the Python file `My calculator`, it will need to be typed as `“My calculator.py”` in the command prompt to run it within the command prompt. It is also possible to simply type `python` in the command prompt line to start a python IDLE, as long as Python is recognized on the PATH variable. 

### PATH environment variable:  
The PATH variable is an environmental variable that Windows uses to make navigating files easier for the system. Basically, when installing software or apps that aren't part of the original Windows system (e.g. art programs) Windows will try to put the main executable file (the program that runs) on PATH. PATH variables usually involve a direct pathline to the executable of a program, e.g. `C:/Users/EZ/Downloads/Illustrator/Illustrator.exe`. This lets Windows instantly navigate to the executable file of a program, instead of looking for the correct exe file to run. You can add programs to the PATH environment by using the Windows advanced settings, or using command prompt directly (although this involves some tricky code). And putting programs on the PATH makes it easier for Windows to find them, and easier for you to search for them. Sometimes putting programs on PATH is necessary for other programs to work properly (e.g. Putting Python on PATH is necessary for Wing IDLE to run Python).

