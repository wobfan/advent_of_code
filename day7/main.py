class Bag():
    def __init__(self, color):
        self.bagColor = color
        self.bagContains = {}
        self.bagIsIn = {}

    def add(self, bag, amount):
        self.bagContains[bag] = amount

    def addToIsIn(self, bag, amount):
        self.bagIsIn[bag] = amount

    def contains(self, bag):
        if bag in self.bagContains:
            return True
        else:
            for recursiveBag in self.bagContains:
                return recursiveBag.contains(bag)
            return False


bags = {}

f = open("advent_of_code/day7/input.sql")
lines = f.readlines()

for line in lines:
    color = line.split(" bags contain ")[0]
    bags[color] = Bag(color)

for line in lines:
    line = line.split(" bags contain ")
    originColor = line[0]

    line[1] = line[1].rstrip(".\n")
    containsStrings = line[1].split(", ")
    
    if "no other bags" in containsStrings:
        continue

    for containsString in containsStrings:
        amount = int(containsString[0])
        color = containsString[2:]              # remove amount
        if color[len(color)-1] == 's':             
            color = color[0:len(color)-1]       # remove s at end of plural
        color = color[0:len(color)-4]           # remove ' bags'
        bags[originColor].add(bags[color], amount)
        bags[color].addToIsIn(bags[originColor], amount)
    

amountContaining = 0
for color in bags:
    if bags[color].contains(bags["shiny gold"]) is True:
        print("%s contains at least one shiny gold bag." % color)
        amountContaining += 1

print("that makes %d bags that may contain it." % amountContaining)