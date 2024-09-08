from validate import checkNgaoTongGu, checkTriple, checkDouble, checkNormal
import globals

def drawCard(cardList, randomCards):
    for card in randomCards:
        cardList.append({
            "card" : card[0],
            "score" : getPoint(card[0]),
            "rank" : getRank(card[0]),
            "pattern" : globals.pattern_logo[card[1]]
        })
    return cardList

def getPoint(card):
    if card == "A": return 1
    if card.isdigit(): return int(card)
    return 10

def getRank(card):
    if card == "A": return 14
    if card == "K": return 13
    if card == "Q": return 12
    if card == "J": return 11
    return int(card)

def calculateScore3Cards(cards):
    total = 0
    is3Times = True
    is5Times = False
    if cards[0]["card"] == cards[1]["card"] == cards[2]["card"]:
        is5Times = True
    for card in cards:
        if card["card"] not in globals.pictures:
            is3Times = False
        total += getPoint(card["card"])

    if is5Times: return "5 倍"
    if is3Times: return "3 倍"
    if total % 10 == 0: return "2 倍"
    return f"{total % 10} 点"

def calculateScore5Cards(cards):
    valid_ngao = getValidNgao(cards)
    if len(valid_ngao) == 0: return [None, "没 NGAO"]

    result = checkNgaoTongGu(valid_ngao)
    if result is not None:
        return [result, "5 倍"]
    [result, highestCard] = checkTriple(valid_ngao)
    if result is not None:
        return [result,f"{highestCard} 点 3 倍"]
    result = checkDouble(valid_ngao)
    if result is not None:
        return [result, "2 倍"]
    [result, highestCard] = checkNormal(valid_ngao)
    if result is not None:
        return [result,f"{highestCard} 点"]

def getValidNgao(cardList):
    combinations = []

    for i in range(len(cardList)):
        for l in range(i + 1, len(cardList)):
            for k in range(l + 1, len(cardList)):
                total = cardList[i]["score"] + cardList[l]["score"] + cardList[k]["score"]
                if total in globals.possible_base:
                    combinations.append({
                        "base" : [cardList[i], cardList[l], cardList[k]],
                        "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                        })
                else:
                    #change one 
                    if cardList[i]["card"] == "3":
                        total = 6 + cardList[l]["score"] + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[l]["card"] == "3":
                        total = 6 + cardList[i]["score"] + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[k]["card"] == "3":
                        total = 6 + cardList[i]["score"] + cardList[l]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                   
                    if cardList[i]["card"] == "6":
                        total = 3 + cardList[l]["score"] + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[l]["card"] == "6":
                        total = 3 + cardList[i]["score"] + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[k]["card"] == "6":
                        total = 3 + cardList[i]["score"] + cardList[l]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })

                    #change two
                    if cardList[i]["card"] == "3" and cardList[l]["card"] == "3":
                        total = 6 + 6 + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[i]["card"] == "3" and cardList[k]["card"] == "3":
                        total = 6 + 6 + cardList[l]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[l]["card"] == "3" and cardList[k]["card"] == "3":
                        total = 6 + 6 + cardList[i]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[i]["card"] == "6" and cardList[l]["card"] == "6":
                        total = 3 + 3 + cardList[k]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[i]["card"] == "6" and cardList[k]["card"] == "6":
                        total = 3 + 3 + cardList[l]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
                    if cardList[l]["card"] == "6" and cardList[k]["card"] == "6":
                        total = 3 + 3 + cardList[i]["score"]
                        if total in globals.possible_base:
                            combinations.append({
                                "base" : [cardList[i], cardList[l], cardList[k]],
                                "top" : [card for j, card in enumerate(cardList) if j not in {i, l, k}]
                                })
    return combinations