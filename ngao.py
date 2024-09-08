import itertools
import random
from print import printPokerCard 
from utils import drawCard, calculateScore3Cards, calculateScore5Cards
import globals

def __init__():
    # Create the deck using itertools.product to get all combinations
    deck = list(itertools.product(globals.card_decks, globals.patterns))
    cards = []
    print("+-----------------------------+")
    print("|     FIRST ROUND             |")
    print("+-----------------------------+")

    first_round = random.sample(deck, 3)
    drawCard(cards, sorted(first_round))
    result = calculateScore3Cards(cards)
    print("+---------------------+")
    print("|     YOUR CARDS      |")
    print("+---------------------+")
    printPokerCard(cards)
    print("+---------------+")
    print("|     RESULT    |")
    print("|     ------    |")
    print(f"|      {result}     |")
    print("+---------------+")

    deck = [card for card in deck if card not in first_round] #filter used cards
    print("+-----------------------------+")
    print("|     SECOND ROUND            |")
    print("+-----------------------------+")
    second_round = random.sample(deck ,2)
    drawCard(cards, sorted(second_round))
    print("+---------------------+")
    print("|     YOUR CARDS      |")
    print("+---------------------+")
    printPokerCard(cards)
    [cards, result] = calculateScore5Cards(cards)
    if cards is not None:
        print("+-----------------------+")
        print("|     YOUR BEST HAND    |")
        print("+-----------------------+")
        printPokerCard(cards["top"])
        printPokerCard(cards["base"])
    if len(result) == 7:
        print("+---------------------+")
        print("|     RESULT          |")
        print("|     ------          |")
        print(f"|     {result}       |")
        print("+---------------------+")
    elif len(result) == 6:
        print("+-------------------+")
        print("|     RESULT        |")
        print("|     ------        |")
        print(f"|     {result}       |")
        print("+-------------------+")
    else:
        print("+---------------+")
        print("|     RESULT    |")
        print(f"|      {result}     |")
        print("+---------------+")
    return

__init__()