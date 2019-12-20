import copy


def getOperands(instr,opcode,p,pc):
    if opcode in ["inp","out"]:
        op1 = p[pc+1] if instr[1] == "1" else p[p[pc+1]]
        return (op1,0)

    if opcode in ["add","mul","less","eq","jmpT","jmpF"]:
        op1 = p[pc+1] if instr[1] == "1" else p[p[pc+1]]
        op2 = p[pc+2] if instr[0] == "1" else p[p[pc+2]]
        return (op1,op2)
    return (0,0)



def execute(p):
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
            p[p[int(pc+1)]] = int(input("input:"))
            print(f"writing to: {p[int(pc+1)]}")
            pc +=2
        elif opcode == "out":
            print(f"output:{op1}")
            pc += 2
        else:
            break

    if done:
        print("Finished with success")
        # print(p)
    else:
        print("Finished with error")


f = open("day5.input","r")
program =  f.readline().split(",")
program = list(map(lambda x: int(x),program))
execute(program)



