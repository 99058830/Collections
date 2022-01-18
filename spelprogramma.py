from random import randint

spelList = ['Monoply','Yathzee','Bridge','Poker','Pesten','Mens erger je niet','Cluedo']

def spelProgramma(spelList, minimum=3, maximum=10):
    list = []
    for i in range(randint(minimum, maximum)):
        list.append(spelList[randint(0,len(spelList)-1)])
    return list

print(*spelProgramma(spelList),sep='\n')