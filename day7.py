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



def execute(p,args,out):
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


    pc = 0
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
            # if args == []:
            #     return -1
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
        pass
        # print("Finished with success")
        # print(p)
    else:
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
        args = [config.pop(0),out.pop()]
        out = []
        execute(program,args,out)

    outputs.append(out.pop())

print(f"Part 1: max: {max(outputs)}")





# programB =  "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")
# programB = list(map(lambda x: int(x),programB))
# outputs = []

# # for combo in itertools.permutations([5,6,7,8,9], 5):  # 2 for pairs, 3 for 
# config =  [9,8,7,6,5] # list(combo)
# # print(config)
# output = 0
# program = []

# #initial loop
# for i in range(0,5):
#     print(f"execute amp {i}")
#     program.append(programB[:])
#     args = [config.pop(0),output]
#     output = execute(program[i],args) 
#     print(output)
    

# for i in range(0,5):
#     print(f"execute amp {i}")
#     args = [output] #  if output != -1 else []
#     print(args)
#     output = execute(program[i],args)    

# print(output)
# outputs.append(output)

# print(f"Part 2: max: {max(outputs)}")
