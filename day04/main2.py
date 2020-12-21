f = open("P:\\workspace\\advent_of_code\\day4\\input.txt")
lines = f.readlines()
current_batch = []
current_credentials = {}

valid_passports = 0
invalid_passports = 0

needed_elements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_len(string, length):
    if len(string) != length:
        return False
    return True

def check_bounds(string, lowest, highest):
    if int(string) < lowest or int(string) > highest:
        return False
    return True

def check_credentials(credentials):
    if "byr" not in credentials.keys() or not check_len(credentials["byr"], 4) or not check_bounds(credentials["byr"], 1920, 2002):
        return False
    if "iyr" not in credentials.keys() or not check_len(credentials["iyr"], 4) or not check_bounds(credentials["iyr"], 2010, 2020):
        return False
    if "eyr" not in credentials.keys() or not check_len(credentials["eyr"], 4) or not check_bounds(credentials["eyr"], 2020, 2030):
        return False
    if "hgt" in credentials.keys():
        string = credentials["hgt"]
        if string[len(string)-2:len(string)] == "in":
            num = string.rstrip("in")
            if not check_bounds(num, 59, 76):
                return False
        elif string[len(string)-2:len(string)] == "cm":
            num = string.rstrip("cm")
            if not check_bounds(num, 150, 193):
                return False
        else:
            return False
    else:
        return False
    if "hcl" in credentials.keys():
        string = credentials["hcl"]
        allowed_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        if len(string) == 7 and string[0] == "#":
            for i in range(1,7):
                if string[i] not in allowed_chars:
                    return False
        else:
            return False
    else: 
        return False
    if "ecl" in credentials.keys():
        allowed_strings = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if credentials["ecl"] not in allowed_strings:
            return False
    else:
        return False
    if "pid" in credentials.keys():
        allowed_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        string = credentials["pid"]
        if len(string) == 9:
            for char in string:
                if char not in allowed_chars:
                    return False
        else:
            return False
    else:
        return False
    return True


def add(valid):
    global valid_passports, invalid_passports, current_batch, current_credentials
    current_batch = []
    current_credentials = {}
    if valid is True:
        valid_passports += 1
    else:
        invalid_passports += 1

for line in lines:
    if line == "\n":
        for batchline in current_batch:
            elements = batchline.split(" ")
            for element in elements:
                title = element.split(":")[0]
                value = element.split(":")[1]
                value = value.rstrip("\n")
                current_credentials[title] = value

        if not check_credentials(current_credentials):
            add(False)
                
        if current_batch != []:
            add(True)
        
    else:
        current_batch.append(line)
        continue

print("i have %d valid and %d invalid passports." % (valid_passports, invalid_passports))