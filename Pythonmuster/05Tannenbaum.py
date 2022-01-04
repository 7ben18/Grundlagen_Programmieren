def tannenbaum(hoehe, stammhoehe):
    for x in range(1, hoehe + 1):
        print(" " * (hoehe - x) + "#" * (2 * x - 1) + " " * (hoehe - x))
    for a in range(stammhoehe):
        print(" " * (hoehe - 1) + "#")

tannenbaum(7,4)