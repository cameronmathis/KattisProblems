# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/addemup
# Complexity: O(N) where N is the number of cards

# check if a card is flipable
# @param: int
# @return: boolean
def isCardFlipable(card):
    for digit in str(card):
        if (digit == "3" or digit == "4" or digit == "7"):
            return False

    return True


# flip the given card
# @param: int
# @return: string
def flipCard(card):
    resultCard = ""
    flipMap = {"1": "1",
               "2": "2", "5": "5", "6": "9", "8": "8", "9": "6", "0": "0"}
    for digit in str(card):
        resultCard += flipMap[digit]
    return resultCard[::-1]


# create a card array containing all flipped values
# @param: int array
# @return: int array
def getCardArrayWithFlips(cardArray):
    resultArray = []
    for card in cardArray:
        nonflippedCard = card
        resultArray.append(nonflippedCard)
        if (isCardFlipable(card)):
            flippedCard = int(flipCard(card))
            resultArray.append(flippedCard)
    return resultArray


# create a card hashmap/dictionary
# @param: int array
# @return: int dictionary
def getCardMap(cardArray):
    resultMap = {}
    for card in cardArray:
        resultMap[card] = card
    return resultMap


# main method to solve the problem
def main():
    # read & store input
    desiredSum = int(input("").split()[1])
    cardArrayWithoutFlips = [int(number) for number in input("").split()]
    cardArrayWithFlips = getCardArrayWithFlips(cardArrayWithoutFlips)
    cardMap = getCardMap(cardArrayWithFlips)

    # check if you can "Add 'Em Up!"
    for card in cardArrayWithFlips:
        desiredCard = desiredSum - card
        if desiredCard in cardMap:
            if not (isCardFlipable(desiredCard)):
                return "YES"
            elif not (int(flipCard(desiredCard)) == card):
                return "YES"
    return "NO"


if __name__ == "__main__":
    result = main()
    print(result)
