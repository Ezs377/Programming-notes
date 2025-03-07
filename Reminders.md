
Java is installed on my current laptop in D drive and has an environmental variable implemented (JAVA-HOME).

(NOT DONE) gcc, gdb, and g++ are installed in D drive under MSYS2 folder for C and C++ compiling. 

"Java stuff" folder in "School stuff" folder has some random useful mini-code for referencing

### Git personal access token instructions:
1. Go to Settings on Github
2. Go to Developer options on the side
3. Go to personal access tokens
4. Generate a new classic access token (use fine token for companies and stuff) 
5. Copy access token to Bitwarden
6. Repeat every month or so

### Adobe Illustrator:  
- The pen tool can draw straight lines by clicking two points or make a curving line by holding and dragging on the second point. It can also make new anchor points by clicking on a path
- The selector mouse cursor can move anchor points which is useful for making small edits, as well as round corners by zooming in and dragging the small dot that shows up in a corner
- The scissor tool can section lines which is useful for removing excesses or line drawings
- For laser cutting (specifically at UoA) use black for engraving, with darker black being deeper engraving. Red (pure R, i.e. 255, 0, 0 RGB) lines for cutting, needs to be in smallest stroke size, i.e. 0.0001 mm. The For engraving it will cover anything that is black.

### Slow internet guide:
I was experiencing a similar thing after 4 days of rapidly downloading around 670 files (most just a few kilobytes, but a few were a couple hundred megabytes). Internet speed test showed normal, but webpages and especially images in webpages loaded much slower than normal. Resetting the modem didn't seem to make any difference, but flushing the DNS cache makes everything as fast as lightning now! These are the steps I followed:

**1.** Right-click the Windows Start button (or hit Windows + X on the keyboard).

**2**. Choose Command Prompt (Admin).

**3.** Select "Yes" to allow Command Prompt to make changes to your computer.

Note: If you are asked for an administrative login, you will need to contact your system administrator.

In the Command Prompt window, type the following commands (**without quotation marks**):

**4.** Type "ipconfig /flushdns" and press Enter.

**5.** Type "ipconfig /registerdns" and press Enter.

**6.** Type "ipconfig /release" and press Enter.

**7.** Type "ipconfig /renew" and press Enter.

**8.** Type "netsh winsock reset" and press Enter.

**9.** Type "netsh int ip reset resetlog.txt" and press Enter.

**10.** Restart the computer.

**11.** I also cleared all browsing history, download history, cookies, cached images and files, and hosted app data from "All time" in my web browser (I did not clear Passwords and Site settings).

**NOTE:** On the final command "netsh int ip reset resetlog.txt", I received the "**Resetting, failed || Access is denied**" error. While it seemed there still was a significant performance boost after ignoring the error and restarting the computer, I performed the following steps to clear the error and then repeated steps 1 - 11 again:

**12.** Press Windows + R on the keyboard and type regedit

**13.** Press "Okay" then "Yes" on the User Account Control prompt.

**14.** In the Registry Editor, navigate to the following folder (be sure to **double check** you have the folder starting with "eb004a00-", because there are several folders with slightly different names):

**HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nsi\{eb004a00-9b1a-11d4-9123-0050047759bc}**

**15.** Right click on folder 26 and select "Permissions".

**16.** Click "Advanced".

**17.** Beside the "Owner" field, click "Change".

**18.** In the field labelled "Enter the object name to select", type "Everyone" (without quotes) and press "Check Names", then press "OK".

**19.** Under the "Owner" field, check the box for "Replace owner on subcontainers and objects", then press "Apply" and "OK".

**20.** Under the "Full Control" section check the box for "Allow", and press "Apply" then "OK".

**21.** Repeat steps 1-11 and everything should reset without error messages this time.

Special thanks to MDTechVideos International for the video explaining the "Access is denied" error fix: [https://youtu.be/euo9zJJt7fY](https://youtu.be/euo9zJJt7fY)

And the following links for the general reset steps: [https://support.pearson.com/getsupport/s/article/Reset-an-Internet-Connection-Flush-DNS#win10](https://support.pearson.com/getsupport/s/article/Reset-an-Internet-Connection-Flush-DNS#win10)

[https://youtu.be/Jzr4XyjZ-mo](https://youtu.be/Jzr4XyjZ-mo)