# Git Basic Steps

Git is a distributed version control system for tracking changes in source code. It lets multiple people collaborate, keep a history of edits, branch and merge work, and sync changes with remote repositories (for example, GitHub).

This document is a quick-start guide that aims to get you using Git confidently at a functional level. Git is a large topic with many workflows and commands for different scenarios, so you should expect to look up extra details as new situations arise—that is normal and encouraged.

## 1. First: Create the repository

Create the repository on your Git hosting platform (for example, GitHub), giving it a clear and meaningful name. Decide whether it should be **public** or **private**, and choose to include a `README` if appropriate.

For the type of project you are creating, select a suitable `.gitignore`. A simple rule of thumb is to pick the `.gitignore` template that matches your main programming language or framework (for example, for a Node.js project, choose the Node template).

## 2. Second: Clone the project

After you have created your remote repository, clone it to your local machine using:

```bash
git clone https://github.com/example-user/example-repo.git
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
