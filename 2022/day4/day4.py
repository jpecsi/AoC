#########################
# Advent of Code - 2022 #
#        Day 04         #
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
        pairs = line.split(",")
        p1 = ([int(x) for x in pairs[0].split("-")])
        p2 = ([int(x) for x in pairs[1].split("-")])

        if p1[0] <= p2[0] and p1[1] >= p2[1]:
            result += 1
        elif p2[0] <= p1[0] and p2[1] >= p1[1]:
            result += 1

    show_result(1,result)


# Part 2 logic
def part2():
    result = 0

    for line in data:
        pairs = line.split(",")
        p1 = ([int(x) for x in pairs[0].split("-")])
        p2 = ([int(x) for x in pairs[1].split("-")])
        
        temp = []
        for i in range((p1[1]-p1[0])+1):
            temp.append(p1[0]+i)

        for i in range((p2[1]-p2[0])+1):
            temp.append(p2[0]+i)

        flag = 0
        for n in temp:
            if temp.count(n) > 1 and flag == 0:
                result += 1
                flag = 1

    show_result(2,result)
#####################



##### MAIN #####
# Get input data
data = get_input_data("input")

# Get answer for part 1/2
part1()
part2()
################