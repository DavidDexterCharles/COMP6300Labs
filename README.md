# GIT Basic Steps

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
git switch

seventh merging branches
after one has made changes to a local branch then
