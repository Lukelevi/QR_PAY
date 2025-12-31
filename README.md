# QR PAY

## GOAL

The aim of QR Pay is to allow for users to make payments by scanning a users unique QR  Code

## Git Flow

- `main`: this branch will represent the ready to use version of the work. will be the source for deplo
- `staging`: this branch is for all the development changes made towards building a final product, and should be the source for development.
- `feature branch` - this will be a branch used to add your feature, it's ideal to create the feature branch from a ticket if not, it can follow this standard: `feature/feature-name` or `fix/bug-being-fixed` or `hotfix/any-urgent-changes-to-main`.

## Getting Started

After cloning the repo, the branch will be on `main`. You will then need to `switch` to staging which is the most up to date branch and branch off from there.

### Step 1

Switch to Staging Branch:
Run `git checkout staging` or `git switch staging`.

NB! Should it not switch branch run `git fetch` then repeat the step above.

### Step 2

Create a new branch that describes the work you want to add and start making changes from there.
e.g if you want to add a feature on authentication you can name your branch like this `feature/adding-auth`

Create your new branch:
Run `git switch -c feature/adding-auth` or `git checkout -b feature/adding-auth`

### Step 3

You can start contributing and making changes to the files. Once you're happy with your changes you can commit your changes and push them to Github.

Commiting Changes:
Run `git add .` to add all changes you've made. or `git add fileName.js` if you want to add specific file.
Then Run `git commit -m 'Meaningful message representing what you did'`.

Then push your new branch with `git push -u origin feature/adding-auth` NB note that **feature/adding-auth**; represents the name of your branch.

### Step 4

Go to the projects Repo on Github and open a pull request that targets the `staging` branch.
