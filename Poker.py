#suits = ['Hearts', "Diamonds", "Spades", "Clubs"]
#ranks = ['2', "3", "4", "5", "6", "J", "Q", "K", "A"]
#deck = []
#for suit in suits:
#    for rank in ranks:
#        deck.append(rank + ' of ' + suit)
#print(deck)
#import random
#numbers = [1, 2, 3, 4, 5]
#random.shuffle(numbers)
#print(numbers)



#numbers = [1, 2, 3, 4, 5]
#subset = numbers[0]
#print(subset)


#----------------------------------------------------------------

suits = ['Hearts', "Diamonds", "Spades", "Clubs"]
ranks = ['2', "3", "4", "5", "6", "J", "Q", "K", "A"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)

import random
random.shuffle(deck)

print("Welcome to the Five Card Draw game!")
print("Here are your initial 5 cards:")

hand = []
for i in range(5):
    card = deck.pop(0)
    hand.append(card)
    print(card)

while True:
    choice = input("\nDo you want to draw more cards? (y/n) ").lower()
    
    if choice == 'y':
        new_card = deck.pop(0)
        hand.append(new_card)
        print(f"You drew: {new_card}")
        print("Your updated hand:")
        for card in hand:
            print(card)
    elif choice == 'n':
        print("Thanks for playing! Your final hand:")
        for card in hand:
            print(card)
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")