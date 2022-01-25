from random import randint

mmList = ['rood','oranje','groen','blauw','geel','bruin']

def mmZak(amount):
    results = []
    for i in range(amount):
        results.append(mmList[randint(0,5)])
    return results

def main():
    amount = int(input("hoeveel M&M's? "))
    if amount > 0:
        print(*mmZak(amount),sep='\n')
    elif type(amount):
        print('Geen getal') 
        main()

main()