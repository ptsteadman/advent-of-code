from module import Module
with open("input.txt", "r") as f:
    total_fuel_requirement = 0
    for l in f.readlines():
        module = Module(mass=int(l))
        total_fuel_requirement += module.fuel_requirement()
    print(total_fuel_requirement)
