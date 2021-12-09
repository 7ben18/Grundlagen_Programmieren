"""
++ Von jeder Zahl die Nachbarn anschauen! Oben unten rechts links
++ Wenn die Zahl gleich oder hoeher ist, FALSE
++ Wenn die Zahl tiefer ist, TRUE und in eine Liste packen und zu jedem El +1
++ Summe der Liste = Resultat

-- einlesen
--

"""
def einlesen(data):
    with open(data) as f:
        return f.read().split("\n")

testdata = einlesen("09testdata")
#print(testdata)
#['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']

def get_numb(list):
    for i in range(len(list)):
        for y in range(len(list[i])):
            if list[i] != list[0] or list[i] != list[-1]:
                nums = list[i][y]
                num_left, num_right = list[i][y-1], list[i][y+1]
                num_down, num_up = list[i+1][y], list[i-1][y]
                if nums < num_left and nums < num_right and nums < num_up and nums < num_down:
                    return nums

print(get_numb(einlesen("09testdata")))