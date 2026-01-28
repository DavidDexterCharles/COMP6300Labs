# GIT Basic Steps

Git is a distributed version control system for tracking changes in source code. It lets multiple people collaborate, keep a history of edits, branch and merge work, and sync changes with remote repositories (e.g., GitHub). This is a guide into some of the basics of git that i think is a good quick start guide for effectively using git at a functional capacity. The uses/readers should keep in mind git is vast and there are various strategies and commands that can be implemented and executed for various multitudes of use case scenarios. Hence users should know that exploring for additional information when issues arise is expected and natural.

first create repo, giving repo a suitable name ensure to specify whether its public or private and also include readme, for the type of project you are going to create you would include the respective git ignore. Basic strategy is to slect the git ignore for the project based on the main programing language being used example, for node project use node git ignore.

second cloning project
after you have created your git repo you can clone it using:
git clone https://github.com/DavidDexterCharles/COMP6300Labs.git
the command is the same for you but the repository link will be different

third adding or staging changes
when you clone a project you actually setup a local repository on your machine. When you make changes to your codebase you can add these changes to a local staging area (so to speak).
Note: for your local git repo there is only one staging area. Therefore when you "git add" it will always overwrite the existing changes in the stageing area.
changes can be added/staged using the following command
"git add --all" , N.B. there are other variations of the command that can allow a user to add specific files, this is up to the student to explore on their own. the "git add --all" is a command that from my experience ensures to capture all changes and prevent unexpected missing files or accidentally forgeting to include project files.

fourth commiting changes
If a user is creating or adding a new feature to the code base and wish to add it to staging, they may not want to overwrite what already exist in staging. In this scenario commiting changes that exist in staging is the next important step in version control to allow users to have esentially checkpoints for their progress.
A user can commit their changes that are already in staging, this will then store a snap shot of the staged project at the specfic time, with a commit message explaining the snapshot( this is just the basic explanation from my perspective but may not be the most technical accurate explanation )
After the changes have been commited, staging area now becomes available/free to add new changes to.
To commit changes the command is shown below:
git commit -m"added two new enponints, this is an example commit message"

fifth pushing changes.
Only changes that have been commited can be pushed to remote branch, i.e. get pushed to the remote repository from your local branch on your computer. The reason for terming your repo branch will be explained in the 6th point. so to push changes to remote branch the user first must add changes to staging, commit the changes, and then use the "git push" command to push the changes. The command is "git push"

sixth creating branches
There are many reasons that can arise as to why one may wish to work on a sepearate copy of the original codebase. One main reason is because they dont want to touch production code that is already working perfectly and risk breaking the production code. In this scenario the concept of branching becomes important and practical solution and is commonly used. Note , users can explore branching on their own with regards to branching strategies, which are various ways dev teams and industry experts came up with for deciding when to branch naming conventions for naming branches, etc. some industry standards some opinionated. I am just going to show you how to create branches.
So to create a branch of the repo in question you use the following command:
git checkout -b"mynewbranch"
this will create a new branch locally, on this new branch you can make changes commit and push as usual, but when you are pushing a new branch for the first time, when you try to type the command "git push" you may see the following in the terminal
"git push --set-upstream origin mynewbranch"
this is just saying that your branch that your trying to push to does not exist remotely yet and therefore to also create the remote version of mynewbranch you will first have to do the "git push --set-upstream origin mynewbranch". After this for subsequent pushes you can use "git push" as usual.

seventh switching between branches
to switch between branches you use the following command:
"git switch nameofbranch" referencing or previous example "git switch mynewbranch" or "git switch main" if you wish to return to your main branch. note "git switch master" may be used if your default(main) branch name was called master instead of main on initial creation.

eight merging branches
after one has made changes to a local branch that they were experimenting with they can then proceed to merge the changes into their branch of choice. they do this by first switching to the branch of choice useing the git switch command and then they would use the "git merge mynewbranch".
example to merge the changes from mynewbranch into main the steps are as follows
"git switch main"
"git status" this is to check if there are local changes in main that needs to be either commited or pushed.
"git pull" this is to pull any remote changes that may have been made.
git status and git pull combo is one of the mehtods I use for minimizing something know as merge conflicts. The user is encoraged to do research on their own to see what merge conflicts are and how to resolve.
after the quick verification that the main branch is in a stable state to be merged into the user can now type the command:
git merge mynewbranch

ninth pulling changes and collaboration
introduced earlier a user can pull changes which may have been made to a remote branch by them from another machine or may have been made by another collaborator on the repo/project. the git pull command is meant to pull changes to local branches.

tenth cleaning up old repos local and remote
Below is how you may go about cleaning up repositories, but delete branches should be done extremely cautiosly, users can lookinto how backing up branches may be possible
Local (safe):
git branch -d <branch-name>
Local force delete (discard unmerged work):
git branch -D <branch-name>
If you're on the branch, switch first:
git switch main
Delete remote branch:
git push origin --delete <branch-name>
Or alternate remote syntax:
git push origin :<branch-name>
users should be very careful when deleteing branches, and in most cases braches arent typicaly deleted unless really neccesarry, sometimes having 50 branches is till normal and managable
