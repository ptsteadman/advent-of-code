from intcode_computer import IntcodeComputer

with open("input.txt", "r") as f:
    c = IntcodeComputer(f.read())
    print(c.ints)
