from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


class IntcodeComputer:
    """ Parses and evaluates intcode, returning the value at position 0 once
    the HALT command is reached.
    >>> IntcodeComputer("1,0,0,0,99").eval().at(0)
    2
    >>> IntcodeComputer("2,3,0,3,99").eval().at(3)
    6
    >>> IntcodeComputer("2,4,4,5,99,0").eval().at(5)
    9801
    >>> IntcodeComputer("1,1,1,4,99,5,6,0,99").eval().at(0)
    30
    """

    def __init__(self, source):
        if type(source) != str:
            raise TypeError("Invalid intcode source")
        self.ints = [int(i) for i in source.split(",")]

    def eval(self, ptr=0):
        op = Opcode(self.ints[ptr])
        if op == Opcode.HALT:
            return self
        elif op == Opcode.ADD:
            val_1 = self.deref(ptr + 1)
            val_2 = self.deref(ptr + 2)
            ret = self.at(ptr + 3)
            self.ints[ret] = val_1 + val_2
        elif op == Opcode.MULTIPLY:
            val_1 = self.deref(ptr + 1)
            val_2 = self.deref(ptr + 2)
            ret = self.at(ptr + 3)
            self.ints[ret] = val_1 * val_2
        return self.eval(ptr+4)

    def at(self, idx=0):
        return self.ints[idx]

    def deref(self, idx=0):
        return self.at(self.at(idx))
