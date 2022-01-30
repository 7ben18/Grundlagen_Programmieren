# Aufgabe 1
print("a")
s = 0
sq = 0
for i in range(3):
    s, sq = s + i, sq + i * i
print(s, sq)

print("b")
def fun(a,b,c):
    a = b + c
    b = 0
    return a - c
a,b,c = 1,2,3
c = fun(a,b,c)
print(a,b,c)

print("c1")
lst = [[1,2,3],[4,5],[6]]
lst[2].append(len(lst[-1]))
print(lst)

print("c2")
l2 = lst[1]
l2[0] = 0
del lst[0]
print(l2)
print("c3")
print(lst)

print("d")
x = 5 ** 2 + 1
print(x < 20 or x > 30)
print((x < 20) == (x > 30))