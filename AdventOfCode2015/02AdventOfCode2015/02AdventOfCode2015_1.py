with open("02data") as f:
    line = f.readlines()
    liste = []
    for i in line:
        liste.append(i.strip().split("x"))

    z = []
    for i in range(len(liste)):
        subliste = []
        for x in liste[i]:
            subliste.append(int(x))
        z.append(sorted(subliste))
    print(z)

    cnt = 0
    for i in range(len(z)):
        cnt += (z[i][0] * z[i][1] * 2 + z[i][1] * z[i][2] * 2 + z[i][0] * z[i][2] * 2 + z[i][0] * z[i][1])
    print(cnt)