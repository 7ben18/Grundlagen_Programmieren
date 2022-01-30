"""
digit_1_len = 2
digit_4_len = 4
digit_7_len = 3
digit_8_len = 7

Pattern
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

 4444
1    2
1    2
 5555
6    3
6    3
 7777
"""

with open("08testdata_2") as f:
    line = f.readline().split()
    signal = line[0:10] #['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    code = line[-4:] #['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
"""
 4444
1    2
1    2
 5555
6    3
6    3
 7777
"""
    pattern = [1,2,3,4,5,6,7]
    encoded = []
    while line:
        encoded = []
        signal = line[0:10]

        for i in range(len(signal)):
            x = len(signal[i])
            if x == 2:
                encoded[i] = 2
            elif x == 3:
                encoded[i] = 7
            elif x == 4:
                encoded[i] = 4
            elif x == 7:
                encoded[i] = 8
            print(encoded)
        line = f.readline().split()




