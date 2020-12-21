lines = open("day5/input.sql").readlines()

row_len = 128
column_len = 8

highest_seat_id = 0
seat_id_list = []

for line in lines:
    line = line.rstrip("\n")
    row_stream = line[0:7]
    column_stream = line[7:]
    current_range = [0,127]
    for char in row_stream:
        range_length = (abs(current_range[0] - current_range[1]) + 1) / 2
        if char == "F":
            current_range[1] -= range_length
        else:
            current_range[0] += range_length
    row = current_range[0]
    current_range = [0,7]
    for char in column_stream:
        range_length = (abs(current_range[0] - current_range[1]) + 1) / 2
        if char == "L":
            current_range[1] -= range_length
        else:
            current_range[0] += range_length
    column = current_range[0]
    seat_id = 8 * row + column
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    seat_id_list.append(seat_id)



for i in range(0,len(seat_id_list)):
    if i-1 in seat_id_list and i+1 in seat_id_list and i not in seat_id_list:
        print("missing seat between two occupied seats: %d" % i)