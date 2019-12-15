import math

f = open("day1.input","r")

def getFuelMass( moduleMass):
    return (math.floor(moduleMass/3) - 2)

fl = f.readlines()

def getFuelMassSum(fl,part):    
    fuelMassSum = 0
    for line in fl:
        moduleMass = int(line)
        fuelMass = getFuelMass(moduleMass)
        if part == 1:
            fuelMassSum += fuelMass
        if part == 2:
            while fuelMass >= 0: 
                fuelMassSum += fuelMass
                fuelMass = getFuelMass(fuelMass)
    return fuelMassSum


print(f"Part 1: fuel for modules: {getFuelMassSum(fl,1)}")
print(f"Part 2: fuel for modules: {getFuelMassSum(fl,2)}")

