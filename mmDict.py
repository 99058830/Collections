from random import randint
import random

mmList = ['oranje','groen','blauw','bruin']
mmDictionary = {}

def mmDict(amount):
    for i in range(amount):
        randomIndex = random.randrange(0, len(mmList))
        color = mmList[randomIndex]
        if color in mmDictionary:
            mmDictionary[color] += 1
        else:
            mmDictionary[color] = 1
    return mmDictionary

def main():
    global mmSelect
    amount = int(input("hoeveel M&M's? "))
    if amount > 0:
        print(mmDict(amount))
    else:
        print('Er is een probleem!')
        main()

main()