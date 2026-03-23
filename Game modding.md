# Oblivion
Terms:  
CS - Construction Set
TES - The Elder Scrolls
.esp -

A common file extension for mod files or Elder Scrolls plugins
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

Basically, the worldspaces are divided into their own cells, exterior cells are designated as part of the land grid, however all interior cells are grouped as part of the 'Interior' worldspace. Hence we need to edit the 'Interior' worldspace first, then add a new interior cell.

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


### NPCs:  
NPC actors are found in the 'Actors' section of the object window.  

To make a new NPC, right click in the NPC actors list and select New.  
![[Pasted image 20240704011507.png]]  
For the NPC ID it can anything, but cannot start with numbers. Note that Name is the NPC's game name, not ID.  

The Class is for the NPC type, for NPCs we don't want Charactergen as this is for the player. Instead pick something else, the class will dictate the NPCs role and their stats and attributes (like a player's class). It is also possible to make a custom class.

The 'Auto calc stats' tickbox will auto-generate the NPC stats based on its class and level.  

For factions we can add them by dragging from the faction window, which is found in the Character tab in the main menu:  
![[Pasted image 20240704012747.png]]  
Player faction is the faction that is allied with the player, use this for allowing friendly NPCs.  

The Stats tab allows us to edit the stats and attributes of the NPC. 
The Factions tab allows us to put the NPC into a factions.
The Inventory tab allows us to drag item objects to place them in the NPCs inventory. In particular, the first given clothing and armor objects are automatically equipped.
The SpellList tab allows us to give the NPC spells.
The Animation tab sets the animations of the NPC (complicated).
The Face and Face Advanced tabs let us change the appearance of the NPC's head.

To add items to the NPCs default inventory simply drag and drop objects like containers. The same applies with spells (which are also found in the object window). For spells, standard spells are safe to use (under the 'Spell' --> 'Spell' sub category).  

Placing an NPC is the same process as placing a world object.  

### NPC packages:  
An NPC package acts as its basic AI script and lets the NPC do stuff. Packages are found in the character menu,  
![[Pasted image 20240705140619.png]]  
The package window gives a set of actions and conditions we can use and customize.  
![[Pasted image 20240705161113.png]]  
Right click to either select New or Edit to make a new package or edit an existing package.  
![[Pasted image 20240705161140.png]]  
Here we have a bunch of NPC actions and package type. 
The Package Type determines the action of the NPC if a condition is met. 
The Schedule sets the time and duration of the NPC action in hours (i.e. The possible times the NPC will do the action). Note that time indicates the hour of the clock, duration is how long the action is performed for in hours. Setting the time as Any will cause the package to run if no other package is running.

![[Pasted image 20240715114415.png]]  
The Location tab indicates the possible locations for the NPC action if ticked. The location can be set as either a nearby given reference object (using reference ID), within an interior cell (Cell), Any Object in the game world, or near the location of either itself or the editor location (it's original spawning location). With the near location setting we can set a radius that determines the trigger, which is in the same unit as the editor coordinates.  

![[Pasted image 20240715114524.png]]  
To apply packages to an NPC we can just double click the NPC in the Object window list and go to the AI tab.
![[Pasted image 20240715114552.png]]  
Aggression affects how likely an NPC will start a fight, higher values means they can start random fights.  
Confidence is how likely the NPC will flee from combat. Higher values means NPC is braver and won't run.  
Energy level is how often the NPC will move around when under the Wander action from a package.  
Responsibility is how likely the NPC will commit a crime or report a crime. Less than 30 means the NPC will steal things.

To add AI packages simply open up the package window for NPCs and drag/drop packages into the AI package list in the NPC window. Note that the order of packages is important, as the game will select the first available package to run.  

Conditions for the AI package are also available, given as standard IF statements.











## How to 'install' mod:
To use our custom stuff it is treated as an .esp file with our mods. To use the mod:  
1. Make sure .esp file is in Data folder of Oblivion folder
2. Open Oblivion through the launcher instead of exe. The launcher exe should be in the Oblivion folder.
3. Go to Data Files, and tick the .esp file of the mod

Also, when you want to edit the same mod, tick the .esp plugin file with the mod when opening a file in TES construction set so the construction set doesn't make a new mod. Then click "Set as Active File" to ensure (note the .esm file must also be selected).  


# Dying Light 1

**TLDR:** Use a file extractor (7-Zip recommended) to extract the data0.pak file located in the DW folder of the game provider's folder (e.g. For Epic Games it could be in D:\Epic Games\Dying Light\DW) and you will find most of the game data files within. Edit .scr and .xml files with Notepad or any text editor.

This guide contains my experience of amateur modding and information about useful things to mod. This guide doesn't delve into creating new objects or worlds and doesn't touch the devtools (from Steam) at all, focusing only on script and text editing. Do note that this is based on my experience and it might not fit the standard way of modding considering I couldn't find a lot of information online about modding Dying Light, and I never used Nexus Mods personally.
## File extraction:
Most of the game mechanics can be modded by editing the various data files in the game files. To access these, a file extractor is needed (recommended is 7-Zip). 

The data folder is located in the DW folder, which is typically located in the game provider's game data folders (e.g. For Epic Games, it is in Epic Games -> Dying Light -> DW). This is generally located on the D drive, where the game is installed. C drive only contains user data which doesn't affect much.

To extract files, 7-Zip can treat the extraction the same way as opening folders, so it's easy with 7-Zip. Otherwise, you'll need to manually extract the .pak files and store them as folders, then zip them back up as .pak files once finished, and replaced the corresponding .pak file in the DW folder. With 7-Zip you can also drag-drop files between the file manager and 7-Zip window, and it will automatically being them over without requiring you to manually extract them, and you can also drag-drop files from file manager to 7-Zip window.

The main data file is called Data0.pak which contains all the data (mostly). Definitely back up all the files before modding as some changes can crash the game. Data3.pak is also generally empty, but is often used by other modders to install their mods.

Within Data0.pak, there are several key files you can change which are listed below with their effects. Editing these requires Notepad (recommended) or a text editor equivalent. With 7-Zip right click and use the Edit option which automatically brings up Notepad provided it is on PATH. Recommended workflow is to copy all the files you want to edit into a folder and make copies of them for backup before editing. Then edit files manually with Notepad, then drag-drop it back to the 7-Zip window that is currently open with the folder the file is located in. Then overwrite the file to bring changes over. Don't rename files with this method. This also means you can revert changes using the backups if anything goes wrong.

If there is no backup and something goes wrong easiest fix is to use the "Verify files" option from the game provider, which should automatically reinstall the edited files to their defaults (this doesn't affect saves, just world data). Note this will remove all existing mods most likely.

## Performance:
The biggest boost to performance lies in the "scripts" folder, then the "*varlist_performance.scr*" file. Then edit the line `VarInt("i_shadows_sun_on", 1)` and make it 0 instead. It makes the game look bad though (everything is either super sunny or dark, minimal shadows) but improves performance a lot. You could also manually go through the other *"varlist"* files to set the settings up the way you want without having to set them in game (helpful if they keep getting resetted)

## Skills:
You can modify some attributes of skills by going to the "skills" folder. 
- "*common_skills.xml*" contains parameters of all the upgradable skills. In particular, you can add `<effect id="NageWazaFront" change="1"/>` to the "NageWaza" skill to let you push zombies forward alongside sideways and backwards. The other common parameter is XP gained during skill actions which can help level up much faster
- *"legend_skills.xml"* contains parameters for Legend skills, which takes a while to level up in the base game. Here you can edit the values for Legend skills such as the stat increases. For example, `<level_req type="Legend" value="20" active_at_skill_level="5"/>` means at skill level 5 you get a 20% increase in the given stat (although this may be just cosmetic text and not the actual stat). Stats come with unique parameters as well that affect the actual stat increase, for example `<effect id="LegendSkillArrowDamageMul" change="800.0"/>` increases the bow damage by 800% per level.
- *default_levels.xml* contains all the player stat data. This is the file to edit if you want to really affect the player character, such as speed increases, bow draw speed, running speed, ziplining speed, health, etc. You can also change the XP requirements for level ups which are all listed at the bottom. Other changeable effects include max ammo count (unverified), maximum fall height before damage, jump height, weapon handling modifiers (critical chance, accuracy, stamina cost), and throwing weapon range, speed, damage, lock on time, max targets (this is really nice for having automatic lock on by reducing the lock delay to 0).
- *buffs.xml* contains data of game buffs that can be applied to the character. Most notably the "IncreaseMoveSpeedInc" stat affects the speed boost, duration, and max stacks of the Kuai dagger effect. You can also alter the effects of potions and even put all effects into one potion instead. 

Final note, in the *default_levels.xml* file you can also change the inventory size. You can also change the quick slot size, but this doesn't affect the quick slot wheel, so you won't be able to find the items placed on quick slot except for the first four, otherwise you'll have to manually tap tab to cycle through the quick slotted items. These items are effectively "hidden" from the inventory menu as well, and resetting the quick slot amount will cause these items to be lost forever.

## Weapons and objects:
All weapons can be edited by going into "scripts" -> "inventory". Here all the files detail weapon data. There's a lot of data here which can take a while to go through. There are 3 versions of each file type here, namely the base, DLC, and gaas versions. Base files refer to content in the main game, DLC refers to DLC items (sometimes data from non-installed DLC appears, but can't use them) and gaas refers to special unique items, either from the base game or DLC (e.g. The Kuai dagger, Fenrir, etc). The following files below refer to the types of files, which can also have base, DLC, or gaas versions.

### Collectables:
The *collectables.scr* files appears to contain the craft plans for throwable items such as grenades and throwing stars, and some data on general collectables. Not sure if it does affect them, notably you can alter the recipe and the amount crafted per recipe. 

### Inventory
The *inventory.scr* file contains stat parameters for craftables, including grenades, ammo, weapon mods, etc. Notably, `throwable_explosive_grenade` refers to the DIY grenade item which can be used as a baseline for testing the stats of other throwables. You can change the damage, area damage range, max stacks, explosion delay, etc. You can also change the throwing range/speed of the throwable with the `ThrowImpulseLook()` stat, where higher = further. `ThrowImpulseUp()` also does something but idk.

### Inventory gen
The *inventory_gen.scr* file contains all data parameters for all the weapons in the base game, with *inventory_gen_dlcXX.scr* corresponding to a DLC (XX is a number which may be different across versions) and *inventory_gaas.scr* for gaas versions. This contains ALL weapons, including their variants. So good luck finding which weapons are which, since they're all named generically. Parameters are listed in subsections for both melee and firearms, but with different effects:
- For melee, the parameters for a weapon object are given as base, damaged, broken. This refers to the stats of the weapon when it is in good condition, in bad condition, and fully broken. The important parameters are only in base, the damaged and broken stats don't affect much except the HUD and appearance of the item, however you can add other parameters for these sections to give weapons a new feel.
- For firearms, the parameters of the weapon object are given as base and recoil. The base affects the usual stats, and recoil affects the recoil pattern? Not too sure but the recoil section might actually affect the recoil when the weapon is aimed.

Notable weapon objects to use:
- Bekir's machete: The weapon appears in the Following DLC in the second(?) mission (the water pump level), but is easy to use as a reference since it is also called Bekir's machete in the files so you can easily navigate to it. Other unique weapons include Tahir's machete, Arena machete, and Rai's gun.
- `Firearm_PistolAGen` and `Firearm_PistolBGen` refers to the base American and German pistol respectively. Note this is for the base weapons, so variants like the composite pistols aren't affected. Likewise `Firearm_RifleAGen` and `Firearm_RifleBGen` refers to the base Police rifle and Military rifle respectively. I dunno about shotguns and SMGs since I didn't do much with them.

For weapon stats, the easy stats to change across all weapons is the damage. 
- **For melee weapons, the following stats are helpful:**
	- `condition` = Amount of hits before needing to be repaired
	- `damage`= Self explanatory (note this is multiplied by legend stats as well)
	- `force` = Seems to affect the impact force of the weapon (i.e. How far zombies go when you smack them)
	- `criticalprob` and `criticaldamage` = Probably affects critical hit chance and damage, expressed as percentage (i.e. 1.00 = 100%)
	- `damagetophysicsobjects` = Could be the damage done to the environment, e.g. Detonating gas tanks
	- `staminausage` = self explanatory
	- `headcutprob` and the others (arms and legs) = Affects chance of cutting these limbs when damage is high enough. Note that head has 2 parameters: `smash` and `cut` which cannot happen at the same time. Stats are expressed as percentages (1.00 = 100%)
	- `damagetype` = Determines the damage effect used when hit. This can be changed so that "axe" attacks can be applied to swords, which makes it much easier to slice zombies, or give sword attacks to baseball bats. Reference other weapons to see the available options (e.g. Axes tend to use the `CutTypesGroup_SharpHeavy` attribute)
	- `flags` = Refers to the weapon object subsections mentioned before. Don't change unless you wanna add more or remove some but be careful.
	- `inventorymeshhq` and `inventorymesh` and `mesh` = Affects the weapon skin. You can change it up to get other weapons looking like other weapons, from what I got you should keep the mesh the same for both parameters. Use .msh options for the mesh, you can refer to other weapons for their meshes.
	- `skin` and `skintag` = Affects the variant of the skin, e.g. Flamboyant versions of the knife mesh. Dunno what options are available, you'll need to go through other weapons and experiment. Not all meshes have skins either.
	- `animprefix` = Affects the swing animation of the weapon. You can basically make a knife swing like an axe and etc. Refer to other weapons for their animations, but remember that this only affects the animation not the appearance (e.g. Machete with axe animation makes the player grab the machete blade with two hands like the axe). Note: This might  also affect the skills attributed to the weapon, e.g. Axe animation makes the weapon have the ability to ground pound (but sometimes it doesn't work so idk).
	- `twohanded` = Seems to affect whether a weapon is two handed or not, dunno what it does really but change it to match the animation just in case.
	- `reparable`, `repairpart`, and `allowedrepairs` = Affects the ability to repair the weapon, `reparable` determines if the weapon can be repaired, `repairpart` determines the parts used to repair, `allowedrepairs` determines the amount of repairs possible
	- `achtype` = NOTE: Regarding weapon animations, this might also affect it so if you switch to a different weapon animation match this too. I forgot if it does affect it but it might.
	
	Aside from these you can also change the sound effect played when hitting stuff (again, refer to other weapons for their sounds) and change the parts given when dismantling and the weapon prices. Also, you'll notice that damaged weapons have their own meshes which might help for more customization.

- **For firearms, the following stats are helpful:**
	- `headsmashprob`, `headcutprob` and etc = Same as melee, along with the other same named parameters. Notably though, changing the mesh and animations seems to crash the game but maybe that was another issue.
	- `shottime` = Affects the delay between shots. Don't make it too short otherwise you can literally dump the entire magazine in 0.1 seconds, around 0.02 is a good delay for rifles.
	- `shotsound` = Affects the sound effect for shots, not fully tested
	- `ammocount` = Amount of ammo before reloading
	- `reloadtime` = Actually useless, it makes the animation faster but not the overall reload time so you just get static animations while waiting for the full reload delay
	-  `shootstatsaccuracy`, `shootminangle`, `shootmaxangle` and etc = Affects the recoil pattern of hipfire shooting(?) not fully tested.
	- `shootmode` = Affects shooting type, comes in single, automatic, burst modes (use other guns to get exact attributes)
	- `bulletspershot` = Amount of bullets shot out per shot, usually used for shotguns but you can alter it in other guns too. Doesn't affect the amount of ammo used, just the amount of bullets that come out.

### Inventory gaas:
Special mention, the *inventory_gaas.scr* is similar to *inventory_gen.scr* but lists unique weapons. Notably, since the weapons are unique it's pretty easy to find the parameters for those weapons, however they're still named with generic names. This also means you can use them to play around with meshes and etc.
- `firearm_gaas revolver` = The last wish revolver, which is the one that shoots an explosive round on the last bullet (I actually never got this one but I assume it to be the same)
- `gaas_shortknife` = The Kuai dagger, which gives you a speed boost when you perform parkour actions with the knife out. 
- `gaas_axe` = Fenrir axe which does more damage for cutting limbs(?)
- There's also the Zaghnal which I didn't realize until I found out it was referred to as the lost invention so I never got around to using it oops 

### Inventory special:
The *inventory_special.scr* file contains data for unique items such as developer items (e.g. Korek machete) and event items. Some of them are have different stats and parameters to the usual items, but mostly are the same. Some developer items are not named which can make it harder to locate them ingame. Unlike other items both the stats and craft plans of items are both included in this file, typically in format of stats, craftplan, so don't confuse items with craftplans when editing. They also combined a lot of other stuff for items so there's quite a few unknown effects and parameters. For example, the Airstrike developer item (in the game it's a flare you throw which spawns a small missile that blows up the area) has the parameters for the flare effect AND the explosion generated, as well as the stats of a throwable (impulse, delay, etc). So yeah some experimentation needed.

### Tricky weapons:
The *tricky_weapons.scr* file has some details on certain DLC weapon effects (mostly Hellraid DLC) idk if it affects anything since I never got any DLCs

## Other notes:
I couldn't find a way to directly change stats of weapons you own in-game, mostly because that requires the save data which is NOT stored in the data0.pak file, and the only save file data I could find couldn't be extracted, or comes out as gibberish.

This also means you can't give yourself items, so for the special unique weapons (Kuai, Fenrir, Last Wish, Zaghnal) you can't give them yourself without doing the actual bounty, but you can always make things easier by editing other stats (e.g. Change the move speed parameter for the Kuai bounty). I might as well list their requirements here and how I got them:
- Kuai dagger: Complete the bounty challenge, which consists of the usual timed parkour challenge. However, it's notoriously difficult, especially since grappling hook is not allowed, yet there's a part where you have to get onto an apartment roof. Also the bounty is started on top of the antenna of the antenna safe house, and you have to climb back up there if you fail (because it's not considered a challenge your position doesn't get reset during failure/success). It's possible normally, just need maxed out skill tree, memorize the path, and hope nothing goes wrong. Otherwise you could just edit the move speed of the player which I found helpful.
- Fenrir: Complete the bounty challenge, which is to slice 3 heads off in one swing, and do this 30 times. Get a machete and give it the axe cut type + damage, then slash away at zombie crowds aiming for their heads. The Following DLC helps with this in the open fields.
- Last Wish: Complete the bounty challenge, which is to land 2 headshots in one shot, and do it 30 times. I never got this cause it was too hard and there's really nothing to help except maybe editing the damage of weapons for additional penetration. But hitting headshots was hard enough, trying to line up two heads is near impossible.
- Zaghnal: In the Prison DLC (which is free I believe) get to the end without using ranged weapons. I don't know exactly, but to be safe I went without guns and throwables in my inventory. The prison consists a building you need to navigate through, and at the end it is an arena of zombies where you face 2 waves of zombies. It is brutal normally, since you will need to face volatiles in the middle section, and a jacked-up demolisher at the end. You could also just modify weapon damage and kill everything in one shot lol.













