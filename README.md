# Working with Git: Clone and Branch

## Cloning a Repository

```bash
git clone git@github.com:thancode99382/DoAnTKHDT.git
```

## Change to the repository directory

```bash
cd DoAnTKHDT
```

## Open the repository in Visual Studio Code

```bash
code .
```

## Create a new branch

```bash
git checkout -b <branch-name>
```

`<branch-name>` is the name of the new branch you want to create. For example, if you want to create a new branch called `feature-1`, you would run:

```bash
git checkout -b feature-1
```

The name of the branch should be descriptive and should give an idea of what the branch is for.

## Why create a new branch?

- To work on a new feature
- To fix a bug
- To experiment with new ideas
- To refactor code
The idea is to isolate changes from the main codebase until they are ready to be merged back in.
