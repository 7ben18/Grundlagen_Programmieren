"""
++ 6 Stellige Zahl wird gesucht
++ Es gibt zwei zahlen die gleich sind und nebeneinander
++ Die Zahl steigt nur in der Spannweite!

"""

range_start = 145852
range_end = 616942
count_num = range_end - range_start
print(count_num)

def checklen(num):
    return len(num) == 6

def checkincrease(num):
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            return False
        else:
            return True

def checkdouble(num):
    for i in range(len(num) - 1):
        for a in range(len(num) - 1):
            if num[i] == num[a + 1]:
                return True
            else:
                return False

valid_pass = 0
invalid_pass = 0

for i in range(range_start, range_end):
    if checklen(str(i)) and checkincrease(str(i)) and checkdouble(str(i)):
        valid_pass += 1
    else:
        invalid_pass += 1


print(valid_pass)
