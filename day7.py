import copy
import itertools


def getOperands(instr,opcode,p,pc):
    if opcode in ["inp","out"]:
        op1 = p[pc+1] if instr[1] == "1" else p[p[pc+1]]
        return (op1,0)

    if opcode in ["add","mul","less","eq","jmpT","jmpF"]:
        op1 = p[pc+1] if instr[1] == "1" else p[p[pc+1]]
        op2 = p[pc+2] if instr[0] == "1" else p[p[pc+2]]
        return (op1,op2)
    return (0,0)



def execute(p,args,out,pc):
    toHuman = {
        "99" : "fin",
        "01" : "add",
        "02" : "mul",
        "03" : "inp",
        "04" : "out",
        "05" : "jmpT",
        "06" : "jmpF",
        "07" : "less",
        "08" : "eq"
    }

    done = False
    while not done:
        instr = str(p[pc]).zfill(4)
        opcode = toHuman[instr[2:4]] 


        op1,op2 = getOperands(instr,opcode,p,pc)

        if opcode   == "fin": # instruction with no parameters
            done = True
        elif opcode == "add":
            p[p[pc+3]] = op1 + op2
            pc += 4
        elif opcode == "mul":
            p[p[pc+3]] = op1 * op2
            pc += 4
        elif opcode == "less":
            p[p[pc+3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == "eq":
            p[p[pc+3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == "jmpT":
            pc = op2 if op1 != 0 else pc + 3
        elif opcode == "jmpF":
            pc = op2 if op1 == 0 else pc + 3                
        elif opcode == "inp":
            if args == []: # nothing to pop, return program counter so that we can continue later..
                return (pc,0)
            inp = args.pop(0)
            p[p[int(pc+1)]] = inp # int(input("input:"))
            # print(f"input: {inp}")
            pc +=2
        elif opcode == "out":
            # print(f"output:{op1}")
            out.append(copy.deepcopy(op1))
            pc += 2
        else:
            break
    if done:
        return (pc,1)
        # print("Finished with success")
        # print(p)
    else:
        return (pc,-1)
        print("Finished with error")


f = open("day7.input","r")
programB =  f.readline().split(",")
programB = list(map(lambda x: int(x),programB))

outputs = []

for combo in itertools.permutations([0,1,2,3,4], 5):  # 2 for pairs, 3 for 
    config = list(combo)

    out = [0] # initial
    for i in range(0,5):
        program = programB[:]
        pc = 0
        args = [config.pop(0),out.pop()]
        out = []
        execute(program,args,out,pc)

    outputs.append(out.pop())

print(f"Part 1: max: {max(outputs)}")

outputs = []

for combo in itertools.permutations([5,6,7,8,9], 5):  # 2 for pairs, 3 for 
    config =  list(combo)
    out = [0]
    program = []
    pc = []

    #initial loop
    for i in range(0,5):
        program.append(programB[:])
        pc.append(0)
        args = [config.pop(0),out.pop()]
        out = []
        (pc[i],_) = execute(program[i],args,out,pc[i]) 
        
    done = 0
    while done == 0:
        for i in range(0,5):
            args = [out.pop()]
            out = []
            (pc[i],done) = execute(program[i],args,out,pc[i])


    outputs.append(out.pop())

print(f"Part 2: max: {max(outputs)}")
