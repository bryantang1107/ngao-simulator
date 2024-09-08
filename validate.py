def checkNgaoTongGu(valid_ngao):
    for i in range(len(valid_ngao)):
        exists = any(card['score'] == 1 and card['pattern'] == '♠' for card in valid_ngao[i]["top"])
        if exists:
            exists = any(card['card'] in globals.pictures for card in valid_ngao[i]["top"])
        if exists:
            return valid_ngao[i]
    return None

def checkTriple(valid_ngao):
    highestCard = {"rank" : 0}
    index = None 

    for i in range(len(valid_ngao)):
        if valid_ngao[i]["top"][0]["card"] == valid_ngao[i]["top"][1]["card"]:
            if valid_ngao[i]["top"][0]["rank"] > highestCard["rank"]:
                highestCard = valid_ngao[i]["top"][0]
                index = i
    return [valid_ngao[index], highestCard["card"]] if index is not None else [None, None]

def checkDouble(valid_ngao):
    for i in range(len(valid_ngao)):
        if (valid_ngao[i]["top"][0]["score"] + valid_ngao[i]["top"][1]["score"]) % 10 == 0:
            return valid_ngao[i]
    return None 

def checkNormal(valid_ngao):
    highestCard = 0
    index = None
    for i in range(len(valid_ngao)):
        topLeft = valid_ngao[i]["top"][0]
        topRight = valid_ngao[i]["top"][1]
        total = topLeft["score"] + topRight["score"]
        if (total % 10) > highestCard:
            highestCard = total % 10
            index = i
        if topLeft["card"] == "3":
            total = topRight["score"] + 6
            if (total % 10) > highestCard:
                highestCard = total % 10
                index = i
        if topRight["card"] == "3":
            total = topLeft["score"] + 6
            if (total % 10) > highestCard:
                highestCard = total % 10
                index = i
        if topLeft["card"] == "6":
            total = topRight["score"] + 3
            if (total % 10) > highestCard:
                highestCard = total % 10
                index = i
        if topRight["card"] == "6":
            total = topLeft["score"] + 3
            if (total % 10) > highestCard:
                highestCard = total % 10
                index = i
    return [valid_ngao[index], highestCard] if index is not None else [None, None]