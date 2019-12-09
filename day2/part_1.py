from intcode_computer import IntcodeComputer

with open("input.txt", "r") as f:
    c = IntcodeComputer(f.read())
    c.ints[1] = 12
    c.ints[2] = 2
    c.eval()
    print(c.at(0))
