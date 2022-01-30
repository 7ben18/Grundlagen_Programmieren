with open("02data") as f:
    line = [x.strip().split("x") for x in f.readlines()]
    line2 = []
    for x in line:
        subline = []
        for a in x:
            subline.append(int(a))
        sub = sorted(subline)
        line2.append(sub)
    #print(line2)

    feet_of_ribbon = 0

    for el in line2:
        #print(el[0] * 2 + el[1] * 2)
        #print(el[2] * el[0] * el[1])
        feet_of_ribbon += el[0] + el[0] + el[1] + el[1] + (el[0] * el[1] * el[2])
    print(feet_of_ribbon)
