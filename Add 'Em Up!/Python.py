# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/addemup
# Complexity: O(N^2) where N is the number of cards

def isCardFlippable(card):
    for digit in card:
        if (int(digit) == 3 or int(digit) == 4 or int(digit) == 7):
            return False

    return True


def flipCard(card):
    result = ""
    for digit in card:
        flipMap = {"1": "1",
                   "2": "2", "5": "5", "6": "9", "8": "8", "9": "6", "0": "0"}
        result += (flipMap[digit])
    return result[::-1]


def main():
    # read & store input
    inputString = input("")
    numberOfCards = int(inputString.split()[0])
    desiredSum = int(inputString.split()[1])
    inputString = input("")
    cardsArray = inputString.split()

    comparisons = 0
    for xCard in range(numberOfCards):
        for yCard in range(xCard + 1, numberOfCards):
            comparisons += 1
            print(comparisons)
            # check if actual sum is desired sum with no cards flipped
            actualSum = int(cardsArray[xCard]) + int(cardsArray[yCard])
            if actualSum == desiredSum:
                return "YES"
            # check if the x card is flippable
            if (isCardFlippable(cardsArray[xCard])):
                # check if actual sum is desired sum with the x card flipped
                actualSum = int(
                    flipCard(cardsArray[xCard])) + int(cardsArray[yCard])
                if actualSum == desiredSum:
                    return "YES"
            # check if the y card is flippable
            if (isCardFlippable(cardsArray[yCard])):
                # check if actual sum is desired sum with the y card flipped
                actualSum = int(
                    cardsArray[xCard]) + int(flipCard(cardsArray[yCard]))
                if actualSum == desiredSum:
                    return "YES"
            # check if the x card and y card are flippable
            if (isCardFlippable(cardsArray[xCard]) and isCardFlippable(cardsArray[yCard])):
                # check if actual sum is desired sum with the x card and y card flipped
                actualSum = int(
                    flipCard(cardsArray[xCard])) + int(flipCard(cardsArray[yCard]))
                if actualSum == desiredSum:
                    return "YES"

    return "NO"


if __name__ == "__main__":
    result = main()
    print(result)
