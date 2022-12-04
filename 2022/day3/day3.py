#########################
# Advent of Code - 2022 #
#        Day 03         #
#########################



##### FUNCTIONS #####
# Read input file
def get_input_data(fn):
    d = []
    with open(fn) as file:
        for line in file:
            d.append(line.rstrip())
    return d


# Print result
def show_result(p,r):
    print("[PART " + str(p) + "] Result: " + str(r))


# Part 1 logic
def part1():
    result = 0
    
    for line in data:
        found = []
        split = int(len(line)/2)
        comp1 = line[0:split]
        comp2 = line[split:]
        for c in comp1:
            if c in comp2 and c not in found:
                found.append(c)
                result += (p.index(c)+1)
    show_result(1,result)


# Part 2 logic
def part2():
    result = 0

    count = 0
    found = []
    temp = []
    for line in data:
        count += 1
        temp.append(line)
        if count == 3:
            for c in temp[0]:
                if c in temp[1] and c in temp[2] and c not in found:
                    found.append(c)
                    result += (p.index(c)+1)
        
            temp = []
            found = []
            count = 0


    show_result(2,result)
#####################



##### MAIN #####
# Get input data
data = get_input_data("input")

# Priorities
p = [
    "a","b","c","d","e","f","g","h","i","j","k",
    "l","m","n","o","p","q","r","s","t","u","v",
    "w","x","y","z","A","B","C","D","E","F","G",
    "H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z"
    ]

# Get answer for part 1/2
part1()
part2()
################