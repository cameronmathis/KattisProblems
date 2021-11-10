# [Calculator](https://open.kattis.com/problems/calculator) - _Completed_

## Table of contents

- [Input](#input)
- [Output](#output)
- [Samples](#samples)
- [Setup](#setup)
- [Difficulty](#difficulty)

## Input

Input contains several test cases, one per line. Each test case consists of an expression to be evaluated, containing numbers, parentheses, and the operators +,−,∗,/.

Normal operator precedence applies, so multiplication and division bind harder than addition and subtraction. All operators evaluate left-to-right. Implicit multiplication is not possible, so 3(1+1) is not a valid input. There may be an arbitrary amount (including 0) of spaces between tokens. Numbers are integers with absolute value at most 500.

Input is terminated by end of file.

## Output

For each test case, output the value of the expression, with two digits of precision after the decimal point.

## Samples

_Sample Input:_ </br>
5 - 3-2 </br>
5- (3-2) </br>
5 / 3 / 2 </br>
5 / (3 / 2) </br>
1/3+1 </br>
1/(3+1) </br>
-4--2 </br>
(1-3)/(5+4) </br>
2\*3\*5\*7\*11\*13\*17\*19 </br>
-5/-5 </br>
_Sample Output:_ </br>
0.00 </br>
4.00 </br>
0.83 </br>
3.33 </br>
1.33 </br>
0.25 </br>
-2.00 </br>
-0.22 </br>
9699690.00 </br>
1.00 </br>

## Setup

In order to run, clone this folder onto your local machine and run the command:

    $ ./run.sh

## Difficulty

~ 3.3 / 10
