# Git Basic Steps

Git is a distributed version control system for tracking changes in source code. It lets multiple people collaborate, keep a history of edits, branch and merge work, and sync changes with remote repositories (for example, GitHub).

This document is a quick-start guide that aims to get you using Git confidently at a functional level. Git is a large topic with many workflows and commands for different scenarios, so you should expect to look up extra details as new situations arise—that is normal and encouraged.

## 1. First: Create the repository

Create the repository on your Git hosting platform (for example, GitHub), giving it a clear and meaningful name. Decide whether it should be **public** or **private**, and choose to include a `README` if appropriate.

For the type of project you are creating, select a suitable `.gitignore`. A simple rule of thumb is to pick the `.gitignore` template that matches your main programming language or framework (for example, for a Node.js project, choose the Node template).

## 2. Second: Clone the project

After you have created your remote repository, clone it to your local machine using:

```bash
git clone https://github.com/DavidDexterCharles/COMP6300Labs.git
```

Your command will use **your** repository URL, but the pattern is the same.

## 3. Third: Add (stage) changes

When you clone a project, you create a full local repository on your machine. When you make changes, you can add those changes to the **staging area**.

Note: for each local Git repository there is only **one** staging area. When you run `git add`, it updates what is currently staged (it does not create multiple separate staging areas).

To stage all changes, you can run:

```bash
git add --all
```

There are many variations of `git add` that let you stage specific files or even parts of files. Students are encouraged to explore those options. In practice, `git add --all` is a simple command that reliably captures all changes and reduces the risk of accidentally missing files.

## 4. Fourth: Commit changes

If you are adding a new feature or making edits and you want to keep a record without losing what is already staged, the next step is to **commit**. Commits act like checkpoints in your project history.

When you commit, Git stores a snapshot of everything currently staged, along with a commit message that describes the change (this is a simplified explanation, but it is a useful mental model).

After the changes have been committed, the staging area is free for new work.

To commit staged changes:

```bash
git commit -m "Added two new endpoints (example commit message)"
```

Write clear, concise commit messages that explain the “why” and “what” of the change.

## 5. Fifth: Push changes

Only committed changes can be pushed to a remote branch—that is, uploaded from your local repository to the remote repository.

To push your local commits to the remote branch:

```bash
git push
```

In practice, the usual flow is:

1. Stage your changes (`git add`).
2. Commit your changes (`git commit`).
3. Push your changes (`git push`).

The idea of “branches” is explained in the next section.

## 6. Sixth: Create branches

Often you will want to work on a separate copy of the main codebase. A common reason is to avoid touching production-ready code directly and risking breaking it. Branching provides a safe and standard way to do this.

There are many branching strategies in industry (for example, Git Flow, trunk-based development) that describe when to branch, how to name branches, and so on. These can be explored separately. Here we focus on the basic commands.

To create and switch to a new branch:

```bash
git checkout -b my-new-branch
```

This creates a new branch **locally**. On this branch, you can make changes, commit, and push as usual. When you push this branch for the first time, Git may suggest a command like:

```bash
git push --set-upstream origin my-new-branch
```

This is telling you that the branch does not exist on the remote yet, and you need to create and link it. After you run that once, you can normally use `git push` without extra options for future pushes on that branch.

## 7. Seventh: Switch between branches

To switch between branches, use:

```bash
git switch name-of-branch
```

For example:

```bash
git switch my-new-branch
git switch main
```

Some older repositories might use `master` instead of `main` as the default branch name. In those cases you may use:

```bash
git switch master
```

## 8. Eighth: Merge branches

After finishing work on a feature branch, you often want to merge those changes into another branch (for example, `main`). A typical flow is:

1. Switch to the branch you want to merge **into** (for example, `main`).
2. Make sure it is up to date and in a stable state.
3. Merge the feature branch.

Commands:

```bash
git switch main
git status     # check for local changes that may need to be committed or cleaned up
git pull       # bring in any remote changes
```

This `git status` + `git pull` combination is a practical way to reduce the chance of merge conflicts (although it does not guarantee avoiding them). Students are encouraged to read more about **merge conflicts** and strategies for resolving them.

Once `main` is in a good state, you can merge your branch:

```bash
git merge my-new-branch
```

## 9. Ninth: Pull changes and collaborate

As mentioned earlier, you can pull changes that were made on the remote branch—either by you from another machine or by collaborators.

To pull changes from the remote into your current local branch:

```bash
git pull
```

This keeps your local copy in sync with the remote repository and is essential when working in a team.

## 10. Tenth: Clean up old branches (local and remote)

Over time, branches can accumulate. Cleaning them up can be useful, but **deleting branches should be done cautiously**. You may want to research backup strategies or protections (for example, protecting the `main` branch).

Some commonly used commands:

- Local (safe delete, only if branch is fully merged):

  ```bash
  git branch -d <branch-name>
  ```

- Local force delete (discard unmerged work):

  ```bash
  git branch -D <branch-name>
  ```

- If you are currently **on** the branch, switch first:

  ```bash
  git switch main
  ```

- Delete a remote branch:

  ```bash
  git push origin --delete <branch-name>
  ```

- Alternate remote delete syntax:

  ```bash
  git push origin :<branch-name>
  ```

In many real projects, it is normal to have many branches (sometimes dozens). Branches are not always deleted immediately; it depends on the team’s workflow and policies. Always double-check before deleting, especially on shared or production-related branches.

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
