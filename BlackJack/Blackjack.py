import random

Type = ["Clubs", "Diamonds", "Hearts", "Spades"]
Number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

playAgain = "Yes"
userInput = ""

while playAgain == "Yes":
    Tokens = 1000

    Bet = int(input(f"How much would you like to bet? (You have {Tokens} tokens.): "))
    while Tokens - Bet < 0:
        print()
        print("You don't have enough tokens to bet that amount.")
        Bet = input(f"How much would you like to bet? (You have {Tokens} tokens.): ")
    Tokens -= Bet
    print(f"Your token balance has changed to: {Tokens}.")
    usedCards = []
    playerCards = []

    #first hands

    playerCard1Type = random.choice(Type)
    playerCard1Number = random.choice(Number)
    usedCards.append((playerCard1Number, playerCard1Type))
    playerCards.append(playerCard1Number)
    playerCard2Type = random.choice(Type)
    playerCard2Number = random.choice(Number)
    while (playerCard2Number, playerCard2Type) in usedCards: #ensures no duplicate cards
        playerCard2Type = random.choice(Type)
        playerCard2Number = random.choice(Number)
    usedCards.append((playerCard2Number, playerCard2Type))
    playerCards.append(playerCard2Number)
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

    print(f"Your hand is: {playerCard1Number} of {playerCard1Type} ({playerCard1Value}) and {playerCard2Number} of {playerCard2Type} ({playerCard2Value}).")
    print(f"The total value of your hand is: {sum(playerCardValues)}")
    print()
    print(f"The dealers hand is: {dealerCard1Number} of {dealerCard1Type} ({dealerCard1Value}) and -- of -- (-).")
    print()

    #checks for duplicates in players hand
    Finished = False
   
    dupe = None
    DupeList = []
    seen = set()
    for i in playerCards:
        if i in seen:
            dupe = True
            DupeList.append(dupe)
        else:
            dupe = False
            DupeList.append(dupe)
        seen.add(i)

    while Finished is False:
        if True in DupeList and len(dealerCardValues) == 2:
            userInput = input("Would you like to Stand, Hit, Split, Double or Surrender: ").strip().capitalize()
            while userInput not in ["Stand", "Hit", "Split", "Double", "Surrender"]:
                userInput = input("Would you like to Stand, Hit, Split, Double or Surrender: ").strip().capitalize()
        else:
            userInput = input("Wouuld you like to Stand, Hit, Double or Surrender: ").strip().capitalize()
            while userInput not in ["Stand", "Hit", "Double", "Surrender"]:
                userInput = input("Would you like to Stand, Hit, Double or Surrender: ").strip().capitalize()

        if userInput == "Stand":
            print(f"The Dealer reveals his cards: {dealerCard1Number} of {dealerCard1Type} ({dealerCard1Value}) and {dealerCard2Number} of {dealerCard2Type} ({dealerCard2Value}.)")
            print(f"The total value of the dealers hand is: {sum(dealerCardValues)}")
            while sum(dealerCardValues) <= 16:
                print("The Dealer hits!")
                dealerNewCardNumber = random.choice(Number)
                dealerNewCardType = random.choice(Type)
                while (dealerNewCardNumber, dealerCard1Type) in usedCards:
                    dealerNewCardNumber = random.choice(Number)
                    dealerNewCardType = random.choice(Type)
                usedCards.append((dealerNewCardNumber, dealerNewCardType))

                if dealerNewCardNumber in ["Jack", "Queen", "King"]:
                    dealerNewCardValue = 10
                elif dealerNewCardNumber == "Ace":
                    dealerNewCardValue = 11
                    if sum(dealerCardValues) + dealerNewCardValue >= 22:
                        dealerNewCardValue = 1
                else:
                    dealerNewCardValue = int(dealerNewCardNumber)
                dealerCardValues.append(dealerNewCardValue)
                print()
                print(f"The dealers new card is: {dealerNewCardNumber} of {dealerNewCardType} ({dealerNewCardValue}).")
            if sum(dealerCardValues) < 22:
                print()
                print("The Dealer stands!")
                if sum(dealerCardValues) == sum(playerCardValues):
                    print("It's a tie!")
                    print("You've got your bet returned.")
                    Tokens += Bet
                    print(f"Your token balance has changed to: {Tokens}.")
                    Finished = True
                elif sum(dealerCardValues) < sum(playerCardValues):
                    print("You've won!")
                    print("Your winnings has been added to your balance!")
                    Tokens += Bet * 2
                    print(f"Your token balance has changed to: {Tokens}.")
                    Finished = True
                elif sum(dealerCardValues) > sum(playerCardValues):
                    print("You've lost!")
                    Finished = True
            if sum(dealerCardValues) >=22:
                print("The dealer has overshot!")
                print("You've won!")
                print("Your winnings has been adden to your balance.")
                Tokens += Bet * 2
                print(f"Your token balance has changed to: {Tokens}.")
                Finished = True

        elif userInput == "Hit":
            playerNewCardNumber = random.choice(Number)
            playerNewCardType = random.choice(Type)
            while (playerNewCardNumber, playerNewCardType) in usedCards:
                playerNewCardNumber = random.choice(Number)
                playerNewCardType = random.choice(Type)

            if playerNewCardNumber in ["Jack", "Queen", "King"]:
                playerNewCardValue = 10
            elif playerNewCardNumber == "Ace":
                playerNewCardValue = 11
            if sum(playerCardValues) + playerNewCardValue >= 22:
                playerNewCardValue = 1
            else:
                playerNewCardValue = int(playerNewCardNumber)

            playerCardValues.append(playerNewCardValue)
            playerCards.append(playerNewCardNumber)

            print()
            print(f"Your new card is: {playerNewCardNumber} of {playerNewCardType} ({playerNewCardValue}).")
            print(f"Your hand is: {playerCards}")

            if sum(playerCardValues) >= 22:
                print("You've busted!")
                Finished = True
        
        

    