import time
rows = open("day11/input").readlines()

rows = [row.rstrip("\n") for row in rows]

hashes = ["", "#", "##", "###", "####"]

def replace_char(string, i, char):
    string_1 = string[:i]
    string_2 = string[i+1:]
    return string_1 + char + string_2

while True:
    changed_seats = 0
    for row in rows:
        print("jetzt neu:")
        time.sleep(2)
        for i in range(0, len(row)):
            length = len(row)
            left = i-1
            right = abs(i - length)-1
            print("char is %s" % row[i], end="")
            print(row)
            if row[i] == ".": 
                continue
            elif row[i] == "L":
                print("found an l")
                left_seat = False
                right_seat = True
                left_1 = 1 if left >= 1 else left
                right_1 = 1 if right >= 1 else right
                if left_1 == 1:
                    if row[i-1] != "#":
                        left_seat = True
                else:
                    left_seat = True
                if right_1 == 1:
                    if row[i+1] != "#":
                        right_seat = True
                else:
                    right_seat = True
                if right_seat == True and left_seat == True:
                    print("DBG changing %d from %s to %s" % (i, row[i], "#"))
                    row = replace_char(row, i, "#")
                    changed_seats += 1
            elif row[i] == "#":
                print("found a #")
                left_seats = False
                right_seats = False
                left_4 = 4 if left >= 4 else left
                right_4 = 4 if right >= 4 else right
                if left_4 >= 1:
                    print(f"{row[i-left_4:i]} : are all hashes? {row[i-left_4:i] == hashes[left_4]})")
                    if row[i-left_4:i] == hashes[left_4]:
                        left_seats = True
                else:
                    left_seats = True
                if right_4 >= 1:
                    if row[i+1:i+right_4] == hashes[right_4]:
                        right_seats = True
                else:
                    right_seats = True
                if right_seats == True and left_seats == True:
                    print("DBG changing %d from %s to %s" % (i, row[i], "L"))
                    replace_char(row, i, "L")
                    changed_seats += 1
    if changed_seats == 0:
        print("no seat has changed.")
        break