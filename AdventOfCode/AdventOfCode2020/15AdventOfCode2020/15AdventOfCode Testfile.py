def twicenums(list):
    if list[-1] in list[:-1]:
        num = list[-1] - list.index(list[-1]) + 1
        list.append(num)
liste = [0,3,6,0]

print(twicenums(liste))