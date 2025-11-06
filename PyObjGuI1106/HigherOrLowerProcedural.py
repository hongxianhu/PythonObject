import random

SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE = (
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
)

NCARDS = 8


def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


print("欢迎来到《高低猜》.")
print("你必须选择下一张显示的牌是比当前牌更大还是更小.")
print("做对了加20分: 做错了扣15分。")
print("你有50分可以开始.")
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict["rank"]
    currentCardValue = currentCardDict["value"]
    currentCardSuit = currentCardDict["suit"]
    print(f"Starting card is:, {currentCardRank} of {currentCardSuit}")
    print()

    for cardNumber in range(0, NCARDS):
        answer = input(
            f"下一张牌会比 {currentCardSuit} 的 {currentCardRank} 大还是小? (输入 h 或 l) : "
        )
        answer = answer.casefoid()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict["rank"]
        nextCardValue = nextCardDict["value"]
        nextCardSuit = nextCardDict["suit"]
        print(f"下一张牌是:, {nextCardRank} of {nextCardSuit}")

        if answer == "h":
            if nextCardValue > currentCardValue:
                print("你答对了, 它更高.")
                score += 20
            else:
                print("抱歉, 它没有更高.")
                score -= 15
        elif answer == "l":
            if nextCardValue < currentCardValue:
                print("你答对了, 它更低.")
                score += 20
            else:
                print("抱歉, 它没有更低.")
                score -= 15

        print("你的分数是:", score)
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('要再次播放, 请按回车键, 或按 "q" 退出: ')
    if goAgain == "q":
        break

print("好的, 再见")
