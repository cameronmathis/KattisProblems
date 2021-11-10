# [A New Alphabet](https://open.kattis.com/problems/anewalphabet) - _Completed_

## Table of contents

- [Problem](#problem)
- [Input](#input)
- [Output](#output)
- [Samples](#samples)
- [Setup](#setup)
- [Difficulty](#difficulty)

## Problem
A New Alphabet has been developed for Internet communications. While the glyphs of the new alphabet don’t necessarily improve communications in any meaningful way, they certainly make us feel cooler.

You are tasked with creating a translation program to speed up the switch to our more elite New Alphabet by automatically translating ASCII plaintext symbols to our new symbol set.

The new alphabet is a one-to-many translation (one character of the English alphabet translates to anywhere between 1 and 6 other characters), with each character translation as follows:

| Original | New | Original | New | Original | New    | Original | New   | Original | New |
| -------- | --- | -------- | --- | -------- | ------ | -------- | ----- | -------- | --- |
| a        | @   | g        | 6   | m        | []\/[] | s        | $     | y        | \`/ | 
| b        | 8   | h        | [-] | n        | []\[]  | t        | ']\[' | z        | 2   | 
| c        | (   | i        | \|  | o        | 0      | u        | \|_\| | 
| d        | \|) | j        | _\| | p        | \|D    | v        | \/    | 
| e        | 3   | k        | \|< | q        | (,)    | w        | \/\/  | 
| f        | #   | l        | 1   | r        | \|Z    | x        | }{    | 

Note that uppercase and lowercase letters are both converted, and any other characters remain the same (the exclamation point and space in this example).

## Input
Input contains one line of text, terminated by a newline. The text may contain any characters in the ASCII range 32–126 (space through tilde), as well as 9 (tab). Only characters listed in the above table (A–Z, a–z) should be translated; any non-alphabet characters should be printed (and not modified). Input has at most 10000 characters.

## Output
Output the input text with each letter (lowercase and uppercase) translated into its New Alphabet counterpart.

## Samples
_Sample Input 1:_ </br>
All your base are belong to us. </br> 
_Sample Output 1:_ </br>
@11 \`/0|\_||Z 8@$3 @|Z3 8310\[\]\[]6 '\]\['0 |\_|$. </br>

_Sample Input 2:_ </br> 
What's the Frequency, Kenneth?</br> 
_Sample Output 2:_ </br>
\\/\\/\[-\]@'\]\[''$ '\]\['\[-\]3 #|Z3\(,\)|\_|3\[\]\\\[\]\(\`/, |<3\[\]\\\[\]\[\]\\\[\]3'\]\['\[-\]? </br>

_Sample Input 3:_ </br>
A new alphabet! </br> 
_Sample Output 3:_ </br>
@ \[\]\\\[\]3\\/\\/ @1|D\[-\]@83'\]\['! </br>

## Setup
In order to run, clone this folder onto your local machine and run the command:

	$ ./run.sh

## Difficulty
~ 2.1 / 10
