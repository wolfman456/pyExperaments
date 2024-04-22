# Space shooter :

## starting plan :

Space shooter will be a more electorate version of the previous dodger typy game.
With the enemy targets coming from above and going down. Additionally, the player will be able to shoot at the ship
to score. The rectangles will be replaced with drawing in this version.

## Issues faced :

1. Getting a bullet to collide with enemy ship.
2. creating buttons
3. even using oop game has started to feel spaghetti code. 

## Checklist:

| Task                            | status      | comment                                                      |
|---------------------------------|-------------|--------------------------------------------------------------|
| Create screen                   | done        |                                                              |
| Add ship                        | done        |                                                              |
| make ship move                  | done        |                                                              |
| add bounds                      | done        |                                                              |
| make ship shoot                 | done        | centering firing on ship not as simple as originally thought |
| add enemy ship                  | done        |                                                              |
| read/write score                | done        |                                                              |
| collision detection             | done        |                                                              |
| end Screen                      |             |                                                              |
| save score                      | done        |                                                              |
| start screen/create player name | done        | functional buttons lead to more changes then expected        |
| refactor code                   | first round | multi step process                                           |
| load image function             | done        |                                                              |
| High score screen               |             |                                                              |

| Refactoring Step                           | Status   |
|--------------------------------------------|----------|
| create skeleton of game object             | complete |
| Move game logic in to game object          | complete |
| Ship added to screen                       | complete |
| fixed ship movement so it is smooth again  | complete |
| ship shooting                              | complete |
| enemy ships                                | complete |
| abstract functionality out of main methods | complete |
| create load screen logic                   | complete |
| make ship shoot only one bullet per press  | complete |   

### Future Plans :

1. Add levels
2. At this point, it would take little effort to alter this in to a space invader type game. So this is a possible
   continuation of this project.
3. Add a fancier background.

### Technology Used :

| Tech name                                          | Use In project          |
|----------------------------------------------------|-------------------------|
| [opengameart](https://opengameart.org/users/kev93) | Used to locate game art |
