# PWM

## This project has 3 containers

- An python app
- An postgres database
- An pgadmin container


## Instructions 

```
# For running locally the application using docker compose:

docker compose up --build

before to work in the app (whatbot) open pgadmin and register a server with the postgres credentials defined in the env file.  
```

## Git best practices 

Squash you commits before make a pull request

```
## Where N is the number of commits
git rebase -i HEAD~<N>

## Git push force

git push -f

```