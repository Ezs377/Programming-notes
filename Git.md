# GIT/GITHUB
### Git:  
To install just look up Git downloads. For installation, it’s best to leave everything to default. For the text editor, you can use Notepad, but it’s recommended to have Notepad++ installed as it is the easiest way to edit text with Git. For the Git init branch name, Git defaults to `master`, but you can change the default to something else if preferable (this provides the name of the git repository). For everything else leave it as it is.

### Git common terms:  
- **Branch**: A version of the repository (main project head) 
- **Checkout**: Go to and edit, whether commit, branch, etc
- **Commit**: A change to the repository from saving. Basically a ‘save’ of your current file state. Is separate from your file’s own savestate. Git takes a mini ‘screenshot’ of your file state when you commit, but your files themselves shouldn’t be affected unless you reset or revert stuff
- **Clone**: Duplicating a repository 
- **Head**: The current branch being worked on. It’s basically what your location is in Git.
- **Index**: A temporary storage for preparing changes to be made. You add or unstage files to commit in the index.
- **Master**: The default branch, although it can be labelled with different names (eg. main)
- **Merging**: Combines the changes made in different branches together
- **Original**: The local\remote repository that the whole repository was cloned off. Usually shortened to origin.
- **Pull**: A change from an online repository that is ‘pulled’ and integrated into a working repository
- **Push**: Uploading a change from a local repository to a remote repository
- **Remote**: A remote repository that is stored on a server and not locally.
- **Repository**: A data storage used by Git to store files and changes to those files
- **Stashing**: Switching branches without committing the current file(s)
- **Tag**: Marking specified commits with a label. Can have customized labels. 
- **Upstream**: The main repository where files are cloned off
- **Downstream**: Files, projects, repositories that have been cloned from ‘upstream’

<!-- For commands
- Git revert: Undo a change to a commit. This creates another commit with the undone changes
- Git checkout: Pulls original files from the main repository and becomes a new commit. Basically resets the current work with the original
- Git reset: Resets all changes done in a commit and loads to a previous commit if --hard is used
- Git ignore: Ignore certain untracked files, preventing them from accidentally being tracked and committed
- Git diff: Shows differences between commits, repository, and other files 
- Git cheat sheet: A list of quick references for Git for various information regarding Git
- Git Flow: The branching model used for Git. A type of branching that is designed to work in collaborative work. Branching is basically a type of version control that duplicates files from a main, allowing people to work with them without altering the main files
- Git squash: Combining several commits into one commit. Useful when combining multiple changes from different people to submit
- Git rm: Used to remove files from the index or working directory
- Git fork: A temporary copy of the main repository that people can use to edit without changing the main repository. A fork is usually used to submit changes to a repository in group projects. Forks aren’t stored locally and local files can be forked and then submitted. Differs from pulling as in that forking is like making a remix of a song on your own. Pushing and pulling is like working with the songwriter to make music.
-->

### Git configuration:   
Git config can be used to set Git settings. Use ‘git config’ to find settings. `--list --show-origin` is used to locate config files for Git. `--list` lists all current config settings for GIt. `user.name` sets the username for Git projects. `init.defaultBranch` sets the name for the default branch. Use `git config --global core.editor` to change the text editor used to set messages for commits.

### Git config options:  
- `--global` = Set for all projects
- `--local` = Set for current repository
- `--unset` = Remove a variable
- `--list` = List all current configs 

Variables can be added. For example, `user.name` adds a variable called `user.name`, which can then be followed by any string afterwards for that variable’s value. It helps with labelling Git projects, such as setting a name for each project. Any word can be used for a variable name as long as it is in the right format (a dot between 2 words)

### Common Git commands (start with ‘git’ for all):  
- `add` = Add files to be committed. Can be repeated until the commit, adding more files. Also prepares a commit to be updated with file changes. Doesn’t change commit.
- `clone` = Clone a repository into a working folder in files. Can start working with repo. Online servers/repositories can be cloned via URL.
- `commit` = Update commit to match updated file. Requires file to be added first
- `commit -a`: Change commit to match the file changes. Requires a message from user (using Notepad++). A simpler, one command function that updates a commit without using add and commit.
- `init` = Creates an empty repository or activate an existing repository in local drive. Adding a directory name after the init will create a folder with the repository inside
- `status` = Check status of files in a repository and whether they are changed or not
- `rm` = Remove files
- `push` = “Upload” committed files to a remote repository, which is kept online. 
- `pull` = “Download” a remote repository into a local repository and merge changes, essentially copying the remote repository and mixing it with a local repository. This is basically a fetch and merge at once.
- `fetch` = Notes changes done to a remote repository and allows you to compare them to your local repository without actually transferring files. Afterwards using merge can merge these changes to your local repository.

### Git options (use with a command)  
- `-m` = Add a message along with the commit (git commit)
- `-a` = Include all changed files in the commit, as long as they have been tracked (git add)
- `--amend` = Redo the last commit done and replace it with a new commit (git commit)
- `-v` = View your attributed data with a variable name. Usually used with git remote to see where you are pushing and pulling with ‘origin’.
- `-` = Use with git reset to move back to HEAD’s last position, useful to put HEAD back to where it was if you accidentally move it somewhere.
- `-s` = Use with git status to have a shorter summary of status.

### Useful Git stuff:  
- `git restore` --staged <file>: Untrack a file/files from a commit
- `git add <file(s)>`: Add files to be tracked
- `git add *`: Add all files in the directory to be tracked (except files that start with a dot). Adding a file extension name after the asterisk (eg. .HTML) will track all files with that extension  
- `git add -p`: View changes in files before adding
- `git log`: Shows history of commits and changes, with messages that were typed prior to saving a commit
- `git push` -u origin <branch name>: Upload (push) files from a local repository to a remote repository
- `git remote rm origin`: Delete a remote repository. Useful to reset the location of remote repository
-  git remote add origin <URL>`: Set a new address for a remote repository to label ‘origin’
- `git init <filename>`: Create a folder named <filename> which will contain the repository. Useful to set a folder for the repository without cloning
- `git clone <URL>`: Use to copy a remote repository and make the copy into a local repository. Useful when pushing and pulling from repositories
- `git diff --status`: Shows the difference between currently staged files and committed files.
- `git show/diff HEAD~<no> <file>`: Shows the difference between commits. The number after HEAD determines the previous commit referenced (1 is the commit right before the current commit, 2 is the commit 2 times before the current commit, and so on). Using show will also display the message with the commit
- `git checkout (head no) <file>`: Reverts back into a previous version of the file determined by the commit no. Useful if you haven’t committed, but want to discard changes to files (usually files that have been saved with their editors and can’t undo the files with their editors). Beware of using this, as moving back more that your latest commit will detach HEAD and mess up your files if you commit. Only use in the form git checkout HEAD <file>. 
- `git revert <HEAD no.>`: Same like git checkout HEAD <file>, but now you can safely move HEAD back as many times as you like without repercussions. Lets you undo changes by moving back to a previous commit. Revert also makes you commit to save the ‘undo’ you just did, so you can undo the revert by using revert again.
- `git reset HEAD~(no)`: Resets files to a previous version depending on the HEAD number. This will completely reset everything to its previous state, so undoing a hard reset is really difficult. Only use if you know what you want to undo and don’t mind losing some work.
- `git rm <file>`: Add a deleted file to commit
- `git commit --amend`: Update a commit message by recommitting. Useful if you write the wrong message or typo in a commit message (which is used to tell what changes you have done in a commit, very important for keeping track of changes)
- `git status -s`: A short summary of git status. Instead of a full description it displays a symbol followed by the file. The symbols are: M = modified, unstaged. MM = Staged,but modified while staged, so unstaged changes. A = added (staged). ?? = untracked, unstaged.
- `rm -rf .git` = Delete a local repository without deleting files in the repository folder

### Starting with Git:  
First, use the git init command to initialize a local repository. This can be done via Windows command line prompt or Git Linux Bash command line. You can also create a remote repository with a Github account, and clone it into a local repository. You will need a command line editor regardless if you want to edit files.  

##### Using `git init`:  
`git init` on its own will create a local repository called `.git` on default. `.git` is 
local, and you shouldn’t touch or rename it as it makes everything harder. Usually it is easier to do `git init <folder name>` as this automatically creates a folder that contains the repository, instead of you having to create a new folder on your own or accidentally creating the repository in the wrong folder. Be aware when naming folders and different command lines have different ways of expressing spaces in names. Windows command prompt uses `“ “` to close a full name, while Linux Bash uses `\` to separate words in a full name.

##### Git help:  
Typing `git help <command>` will bring up an offline HTML doc that shows what the command does and the commands associated with it. If that is too much and you only need a simple options list use `git <command> -h`. 

##### Gitignore file:  
The gitignore file is used by Git to ignore specified files in your repository, meaning it won’t show up on your Git status and etc. A hashtag  ` # ` is used to write comments in the file.  
A list of common symbols used for the file:  
- `*.exe` = ignore files that end with an .exe (e.g. `Steam.exe` would be ignored)
- `!Office.exe` = Don’t ignore the file named `Office.exe`, but ignore all other `.exe` files (from the previous command, `*.exe`)
- `/notes.txt` = Ignore the file `notes.txt` in the current directory, but don’t ignore files called `notes.txt` in other directories (folders)
- `Main/` = ignore all files in the directory `Main` (folder)

###### How to push a local branch to a remote repository:  
The purpose of this is to save files locally, then transfer them online to a remote repository.
First git remote add origin <URL> will set a remote repository as ‘origin’. Then use the push command to push a branch to the repository. Make sure origin is the URL and not something else otherwise won’t push. Using -f as an option will force a push, and replace the remote repository with the commits from the local repository. This might delete files and commits from the remote repository.

##### Undoing changes:  
Git has 3 different methods for undoing changes: Revert, Checkout, and Reset.  
Using `git revert <HEAD~no.>` will revert all commits done to the HEAD number specified. This is considered a change to the current HEAD, where the files have been committed with new changes. Since a commit saves all files permanently with their changes, using revert will undo the changes done in a commit, bringing the files back to the state before they were committed. This is considered another change to Git, so you have to re-commit after a revert to actually save the files.  
For example:  
There is a file. The file’s contents are:  
```
	Hello there
	we are good
	Goodbye
```  
This becomes HEAD  
You edit some stuff and commit it  
```
	Hellow Their
	we are bad
	bye
```
Now this commit is HEAD
You realize the stuff you edited was wrong, but it has been committed. So you use `git revert HEAD~1` to restore the file to a previous version to undo the changes. `HEAD~1` is used as that is the previous HEAD, and HEAD numbers are counted from the current HEAD.
```
	Hello there
	we are good
	Goodbye
```  
This change is committed, therefore saving the file as this version.
	
Simply put, `git revert` undos changes that have been committed. It helps if you accidentally submit, push, or commit some changes to files that you didn’t want. This can also be used to undo changes on remote repositories, as every commit can be pushed to the remote repository. Thus, pushing a revert commit to a remote repository will replace the wrong files with the new restored files.

Using `git checkout <file>` will reset the version of a file to its last commit as long as the file hasn't been staged (added to be committed). Instead of undoing commits, git checkout  is used to reset a file to its last commit. This is useful if you haven’t saved or committed the file, but decided to undo all the changes you have done because of reasons.  
For example:  
You have a file
```
	Hello there
	we are good
	Goodbye
```  
It has been committed. Now you start working on it 
```
	Hellow Their
	we are bad
	bye
```  
You don’t like the way it looks, or all the spelling errors. So you use `git checkout <filename>` to undo all of your changes
```
	Hello there
	we are good
	Goodbye
```  
No harm, no foul. FIle is restored to before and nothing has been committed.

Simply put, `git checkout` is used when undoing all of your changes to a file, instead of going through the file yourself and deleting your changes manually. As long as the last commit contains a saved file you can keep using checkout to revert back to the original version until your next commit. If you do commit some bad changes, use `git revert`. Don’t use `git checkout` with a HEAD no. as that will move your HEAD back to before your most recent commit and detach it, meaning that now you can’t do anything without messing up your files (doing this creates a non-existent branch, which is way too complicated). `git checkout`is primarily used for switching branches in Git, so if possible it's preferable to undo your changes manually in the file.

Finally, `git reset (option) <HEAD no.>` will completely revert your files to a version specified by the HEAD no. It has different options that can be used which may or may not be useful to you. The main difference between `git revert` and `git reset` is that with `git revert` you make a commit that contains your reverted files, while `git reset` moves to a different version of your files and removes all commits in front of your current version. `git revert` is considered safer as your previous commits are still saved, and you can still see and view them, and even go back to them with `git revert` again if you want. `git reset`, however, actually moves you back to a previous version of your files. This is dangerous as if you accidentally commit now, then the commits that you skipped over while moving back will be erased, meaning you can’t undo your reset. For example:  
You have a file that is committed (commit 1)  
```
	Hellow Their
	we are bad
	bye
```  
Make some changes, commit again (commit 2)  
```
	Wellow thier
	we are good
	byebye
```  
And then make some more changes, and commit again (commit 3)  
```
	Hello there
	we are good
	Goodbye
```  
You then want to reset it to your original version. So you use `git reset --hard HEAD~2` (HEAD~2 as it moves back 2 commits from the current commit, which is the very first commit you did). This resets your file version to your original.
```
	Hellow Their
	we are bad
	bye
```  
Then you commit. Then you decide the latest commit was better (commit 3) but now you can’t go back to that version as you’ve committed, and Git deletes the other commits as it was done AFTER the commit you are on, and since you moved back from commit 3 to commit 1, commit 2 and commit 3 is deleted by Git as they were done after commit 1, therefore, they didn’t exist when you were working on commit 1.  
The options used also affect your chances of restoring your work.  
- `--soft` will change your files to a previous version (commit 1), but your changes are still saved in the index and in your local files. Meaning that doing a commit without changing anything brings your files back to commit 3 without any changes, undoing your reset. UNLESS you edited files in commit 1, then add them to the index. This replaces the files from commit 3 with files from commit 1, therefore leaving you with no chance of recovering changes in commit 3. This option is usually used when moving commits to a different branch and has other work you want to merge with these commits. Reset, move to a branch, and commit to integrate these commits to that branch without altering the commits in the main branch.  
- `--mixed` is almost the same as --soft except only your working directory is untouched. Your index is reset, but files appear as modified as they aren’t changed. Adding and committing these files brings your files back to commit 3. Like before, any changes done to your files will prevent you from undoing your reset, as committing these changes will erase traces from commit 3. Only way to undo a reset is to add and commit right after the reset without editing anything. 
- `--hard` completely resets everything to your specified state. Can’t undo the reset as it also wipes your index and working directory so there is no trace of commit 3.

`git reset` is only recommended on local repositories. Doing a reset on a remote repository could erase changes and file permanently on the server with no way to bring them back, a very bad idea when working with others. `git reset` is generally not used at all unless you really need to go back to previous version of your files and don’t mind losing your current versions (like if you deleted several files, commit, and then decided to get them back).

If by any chance you accidentally do a `git reset` and lose your changes, `git reflog` can be used to find the correct HEAD no. in which you use git reset again to go back. `git reflog` is basically a history of commits that Git always keeps in a storage file, and can’t be altered except if you empty it manually or Git empties it automatically after 90 days. Reflog displays previous commits as `HEAD@{<no.>}` as opposed to the standard `HEAD~(<no.>)`. So don’t forget to add a `@` symbol, and close the HEAD number in curly brackets (`{ }`) instead of just writing the number. Using `git reset` with a reflog HEAD resets your files to that state, regardless of whether it was done in the past or future, as long as it exists in reflog. And reflog notes down every commit you make, so it’s likely that using a reflog HEAD allows you to restore any version of your files. 

To summarize: Use `git checkout HEAD <file>` to discard changes to your files if you haven’t committed. If you have, then use `git reset` to go back to a previous commit. If you want to undo a change while working with a remote repository, use `git revert` to safely undo the change without messing with the remote repository. `checkout` and `reset` are used for local files, revert is usually used when working with a remote repository.

### Specifications of the HEAD label:  
HEAD is basically a pointer in Git while navigating files and repositories. HEAD points to the current branch your most recent version of your files you are on. Changing between branches, resetting history, making commits all move your HEAD pointer. HEAD basically tells you where you are in terms of your files, branches, and repositories. HEAD usually tells where you are by pointing to the end of a branch, which is usually the most recent commit you have done. If HEAD is detached, that means it is directly pointing to a commit rather than a branch. SInce all commits need to be on a branch in order for Git to be able to arrange them in chronological order, committing while HEAD is detached will instead commit your files to a ‘ghost’ branch, which cannot be accessed with Git usually. If this happens, use `git reflog` to find that commit, and use `git branch (branch name) <commit no.>` to create a new branch with that commit. Then if you want you can merge it with your main branch to integrate the commits. To move HEAD back from a detached state use `git checkout -`. 

There are 3 main HEAD functions you can use: `HEAD~`, `HEAD^`, and `HEAD@{}`.

`HEAD~` is primarily used to through your commit history, and go to previous commits by using your current commit as a reference point. All locations of your history are taken relative to your current commit number. For example:  
`HEAD~1` will move back to the commit BEFORE the current commit. Git moves back one step in your history. 

`HEAD~5` moves back 5 commits before your current commit. Git moves back 5 steps in your history. Cannot do if you have less than 5 commits.

Using `HEAD` without any number will simply bring back your most recent commit version, which is usually what you were on before doing `HEAD~1`. Note that typing `HEAD~` without a number is the same as doing `HEAD~1`.

`HEAD@{}` is another type of navigation that uses your commit history from reflog, instead of using your current commit as your reference point. Reflog contains a list of ALL commits you have done, even deleted commits, so this type of HEAD navigation is usually used to bring back lost files. `HEAD@{`} works differently, as you would probably need to run `git reflog` to find the right HEAD number that has the commit you want (which is why leaving messages in your commits is useful as you can use them to identify which commit is which) and use that number in between the curly brackets (eg. `HEAD@{4}`) to navigate to that. `HEAD@{}` actually follows the number to the attributed commit, while `HEAD~` uses the number to move back that amount of steps. For example: 

`HEAD@{1}` will move to commmit 1 specifically. This uses the label from reflog to identify a previous commit in your history, and brings that back.

`HEAD^` is usually used if you’ve merged branches. `HEAD^` is usually used to identify the branch number that was before you merged it with another branch. Usually you would need to use both `HEAD~` and `HEAD^` to move to another branch and the previous commit. The diagram provides a better explanation:  
![Git branch HEAD flow](https://github.com/Ezs377/Programming-notes/blob/main/Images/Git%20undos.jpg)  
Note that the ‘first’ commit isn’t `HEAD~1`. If using `HEAD@{}` then yes, you would do `HEAD@{1}` to move to the first commit. But `HEAD~1` will only move you one step before the current commit (which is simply HEAD). `HEAD~2^1`  is used to move to the third commit, as `HEAD~2`  will move back 2 steps from your current commit, while `HEAD^1` ensures you stay on the first branch, and not the other branch which is merged later on.

Please note that all navigation done with HEAD either needs a `git checkout` or a `git reset` command with it, or another command that is used with HEAD. Using HEAD on its own doesn’t work. 

Simple Git cheat sheet, for quick referencing on commands:  
![Git cheat sheet](https://github.com/Ezs377/Programming-notes/blob/main/Images/Git%20cheat%20sheet.jpg)
***
