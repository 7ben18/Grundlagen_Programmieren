"""
digit_1 = 2
digit_4 = 4
digit_7 = 3
digit_8 = 7
"""
with open("08data") as f:
    line = f.readline().split()[-4:]
    #print(line)

    cnt = 0
    while line:
        for el in line:
            x = len(el)
            if x == 2 or x == 4 or x == 3 or x == 7:
                cnt += 1
        line = f.readline().split()[-4:]
    print(cnt)