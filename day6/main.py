lines = open("day6/input.sql").readlines()

current_batch = []
sum_of_yes = 0

for line in lines:
    if line == "\n":
        questions = []
        for batch_line in current_batch:
            batch_line = batch_line.rstrip("\n")
            for char in batch_line:
                if char not in questions:
                    questions.append(char)
        sum_of_yes += len(questions)
        current_batch = []
    else:
        current_batch.append(line)

print("sum of answers that anyone had: %d" % sum_of_yes)