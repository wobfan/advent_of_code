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
                if recursiveBag.contains(bag):
                    return True
            return False

    def contains_amount(self):
        amount = 0
        for recursiveBag in self.bagContains:
            amount += recursiveBag.contains_amount()
        for key in self.bagContains.keys():
            amount += self.bagContains[key]
        print(f"{self.bagColor} contains {amount} bags.")
        return amount


bags = {}

f = open("day7/input.sql")
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
    

print("a single shiny gold bag requires %d bags in it." % bags["shiny gold"].contains_amount())