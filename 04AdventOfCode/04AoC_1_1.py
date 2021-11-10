"""
- Datei einlesen
- Gruppen separieren
- vorderen Teil des String extrahieren
- alle verlangten Strings vorhanden
"""
keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
hex_num = {"1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"}
nums = {"1","2","3","4","5","6","7","8","9","0"}

def hgt_ok(s):
    return (s[-2:] == 'cm' and 150 <= int(s[:-2]) <= 193) or (s[-2:] == 'in' and 59 <= int(s[:-2]) <= 76)

def hcl_ok(s):
    return s[0] == '#' and len(s[1:]) == 6 and {c for c in s[1:]}.issubset(hex_num)

def pid_ok(s):
    return {x for x in s[0]}.issubset(nums)

def passport_valid_1(passport):
    return keys.issubset(passport.keys())

def passport_valid_2(passport):
    return passport_valid_1(passport) and 1920 <= int(passport['byr']) <= 2002 and hgt_ok(passport['hgt']) \
    and hcl_ok(passport['hcl']) and passport['ecl'] in ecls and pid_ok(passport['pid']) \
    and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030


def run_task(file_name: str, passport_valid: callable) -> int:
    cnt = 0
    with open(file_name) as f:
        line = f.readline()
        while len(line) != 0:
            passport = {}
            while len(line) > 1:
                for x in line.split():
                    x = x.split(':')
                    passport[x[0]] = x[1]
                line = f.readline()
            if passport_valid(passport):
                cnt += 1
            line = f.readline()
    return cnt


if __name__ == '__main__':
    print(run_task('04AoC_2_data', passport_valid_1))
    print(run_task('04AoC_2_data', passport_valid_2))




