listOne = ["1","2","3","4","5","6","7","8","9","10"]
listTwo = ["2","4","6","8","10","12","14","16","18","20"]

listOne = [int(i) for i in listOne]
listTwo = [int(i) for i in listTwo]

def addAndDisplayLists (listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(listOne[i] + listTwo[i])
    return results

print('--------------------')
for i in range(len(listOne)):
    print(listOne[i], "+", listTwo[i], "=", addAndDisplayLists(listOne, listTwo)[i])

def substractAndDisplayLists (listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(listOne[i] - listTwo[i])
    return results

print('--------------------')
for i in range(len(listOne)):
    print(listOne[i], "-", listTwo[i], "=", substractAndDisplayLists (listOne, listTwo)[i])

def multiplyAndDisplayLists (listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(listOne[i] * listTwo[i])
    return results

print('--------------------')
for i in range(len(listOne)):
    print(listOne[i], "*", listTwo[i], "=", multiplyAndDisplayLists (listOne, listTwo)[i])

def divideAndDisplayLists (listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(listOne[i] / listTwo[i])
    return results

print('--------------------')
for i in range(len(listOne)):
    print(listOne[i], "/", listTwo[i], "=", divideAndDisplayLists  (listOne, listTwo)[i])