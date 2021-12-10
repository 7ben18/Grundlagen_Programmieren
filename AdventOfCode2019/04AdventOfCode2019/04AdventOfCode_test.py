def checkdouble(num):
    for i in range(len(num) - 1):
        for a in range(len(num) - 1):
            n = num[i]
            n2 = num[a + 1]
            if num[i] == num[a + 1]:
                return True
            else:
                return False

print(checkdouble("1000"))
print(checkdouble("5903"))