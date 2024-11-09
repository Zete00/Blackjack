import random

Type = ["Clubs", "Diamonds", "Hearts", "Spades"]
Number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

playAgain = "Yes"

if playAgain == "Yes":
    usedCards = []

    #first hands

    playerCard1Type = random.choice(Type)
    playerCard1Number = random.choice(Number)
    usedCards.append((playerCard1Number, playerCard1Type))
    playerCard2Type = random.choice(Type)
    playerCard2Number = random.choice(Number)
    while (playerCard2Number, playerCard2Type) in usedCards: #ensures no duplicate cards
        playerCard2Type = random.choice(Type)
        playerCard2Number = random.choice(Number)
    usedCards.append((playerCard2Number, playerCard2Type))
    dealerCard1Type = random.choice(Type)
    dealerCard1Number = random.choice(Number)
    while (dealerCard1Number, dealerCard1Type) in usedCards: #ensures no duplicate cards
        dealerCard1Type = random.choice(Type)
        dealerCard1Number = random.choice(Number)
    usedCards.append((dealerCard1Number, dealerCard1Type))
    dealerCard2Type = random.choice(Type)
    dealerCard2Number = random.choice(Number)
    while (dealerCard2Number, dealerCard2Type) in usedCards: #ensures no duplicate cards
        dealerCard2Type = random.choice(Type)
        dealerCard2Number = random.choice(Number)
    usedCards.append((dealerCard2Number, dealerCard2Type))
    
    dealerCardValues = []
    playerCardValues = []

    if dealerCard1Number in ["Jack", "Queen", "King"]:
        dealerCard1Value = 10
    elif dealerCard1Number == "Ace":
        dealerCard1Value = 11
    else:
        dealerCard1Value = int(dealerCard1Number)
    dealerCardValues.append(dealerCard1Value)

    if dealerCard2Number in ["Jack", "Queen", "King"]:
        dealerCard2Value = 10
    elif dealerCard2Number == "Ace":
        dealerCard2Value = 11
        if dealerCard1Value + dealerCard2Value >= 22:
            dealerCard2Value = 1
    else:
        dealerCard2Value = int(dealerCard2Number)
    dealerCardValues.append(dealerCard2Value)
    
    if playerCard1Number in ["Jack", "Queen", "King"]:
        playerCard1Value = 10
    elif playerCard1Number == "Ace":
        playerCard1Value = 11
    else:
        playerCard1Value = int(playerCard1Number)
    playerCardValues.append(playerCard1Value)

    if playerCard2Number in ["Jack", "Queen", "King"]:
        playerCard2Value = 10
    elif playerCard2Number == "Ace":
        playerCard2Value = 11
        if playerCard1Value + playerCard2Value >= 22:
            playerCard2Value = 1
    else:
        playerCard2Value = int(playerCard2Number)
    playerCardValues.append(playerCard2Value)
    