"""
-- Daten einlesen
-- die ersten 3 Zahlen summieren, 0,1,2
-- die naechsten 3 Zahlen summieren 1,2,3
-- die beiden summen vergleichen, wenn die zweite summe groesser als die erste, + 1
"""

with open("testdata_01") as f:
    zahlenliste = [int(x) for x in f.read().split("\n")]
    #print(zahlenliste)

# Index sclicing 0 - 2, 1 - 3, 2 - 4 etc....

list = []
for i in range(len(zahlenliste)):
    list.append(zahlenliste[i:i+3])

print(list)

cnt = 0
for i in range(len(list) - 1):
   #print(sum(list[i]))
    if sum(list[i + 1]) > sum(list[i]):
        cnt += 1
print(cnt)
