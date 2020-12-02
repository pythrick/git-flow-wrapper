# gflow
Wrapper to run common git flow commands with remote repositories.

Gitflow Workflow is a Git workflow that helps with continuous software development and implementing DevOps practices. It was first published and made popular by Vincent Driessen at nvie. The Gitflow Workflow defines a strict branching model designed around the project release. This provides a robust framework for managing larger projects.

## How it works

GitFlow are guidelines for the organization of our branches, and for this reason it sets standards for names and functions for each type of branch, they are:

- **master**: contains your production code.
- **develop**: contains the code for our next deploy, this means that as the features are being finalized they will be committed to this branch to later go through another step before being committed with the master.
- **feature/***: they are branches for the development of a specific functionality, by convention they have the name started by feature/, for example: feature/registration-users. It is important to note that these branches are always based on development.
- **hotfix/***: they are branches involved in making some critical correction found in production and that is why they are made from the master.
- **release/***: has a greater confidence that a branch is developing and that it is at a level of preparation to join a master and develop.

![git-flow](images/git-flow.svg)

## Commands

```sh
# Initialize gitflow in the repository
git flow init

# Create feature
flow new feature registration-users

# Create release
flow new release v1.1

# Create hotfix
flow new hotfix correct-registration-users

# Publish changes
flow publish
```
