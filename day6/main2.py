lines = open("day6/input.sql").readlines()

current_batch = []
sum_of_yes = 0

mode = "append"

current_line = 0

for line in lines:
    if line == "\n":
        mode = "append"
        questions = []
        for batch_line in current_batch:
            batch_line = batch_line.rstrip("\n")
            if mode == "append":
                for char in batch_line:
                    if char not in questions:
                        questions.append(char)
                mode = "remove"
            elif mode == "remove":
                for char in questions:
                    if char not in batch_line:
                        questions.remove(char)
        sum_of_yes += len(questions)
        print("in lines %d to %d i had %d matching answers: %s" % (current_line-len(current_batch), current_line, len(questions), questions))
        current_batch = []
    else:
        current_batch.append(line)
    current_line += 1

print("sum of answers that everyone had: %d" % sum_of_yes)