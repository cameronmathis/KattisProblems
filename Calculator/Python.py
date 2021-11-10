# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/calculator
# Complexity: O(1)

import sys


def main():
    for line in sys.stdin:
        # evaluation input
        answer = eval(line)
        # format the answer decimals
        formattedAnswer = "{:.2f}".format(answer)
        print(formattedAnswer)


# call the main method
if __name__ == "__main__":
    main()
