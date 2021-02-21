# Brick-Breaker-Terminal-Based-Game
### By Ayush Sharma - 2019101004

## Overview

A classic arcade Brick Breaker terminal based game written in Python3. 
The player will be using a paddle with a bouncing ball to smash a wall 
of bricks scores! The objective of the game is to break 
all the bricks as fast as possible. You lose 
a life when the ball touches the ground below the paddle.
```
* The code is modular and extensible to new features.
* Concepts of object oriented programming is present in the code
* The game is a basic simulator of brick breaker
* Libraries(external) used are colorama.
* Note: The development has been done on Ubuntu 18.04 OS.
* Note: For better experience use builtin terminal to play.
```

## GUIDE


Reqiurements

- Python3
- Colorama

For mac:
```
brew cask update
sudo brew cask install python3
pip install colorama
```
For Linux:
```
sudo apt-get update
sudo apt-get install python3
pip install colorama
```


Run the following code to start the game.
```
python3 main.py
```

* NOTE: Input file i.e. `input.py` has been made & checked only for UBUNTU OS.


GAME RULES
-------------------

> - Player will have total `3` lives.
> - One life is lost when ball goes below the paddle i.e. bottom of the frame
> - Increment of `+5` will be made once a brick got broke completely
> - Timer start from the start of the game, with no time limit
> - Further the ball hits from the center, more the deflection in that direction.
> - Once all lives are lost, game will get ended.
> - Once all bricks are broken, stage up will be done with new brick layout.
> - Maximum stage a player can reach is `3`

------------------------



## FUNCTIONALITIES

Controls
------------------

>- Press `Spacebar` to release the ball
>- Press `a` or `A` to move paddle left
>- Press `d` or `D` to move paddle right
>- Press `i` or `I` to change your Ball
>- To quit, press `q`

___________________


Features
-------------------

> - Total `5` different types of bricks. Three breakable, One Unbrekable & One Chain reaction initializer.
> - Chain reaction initializer brick on breaking with the ball would explode resulting in the destruction of all the bricks adjacent to it(diagonally, vertically and horizontally)
> - Total `7` ball shapes
> - Implementation of different level
> - Colors for Objects
> - Well commented code.
> - Some degree of randomness in forming Brick-Layout for a stage.

-------------------