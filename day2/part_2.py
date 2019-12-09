from intcode_computer import IntcodeComputer

with open("input.txt", "r") as f:
    src = f.read()
    for noun in range(0, 100):
        for verb in range(0, 100):
            c = IntcodeComputer(src)
            c.ints[1] = noun
            c.ints[2] = verb
            c.eval()
            if c.at(0) == 19690720:
                print(100 * noun + verb)
                break
