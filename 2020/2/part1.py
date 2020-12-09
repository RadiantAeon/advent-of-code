import sys
# split the puzzle input by newline
puzzle_input = open("input", "r")

valid = 0
for line in puzzle_input:
    # each line looks like this:
    # 1-3 a: abcde

    # get the min and max amount of occurences
    min = int(line.split("-")[0])
    max = int(line.split(" ")[0].split("-")[1])

    # get the letter we need to check for
    letter = line.split(" ")[1][0]
    # get the password
    password = line.split(": ")[1]

    print(f"min is {min} and max is {max} for letter {letter}. the password is {password}")
    # check if it is a valid password
    if min <= password.count(letter) <= max:
        valid += 1
        print("It is valid")
    else:
        print("It is not valid")
print(valid)