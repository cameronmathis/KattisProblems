# [Add 'Em Up!](https://open.kattis.com/problems/addemup) - _Completed_

## Table of contents

- [Problem](#problem)
- [Input](#input)
- [Output](#output)
- [Samples](#samples)
- [Setup](#setup)
- [Difficulty](#difficulty)

## Problem
Simon is a contestant on the new exciting game show, Add âEm Up! In this show, contestants are given a set of cards with multi-digit numbers on them, and need to select two cards that add up to a given sum. However, to make things more interesting, the font that the cards are printed in (see below) means that certain cards will display different numbers if turned upside-down, and it is legal to turn either or both of the cards if necessary to generate the sum. Please help Simon win the game!

## Input
The first line contains two integers, ð, the number of cards, and ð , the desired sum. The second line will contain ð integers between 1 and 100000000 inclusive. You may assume that 1â¤ðâ¤100000 and 2â¤ð â¤200000000.

## Output
The output should be a single line consisting of the string YES if two cards can be chosen such that (in some orientation) they add up to ð , and the string NO otherwise.

## Samples
_Sample Input 1:_ </br>
3 66 </br>
15 21 22 </br>
_Sample Output 1:_ </br>
NO </br>

_Sample Input 2:_ </br>
3 63 </br>
15 21 22 </br>
_Sample Output 2:_ </br>
YES </br>

## Setup
In order to run, clone this folder onto your local machine and run the command:

	$ ./run.sh

## Difficulty
~ 4.8 / 10
