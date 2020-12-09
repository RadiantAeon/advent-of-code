import sys
# split the puzzle input by newline
puzzle_input = open("input", "r")

valid = 0
for line in puzzle_input:
    # each line looks like this:
    # 1-3 a: abcde

    # get the index1 and index2
    index1 = int(line.split("-")[0])
    index2 = int(line.split(" ")[0].split("-")[1])

    # get the letter we need to check for
    letter = line.split(" ")[1][0]
    # get the password
    password = line.split(": ")[1]

    print(f"the first index is {index1} and the second index is {index2} for letter {letter}. the password is {password}")
    # check if it is a valid password
    # valid password must contain exactly one instance of the letter total at both indices
    if (password[index1 - 1] == letter) ^ (password[index2 - 1] == letter):
        valid += 1
        print("It is valid")
    else:
        print("It is not valid")
print(valid)