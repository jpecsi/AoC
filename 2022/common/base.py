#########################
# Advent of Code - 2022 #
#        Day XX         #
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
    result = ""
    show_result(1,result)


# Part 2 logic
def part2():
    result = ""
    show_result(2,result)
#####################



##### MAIN #####
# Get input data
data = get_input_data("input")

# Get answer for part 1/2
part1()
part2()
################