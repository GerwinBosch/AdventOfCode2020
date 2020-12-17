def scannerForLength():
    validPassports = 0
    passportSegments = 0
    with open("./passports.txt") as fp:
        line = fp.readline().rstrip()
        while line:
            if len(line.rstrip()) == 0:
                if passportSegments == 7:
                    validPassports += 1
                passportSegments = 0
            else:
                passportSegments += len(
                    list(filter(lambda segment: not segment.startswith("cid"), line.split(" "))))
            line = fp.readline()
    if passportSegments == 7:
        validPassports += 1
    return validPassports


print("task1", scannerForLength())


def byrValidator(byr):
    return len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002


def iyrValidator(iyr):
    return len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020


def eyrValidator(eyr):
    return len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030


def hgtValidator(hgt):
    limits = [0, 0]
    if hgt.endswith("cm"):
        limits = [150, 193]
    elif hgt.endswith("in"):
        limits = [59, 76]
    else:
        return False
    number = int(hgt[:-2])
    return number <= limits[1] and number >= limits[0]


def hclValidator(hcl):
    if hcl[0] == "#" and len(hcl) == 7:
        try:
            int(hcl[1:], 32)
            return True
        except:
            return False
    return False


eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def eclValidator(ecl):
    return ecl in eyeColors


def pidValidator(pid):
    return len(pid) == 9 and int(pid)


def validationScanner():
    validPassports = 0
    passportSegments = 0
    with open("./passports.txt") as fp:
        line = fp.readline()
        passport = {}
        while line:
            if len(line.rstrip()) == 0:
                if len(passport) == 7:
                    try:
                        if byrValidator(passport["byr"]) and iyrValidator(passport["iyr"]) and eyrValidator(passport["eyr"]) and hgtValidator(passport["hgt"]) and hclValidator(passport["hcl"]) and eclValidator(passport["ecl"]) and pidValidator(passport["pid"]):
                            validPassports += 1
                    except:
                        print("INVALID")
                        # Do nothing
                passport = {}
            else:
                for item in line.rstrip().split(" "):
                    [code, value] = item.split(":")
                    if code == "cid":
                        continue
                    passport[code] = value
            line = fp.readline()
    if passportSegments == 7:
        validPassports += 1
    return validPassports


print("task2", validationScanner())
