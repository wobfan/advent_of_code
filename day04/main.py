f = open("P:\\workspace\\advent_of_code\\day4\\input.txt")
lines = f.readlines()
current_batch = []
current_credentials = {}

passports = 0
valid_passports = 0
invalid_passports = 0

needed_elements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in lines:
    if line == "\n":
        passports += 1
        for batchline in current_batch:
            elements = batchline.split(" ")
            for element in elements:
                title = element.split(":")[0]
                value = element.split(":")[1]
                value = value.rstrip("\n")
                current_credentials[title] = value

        for needed in needed_elements:
            if needed not in current_credentials.keys():
                invalid_passports += 1
                current_batch = []
                current_credentials = {}
                break
                
        if current_batch != []:
            current_batch = []
            current_credentials = {}
            valid_passports += 1
        
    else:
        current_batch.append(line)
        continue

print("in %d passports i have %d valid and %d invalid passports." % (passports, valid_passports, invalid_passports))