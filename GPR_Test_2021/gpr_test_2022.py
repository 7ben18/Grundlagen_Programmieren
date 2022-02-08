lst = [[1,2]] * 3
print(lst) #[[1, 2], [1, 2], [1, 2]]

lst[0][0] = 3
print(lst)

def prime_zerlegung(x, factor):
    cnt = 0
    while x % factor == 0:
        cnt += 1
        x = x / factor

    return cnt

print(prime_zerlegung(15,3))
print(prime_zerlegung(45,3))
