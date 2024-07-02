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
Space + Mouse - Pan
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

### Oblivion items:  
![[Pasted image 20240628001115.png]]  

**Duplicating:**  
To copy and paste items, ctrl+click to select multiple objects (or drag and select). 

Pressing ctrl+d will duplicate all selected objects, and automatically set the selection on the duplicated items, so clicking and dragging the objects will move the duplicates. NOTE that the duplicated objects will superimpose themselves on the existing objects so needs to be clicked and dragged out.  
![[Pasted image 20240701220227.png]]
Alternatively ctrl+c and ctrl+v works as well.  

### Containers:  
For player containers (i.e. Items stay permanently) use containers with a PC prefix.  

Double click the container to edit its base contents and ID. ALWAYS change the baseID first before making a custom container, as editing a container will change all existing containers in the world. Once baseID is changed then accept the option to create a new form.  

The `Edit Base` option in the reference window brings up the container's default items and status.  
![[Pasted image 20240702000920.png]]  
The list on the right shows all items in the chest. 

To add items to a container find the item in the object window, then drag into the container list.  

### Pathgrids:  
Pathgrids tell NPCs where they're allowed to move. Use the pathgrid option in the navigation menu to start.  
![[Pasted image 20240702010840.png]]  
Use right click to place red nodes, and ctrl+right click to add a connected node. Left click selects nodes, where we can move them, delete them, etc. We can also connect nodes with a path by using ctrl+left click when not placing new nodes. Note that this connects a path from the clicked node to the active node, which is the previously selected node.  

A node indicates a safe spot for NPCs to stand in, and a path between nodes tells the NPC they can move along the path. Multiple paths can connect a node to others. 

In exteriors, path grids come in 3 different nodes:  Blue, orange, red. 
- Blue nodes are important nodes and NPCs will prioritize following these nodes (ONLY IN EXTERIORS). Ideally minimize the amount of blue nodes, and don't delete existing blue nodes  (just move them)
- Red nodes are medium importance and NPCs will follow them sometimes
- Orange nodes are auto generated and have the lowest priority




### Exteriors:  
Exterior cells represent the whole world. The main worldspace is the Tamriel exterior cell, which represents the land. Child worldspaces are smaller worlds, such as city interiors which aren't interior cells but another cell used for exteriors. Editing objects in a worldspace will cause it to show up.  

Be careful to note where existing objects are in an exterior cell, since the land is comprised of grids of exterior cells.  

Exterior cells can be selected in the cell view window by switching to another cell other than the Interior type. Note that child worldspaces are considered their own exterior cells, the Tamriel exterior cell is the one we want.  
![[Pasted image 20240702121319.png]]  
Ideally rename the desired cell grid so we don't have to navigate by grid coordinates each time. This is done by clicking on the editor ID name when already selected (like an interior cell). NOTE, exterior Tamriel cells that are named Wilderness are safe to use, but if it isn't then it could potentially disrupt existing objects. Naming cell IDs doesn't affect the actual game but it helps to keep track of our work.

Also note that using arrow keys on the camera causes it to navigate to the next neighboring cell instead of panning the camera for some stupid reason. And note that interacting with objects outside the selected exterior cell will cause the cell view to move to that cell.

Press B key to show grids of cells. This shows the boundaries of each exterior cell in the selected coordinate. REMEMBER: Exterior cells are shown as a bunch rather than one by one, the grids help keep the objects within the same cell. 

Purple regions represent water in the exterior cell view.  
![[Pasted image 20240702133213.png]]
Aside from that the exterior cells operate in the same manner as interior cells for placing objects and etc.

We can disable objects by double clicking and ticking 'initially disabled'. This stops them from being drawn in the world but keeps them there as a reference for later use if needed.  

### Landscaping:  
Altering the terrain land is different from objects. 

Press the H key to bring up the landscape editor or press the landscape button on the menu.  
![[Pasted image 20240702144311.png]]  
![[Pasted image 20240702144359.png]]  

The edit radius determines the size of the our landscape paintbrush. We can hold and drag to either raise/lower terrain within the paintbrush. Flatten and soften vertices options will change the behaviour to whatever is selected, flatten will make the land flat, soften will smooth out the land.  

Roughly a radius of 2 is enough to form a basic path width when reducing terrain. 

Right clicking with the landscaping tool will paint the chosen texture from the texture list onto the terrain. The max opacity determines how visible the texture can be (note, this is not from one right click, but the max opacity if the texture is layered multiple times). 

Pressing the I key when the edit radius is over terrain brings up the terrain info.  
![[Pasted image 20240702155252.png]]  
There can only be a maximum of 9 different textures used in each quad (each exterior cell is divided into 4 quad regions). If the amount of textures exceeds 9 then we get janky textures. 

The dominant texture is the texture listed at the top of each quad list and the dominant texture covers the most terrain in that quad. NEVER delete the dominant texture otherwise we get a black texture. If we get the black texture error it is mostly unrecoverable.  

If a quad is full on textures then we can delete the texture at the bottom of the list to see if it helps. 

### Map marker:
The map marker object from 'Static' world objects can set the fast travelling location on the map, and allows the player to fast travel to the location where they will teleport on the map marker during fast travel. The map marker also lists the location details. Double click to edit location details.  
![[Pasted image 20240702153315.png]]  
- **Name:** Is the name that appears when you get close to the marker in game as in '*You have found Bogwater Burrow*'
- **Type:** Tells the game what sort of place this is so it gets the proper icon on the map  
- **Visible:** When flagged will make the marker visible on the map even if you never found that place before. (Unchecked and it will be invisible until the player "finds" the location)  
- **Can Travel To:** When flagged you will be able to fast travel to this location even if you didn't find it first.

Note this makes a reference for the object, and hence we won't change other objects of the same type by editing this marker. Double clicking always opens up the reference window, it's when we alter base IDs that we have to be careful.  

### Doors:  
Door objects (under World objects) have a built in Teleport property under their reference window. This allows us to set to the destination cell when the door is activated. There's also a Lock tab that lets us lock doors with a lock level.  

However, door linking will only link to other door world objects of the same type. In the test example I put another farm type door for the interior house so we can only link to that.  
![[Pasted image 20240702154605.png]]  
We can also select the reference manually by double clicking it in the render window after pressing 'Select Reference in Render Window'. We can also click 'View Linked Door' to see the door it is linked to, and also click 'View Teleport Door' when in the interior to see the door that teleports to that interior.  

The door marker, 
![[Pasted image 20240702154903.png]]  
which appears when a door is successfully linked, will show the direction of the player when they 'exit' the door. The pink arrow indicates the direction the player is facing when exiting the door. The door marker essentially indicates where the player would be placed at when exiting the door.  






### Grass:  
Grass isn't rendered in the render window, but will appear on textures in game. This makes it difficult to pinpoint which textures are causing grass to clip through our objects in the exterior cell. 

To find grass we might have to take a screenshot of the object in game to determine where it is. Then we can use a texture with no grass, and layer it over areas we don't want any grass in. Usually every texture has two versions, one with grass and one without, and usually the non-grass version has 'NoGrass' in the texture ID.
![[Pasted image 20240702210918.png]]
There are also specific unique textures that have no grass.  

Set the max opacity to 100% when layering a non-grass texture, as this prevents the existing grass from clipping through.  

Using ctrl+right click will give the terrain type that we are clicking, so it can be useful to find what texture is currently on the terrain so we can use the no grass version.

### Grid snapping:  
Ideally we would turn on grid snapping at the start of making a new cell to ensure all objects are set on the grid properly. Also set the first piece in an interior cell to 0 in all dimensions (x, y, z, rotations).  

Holding a dimension key (i.e. x, y, z) while dragging an object will only move the object along that axis. So it can be useful when using the snap grid and duplicating objects.  

### Lighting:  
The ambient lighting will set an overall 'hue' to the interior cell. We can adjust it to get a different feel using the lighting.  


## How to 'install' mod:
To use our custom stuff it is treated as an .esp file with our mods. To use the mod:  
1. Make sure .esp file is in Data folder of Oblivion folder
2. Open Oblivion through the launcher instead of exe. The launcher exe should be in the Oblivion folder.
3. Go to Data Files, and tick the .esp file of the mod

Also, when you want to edit the same mod, tick the .esp plugin file with the mod when opening a file in TES construction set so the construction set doesn't make a new mod. Then click "Set as Active File" to ensure (note the .esm file must also be selected).  









