# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/addemup
# Complexity: O(N) where N is the number of cards


# card object to store a card's number and id
class cardObject:
    def __init__(self, number, id):
        self.number = number
        self.id = id


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
# @param: cardObject array
# @return: cardObject array
def getCardObjectArrayWithFlips(cardArray):
    resultArray = []
    id = 0
    for card in cardArray:
        nonFlippedCard = card
        resultArray.append(cardObject(nonFlippedCard, id))
        if (isCardFlipable(card)):
            flippedCard = int(flipCard(card))
            resultArray.append(cardObject(flippedCard, id))
        id += 1
    return resultArray


# create a card hashmap/dictionary
# @param: cardObject array
# @return: int dictionary
def getCardMap(cardObjectArray):
    resultMap = {}
    for cardObj in cardObjectArray:
        resultMap[cardObj.number] = cardObj.id
    return resultMap


# main method to solve the problem
def main():
    # read & store input
    desiredSum = int(input("").split()[1])
    cardArrayWithoutFlips = [int(number) for number in input("").split()]
    cardObjectArrayWithFlips = getCardObjectArrayWithFlips(
        cardArrayWithoutFlips)
    cardMap = getCardMap(cardObjectArrayWithFlips)

    # check if you can "Add 'Em Up!"
    for cardObj in cardObjectArrayWithFlips:
        desiredCard = desiredSum - cardObj.number
        if desiredCard in cardMap:
            if not (cardMap[desiredCard] == cardObj.id):
                return "YES"
    return "NO"


# call the main method
if __name__ == "__main__":
    result = main()
    print(result)
