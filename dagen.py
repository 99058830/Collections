weekDagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print('-- Alle dagen')
for x in range(len(weekDagen)): 
    print(weekDagen[x])

print('-- Werkdagen')
for x in (weekDagen)[:-2]:
    print(x)

print('-- Weekend')
for x in (weekDagen)[-2:]:
    print(x)

print('-- Dagen omgekeerd')
for x in reversed(weekDagen):
    print(x)

print('-- Werkdagen omgekeerd')
weekDagen.reverse()
for x in (weekDagen)[-5:]:
    print(x)
weekDagen.reverse()

print('-- Weekend omgekeerd')
weekDagen.reverse()
for x in (weekDagen)[:2]:
    print(x)