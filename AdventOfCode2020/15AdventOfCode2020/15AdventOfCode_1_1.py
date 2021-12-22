startlist = [0, 3, 6]
dict = {}

for i, x in enumerate(startlist, 1):
    if startlist.count(startlist[-1]) == 1:
        startlist.append(0)
    elif startlist.count(startlist[-1]) != 1:
        for i in dict:
            if dict[i] == startlist[-1]:
                nums = i
    dict[i] = x
    if i == 2020:
        break
print(dict)

for i in dict:
    if dict[i] == 0:
        l = [i]
        print(l)



start = [0, 3, 6]

dict = {x: i for i, x in enumerate(start, 1)}
print(dict) #{0: 1, 3: 2, 6: 3}

if start.count(start[-1]) == 1:
    start.append(0)
print(start)
index_list = list(range(1,len(start)+1))
print(index_list)

