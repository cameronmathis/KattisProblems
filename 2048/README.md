# [2048](https://open.kattis.com/problems/2048)

## Table of contents

- [Problem](#problem)
- [Input](#input)
- [Output](#output)
- [Samples](#samples)
- [Setup](#setup)
- [Difficulty](#difficulty)

## Problem
2048 is a single-player puzzle game created by Gabriele Cirulli. It is played on a 4×4 grid that contains integers ≥2 that are powers of 2. The player can use a keyboard arrow key (left/up/right/down) to move all the tiles simultaneously. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move. Please observe this merging behavior carefully in all Sample Inputs and Outputs.

## Input
The input is always a valid game state of a 2048 puzzle. The first four lines of input, that each contains four integers, describe the 16 integers in the 4×4 grid of 2048 puzzle. The j-th integer in the i-th line denotes the content of the cell located at the i-th row and the j-th cell. For this problem, all integers in the input will be either {0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}. Integer 0 means an empty cell. </br>

The fifth line of input contains an integer 0, 1, 2, or 3 that denotes a left, up, right, or down move executed by the player, respectively.

## Output
Output four lines with four integers each. Two integers in a line must be separated by a single space. This describes the new state of the 4×4 grid of 2048 puzzle. Again, integer 0 means an empty cell. Note that in this problem, you can ignore the part from the 2048 puzzle where it introduces a new random tile with a value of either 2 or 4 in an empty spot of the board at the start of a new turn.

## Samples
_Sample Input 1:_ </br>
2 0 0 2 </br>
4 16 8 2 </br>
2 64 32 4 </br>
1024 1024 64 0 </br>
0 </br>
_Sample Output 1:_ </br>
4 0 0 0 </br>
4 16 8 2 </br>
2 64 32 4 </br>
2048 64 0 0 </br>

_Sample Input 2:_ </br>
2 0 0 2 </br>
4 16 8 2 </br>
2 64 32 4 </br>
1024 1024 64 0 </br>
1 </br>
_Sample Output 2:_ </br>
2 16 8 4 </br>
4 64 32 4 </br>
2 1024 64 0 </br>
1024 0 0 0 </br>

_Sample Input 3:_ </br>
2 0 0 2 </br>
4 16 8 2 </br>
2 64 32 4 </br>
1024 1024 64 0 </br>
2 </br>
_Sample Output 3:_ </br>
0 0 0 4 </br>
4 16 8 2 </br>
2 64 32 4 </br>
0 0 2048 64 </br>

_Sample Input 4:_ </br>
2 0 0 2 </br>
4 16 8 2 </br>
2 64 32 4 </br>
1024 1024 64 0 </br>
3 </br>
_Sample Output 4:_ </br>
2 0 0 0 </br>
4 16 8 0 </br>
2 64 32 4 </br>
1024 1024 64 4 </br>

_Sample Input 5:_ </br>
2 2 4 8 </br>
4 0 4 4 </br>
16 16 16 16 </br>
32 16 16 32 </br>
0 </br>
_Sample Output 5:_ </br>
4 4 8 0 </br>
8 4 0 0 </br>
32 32 0 0 </br>
32 32 32 0 </br>

_Sample Input 6:_ </br>
2 2 4 8 </br>
4 0 4 4 </br>
16 16 16 16 </br>
32 16 16 32 </br>
2 </br>
_Sample Output 6:_ </br>
0 4 4 8  </br>
0 0 4 8  </br>
0 0 32 32  </br>
0 32 32 32 </br>

## Setup
In order to run, clone this folder onto your local machine and run the command:

	$ ./run.sh

## Difficulty
2.8
