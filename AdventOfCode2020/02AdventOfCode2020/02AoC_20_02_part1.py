"""
Aufgabe:
Zaehle Zeilen in Datei,
fuer die Anzahl von Zeichen in Zeichenkette,
zwischen Untergrenze und Obergrenze eingeschlossen

1-3 a: abcde

1 = Untergrenze
3 = Obergrenze
a = 1 Zeichen
abcde = Zeichenkette

1) Datei lesen (Zeilen daraus)
2) String (Zeile aus Datei) zerlegen
3) Pruefen ob Zeichen "korrekt oft" in Zeichenkette ist
4) Korrekte Zeilen zaehlen
"""
# with open("Dateiname") as f, oeffnet die Datei
# f.read() liest die Datei ein
# f.readline() liest eine Zeile ein
# f.readlines() liest Zeile in gruppen ein
# .split() trennt den String und macht eine Liste daraus anhand vom Parameter .split("-")
# .strip() entfernt Am Anfang und Ende Leerzeichen, Tabulatoren, etc.. unnoetiges

def valid_1(line: str) -> bool:
    lst = line.strip().split("-")
    lst = [lst[0]] + lst[1].split()
    return psw_valid_1(int(lst[0]), int(lst[1]), lst[2][0], lst[3])

def psw_valid_1(lower: int, upper: int, x: chr, pwd: chr) -> bool:
    cnt = 0
    for i in pwd:
        if i == x:
            cnt += 1
    return cnt >= lower and cnt <= upper

def run_1():
    cnt = 0
    with open("password_list_part1") as f:
        line = f.readline()
        while line:
            if valid_1(line):
                cnt += 1
            line = f.readline()
    print(cnt)

def psw_valid_2(lower: int, upper: int, x: chr, pwd: chr) -> bool:
    cnt = pwd.count(x)
    return lower <= cnt and cnt <= upper
    # return lower <= cnt <= upper

def psw_valid_3(lower: int, upper: int, x: chr, pwd: chr) -> bool:
    return lower <= pwd.count(x) <= upper

def run_2():
    with open("password_list_part1") as f:
        lsg1 = len([line for line in f if valid_1(line)])
        lsg2 = sum(1 for line in f if valid_1(line))
    print(lsg1)

run_1()