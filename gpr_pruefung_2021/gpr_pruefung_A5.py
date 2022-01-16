# Aufgabe 5a
def is_ok(temperature, status):
    t = temperature
    s = status
    if s == "ok" and t >= -10 and t <= 44:
        return True
    elif s == "off" and t == 0:
        return True
    elif s == "fault":
        return True
    else:
        return False

print(is_ok(30, "ok"))
print(is_ok(-10, "ok"))
print(is_ok(-11, "ok"))
print(is_ok(-11, "off"))
print(is_ok(0, "off"))
print(is_ok(90, "fault"))

# Aufgabe 5b
def count_errors(file_name):
    with open(file_name) as f:
        lst = [x.split() for x in f]
        cnt = 0
        for x in lst:
            if is_ok(int(x[2][:-1]),x[3]) == False:
                cnt += 1
        return cnt

print(count_errors("gpr_pruefung_A5_datei"))

# Aufgabe 5c
def count_errors_mult(file_names):
    cnt = 0
    for datei in file_names:
        cnt += count_errors(datei)
    return cnt

print(count_errors_mult(["gpr_pruefung_A5_datei","gpr_pruefung_A5_datei","gpr_pruefung_A5_datei"]))