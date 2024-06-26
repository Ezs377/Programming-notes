Terms:  
CS - Construction Set
TES - The Elder Scrolls
.esp - A common file extension for mod files or Elder Scrolls plugins
.esm - A common file extension for Elder Scrolls master files
OBSE - Script extender for Oblivion

## Starting out:  
#### First steps:  
1. In the main window, go to File -> Data, then tick `Oblivion.esm` then press ok

Object window: Contains all objects in the game including NPCs, buildings, items, etc. 
![[Pasted image 20240626180037.png]]  

Cell View Window: Contains a list of cells (i.e. Environments) for interior and exterior cells. For exteriors, cells are grid squares side by side. For interior, cells are a 3D container for building interiors.  
![[Pasted image 20240626180210.png]]  

Render Window: Dragging objects to the render window will display them. Also loads cells and displays them.
![[Pasted image 20240626180222.png]]  

### Main menu:  
Main Window: Has the menu and toolbar  
![[Pasted image 20240626180318.png]]  
The buttons are:  
1.  **Open File:** A shortcut for Data>File
2.  **Save:** Saves the active mod
3. **Preference:** Allows you to alter camera speed, rotation speed, etc
4. **Undo:** Undoes the last action (ctrl+z is the keyboard shortcut for undo)
5. **Redo:** Redoes the last undone action (ctrl+y is the keyboard shortcut for redo)
6. **Snap to Grid:** When activated snaps objects to the invisible cell grid
7. **Snap to Angle:** When activated snaps objects to a specific angle
8. **Worldspace:** Allows you to select a worldspace to view
9. **Landscape:** Turns on the landscaping tool (keyboard shortcut H to open)
10.  **Pathgrid:** Turn on the pathgrid tool. when active you can place and change pathgrid nodes, but you cannot move any static objects in the render window.
11. **Havoc Sim:** When turned on, it will simulate the game's havoc so will cause fires to burn and objects to fall in the Render Window.
12. **Worklight:** Toggles the worklight on/off in the Render Window (keyboard shortcut A)
13. **Sky:** Renders the sky in the exterior and in interiors where the lighting is set to behave like an exterior, can give you a better idea of how the scene will look in game, but can lag your rig so it's best left off most of the time.
14. **Leaves:** When on, renders leaves on the trees in the render window. When turned off, trees will appear bare in the CS, but in game the leaves will render. Turning them off is just to conserve resources.
15. **Questbuilder:** Opens the questbuilding tool. The Questbuilder is used to create quests and also to add dialogue to custom characters.
16. **Filtered Dialogue:** Opens the filtered dialogue feature that allows you to see what dialogue each character speaks. It can be useful for tracking down dialogue your NPCs are saying. Not used for creating dialogue.
17. **Script Maker:** This opens the script notepad where you can view existing scripts and create your own. (See our [Scripting Class](https://tesalliance.org/forums/index.php?/topic/831-class-1-the-basics-of-oblivion-scripts/) for information on creating scripts)
18. and beyond: **Main Menu:** These categories contain several more shortcuts to the various tools in the CS, many the same as what we've already reviewed; the most commonly used ones we've already explored on the tool bar.

### Basic controls:  
**Camera**  
Center Wheel Scroll - Zoom  
Center Wheel Hold - Move  
Shift + Mouse - Rotate  
C - Center On selected  
T - Top View selected  
Arrow Keys - Move the camera view Left, Right, Up and Down.  
  
**Object**  
D - De-select  
LMB - move: x, y  
Z + LMB move: z only  
X + LMB move: x only  
Y + LMB move: y only  
F - Fall  
CTRL x - cut  
CTRL c - copy  
CTRL v - paste  
CTRL d - copy and paste in present position (duplicate)  
LMB (with nothing selected) select multi-objects  
S - "Scale": drag mouse to edit size  
RMB + z  rotate about z  
RMB + y  rotate about y  
RMB + x  rotate about x  
  
**Misc**  
A - Toggle Bright Light  
M - Toggle Markers On/Off  
B - In Exterior Toggles Cell Grid Borders On/Off  
H - Opens the landscape editor  
L - Toggle the Light Object Radius On/Off

In the object list we can search by clicking in the object list and pressing a letter. Somehow it works, to reset the search click somewhere else.

### Make a new cell:
1. To make a new interior, right click on an existing interior cell in the cell view window, and click edit
2. Right click on the window that pops up and click new
3. Make a name for the interior cell ID, should NOT start with numbers
4. The three tabs on the right are Common Data, Lighting, Interior Data. Lighting sets the lighting colors, Interior Data sets the name of the cell and the owner of the cell (select Player to own it, select Player Faction to allow companions)
5. The cell should show up in the Cell View window list
6. Select an interior object from the object window and drag to the render window to display it. Something should pop up.  

Double clicking an object in the render window will bring up the reference window.  
![[Pasted image 20240627000730.png]]  
This allows us to change the objects x/y/z positions, rotation, disable/enable, scale, and etc. Works for any object that is double clicked in the render window.  

We should always zero the first object in the interior, to make things easier, by setting all positions to zero.  

Can double click the object in cell window content list to move camera to that object.  
![[Pasted image 20240627001310.png]]  

### Putting objects:  
Camera tips:  
- Holding shift will let you rotate the camera without affecting the object by moving the mouse around
- Holding the respective dimension key (i.e. x, y, z) and dragging it will move the object only in its respective dimension. Otherwise it moves relative to the current view
- Ctrl+z does an undo on the last movement done with the camera, although redo seems to be broken
- Pressing F will drop down the object to ground level (i.e. The first surface it touches in Y direction) so be careful not to drop in open space as it will likely crash
- Holding S key and dragging scales the object
- The C and T key will focus on the object, C centers as third person view, T centers as top view
- If an object is too far from the desired position it may be helpful to use the reference window by double clicking and manually setting coordinates.
- Pressing D deselects objects

Example:  
![[Pasted image 20240627002809.png]]  
For chairs the outlines indicate the character model positions and sizes, make sure it doesn't interfere with any objects. Note that for usable chairs it should be taken from the Furniture label in the object menu, not Static.  

For fires they are rendered sideways on X axis by default.  

## How to install mod:
To use our custom stuff it is treated as an .esp file with our mods. To use the mod:  
1. Make sure .esp file is in Data folder of Oblivion folder
2. Open Oblivion through the launcher instead of exe. The launcher exe should be in the Oblivion folder.
3. Go to Data Files, and tick the .esp file of the mod







