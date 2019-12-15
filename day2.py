def execute(program,par1,par2):
    program[1] = par1
    program[2] = par2
    pc = 0
    while program[pc] != 99:
        op1 = program[program[pc+1]] 
        op2 = program[program[pc+2]]
        if program[pc]   == 1: # Add
            program[program[pc+3]] = op1 + op2
        elif program[pc] == 2: # Mult
            program[program[pc+3]] = op1 * op2
        else:
            break
        pc += 4


f = open("day2.input","r")

programB = f.readline().split(",")
programB = list(map(lambda x: int(x),programB))

# Part 1
program = programB[:]
execute(program,12,2)
print(f"part 1: {program[0]}")

# Part 2
for i in range(0,100):
    for j in range(0,100):
        program = programB[:]
        execute(program,i,j)
        if(program[0] == 19690720):
            print(f"part 2: i: {i}, j: {j}, program[0]: {program[0]}, answer: {100*i + j}")


