import sys
# split the puzzle input by newline
puzzle_input = open("input", "r").read().split("\n")
# strip any remaining whitespace and turn each value into an int
puzzle_input = [int(e.strip()) for e in puzzle_input]

# loop through all values to get desired output
for num1 in puzzle_input:
    for num2 in puzzle_input:
        for num3 in puzzle_input:
            if num1 + num2 + num3 == 2020:
                # print out the product and exit
                print(num1 * num2 * num3)
                sys.exit(0)