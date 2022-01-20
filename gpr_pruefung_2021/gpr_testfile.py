lst = [1,1,1,3,4,5,6]
def heuristic(n):
    thisdict = {
    }
    for i in n:
        x = 0
        for y in n:
            if y == i:
                x += 1
        thisdict[i] = x
    return thisdict
print(heuristic(lst))
#{1: 3, 3: 1, 4: 1, 5: 1, 6: 1}