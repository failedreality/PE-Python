# video follow along for this week and the libraries section
import random


############################################################
# Random Choice                                                  
############################################################
# stores the random choice in var coin
# coin = choice(['Heads', 'Tails'])
# print(coin)

############################################################
# Randint                                                  
############################################################
number = random.randint(1,10)
print(number)

############################################################
# Random Shuffle              
############################################################
cards = ['jack', 'king', 'queen' ]
random.shuffle(cards)
print(cards) # prints the list in syntax format - need to for loop to print the actual shuffle

# will print the list nicely and shuffled
for x in cards:
    print(x)


# from - where you can specify which import module to the library
# if you do like from random import choice, then you dont need to specify random.choice and can just
# use choice as above.

# randint(a,b) - so like 1,10 - only includes those numbers.


