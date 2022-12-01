#########################
# Advent of Code - 2022 #
#        Day 01         #
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
    
    counter = 0
    highest = 0

    for item in data:
        if len(item) > 0:
            counter += int(item)
        else:
            if counter > highest:
                highest = counter
            counter = 0

    result = highest
    show_result(1,result)


# Part 2 logic
def part2():

    inventory = []
    counter = 0

    for item in data:
        if len(item) > 0:
            counter += int(item)
        else:
            inventory.append(counter)
            counter = 0

    
    x=sorted(inventory, reverse=True)
    print(x[0])
    
    result = x[0] + x[1] + x[2]
    show_result(2,result)
    
#####################



##### MAIN #####
# Get input data
data = get_input_data("input")

# Get answer for part 1/2
part1()
part2()
################