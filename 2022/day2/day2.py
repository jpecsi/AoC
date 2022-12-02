#########################
# Advent of Code - 2022 #
#        Day 02         #
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
    for round in data:
        play = round.split(' ')
        result += scoring[play[1]]
        
        if winning[play[0]] == play[1]:
            result += 6
        elif scoring[play[0]] == scoring[play[1]]:
            result += 3


    show_result(1,result)


# Part 2 logic
def part2():

    match = {
        "X":0,
        "Y":3,
        "Z":6
    }

    result = 0
  
    for round in data:
        play = round.split(' ')
        result += match[play[1]]

        if play[1] == "X":
            result += scoring[loss[play[0]]]
        
        if play[1] == "Z":
            result += scoring[winning[play[0]]]
            
        if play[1] == "Y":
            result += scoring[play[0]]
        

    show_result(2,result)

#####################



##### MAIN #####
# Get input data
data = get_input_data("input")

# Reference data
scoring = {
    "A":1,
    "B":2,
    "C":3,
    "X":1,
    "Y":2,
    "Z":3,
}

winning = {
    "A":"Y",
    "B":"Z",
    "C":"X"
}

loss = {
    "A":"Z",
    "B":"X",
    "C":"Y"
}

# Get answer for part 1/2
    # A = Rock / B = Paper / C = Scissors
    # X = Rock / Y = Paper / Z = Scissors
    # Rock = 1pt / Paper = 2pt / Scissors = 3pt
    # Round Score: Loss = 0 / Draw = 3 / Win = 6
part1()
part2()
################