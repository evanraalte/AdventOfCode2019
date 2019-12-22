mem = {}
pc = 0
rb = 0

def read(index):
    if not index in mem:
        mem[index] = 0
    return mem[index]

toHuman = {
    "99" : "fin",
    "01" : "add",
    "02" : "mul",
    "03" : "inp",
    "04" : "out",
    "05" : "jmpT",
    "06" : "jmpF",
    "07" : "less",
    "08" : "eq",
    "09" : "rb"
}

def write(index,value):
    mem[index] = value

def getOperands(instr):
    global pc, rb

    imm1 = pc+1
    imm2 = pc+2
    pos1 = read(imm1)
    rb1  = pos1+rb
    pos2 = read(imm2)
    rb2  = pos2+rb     
    pos3 = read(pc+3)
    rb3  = pos3+rb  

    p_op1 = imm1 if instr[2] == "1" else pos1 if instr[2] == "0" else rb1
    p_op2 = imm2 if instr[1] == "1" else pos2 if instr[1] == "0" else rb2
    p_op3 = pos3 if instr[0] == "0" else rb3
    return (p_op1,p_op2,p_op3)



def intCode(inputs,outputs):
    global pc, rb

    done = False
    iCnt = 0
    while not done:
        iCnt += 1
        instr = str(read(pc)).zfill(5)      
        opcode = toHuman[instr[-2:]] 
        # print(f"{read(pc)}\t{read(pc+1)}\t{read(pc+2)}\t{read(pc+3)}")
        p_op1,p_op2, p_op3 = getOperands(instr)
        op1 = read(p_op1)
        op2 = read(p_op2)
        dest = p_op3
        if opcode   == "fin": # instruction with no parameters
            done = True
        elif opcode == "add":
            write(dest,op1 + op2)
            pc += 4
        elif opcode == "mul":
            write(dest,op1 * op2)
            pc += 4
        elif opcode == "less":
            res = 1 if op1 < op2 else 0
            write(dest,res)
            pc += 4
        elif opcode == "eq":
            res = 1 if op1 == op2 else 0
            write(dest,res)
            pc += 4
        elif opcode == "jmpT":
            pc = op2 if op1 != 0 else pc + 3
        elif opcode == "jmpF":
            pc = op2 if op1 == 0 else pc + 3                
        elif opcode == "inp":
            if inputs == []:
                return 0
            inp = inputs.pop(0)
            write(p_op1,inp)
            # print(f"writing {inp} to addr {p_op1}, rb: {rb}")
            pc +=2
        elif opcode == "out":
            outputs.append(op1)
            pc += 2
        elif opcode == "rb":
            rb = rb + op1
            pc += 2
        else:
            print("Bad opcode")
            break
    print(iCnt)
    if done:
        return 1
        
    else:
        return -1
        print("Finished with error")


f = open("day11.input","r")
program =  f.readline().split(",")
for index,instruction in enumerate(program):
    write(index,int(instruction))

direction = 0
curx  = 0
cury = 0
posx = []
posy = []
posx.append(curx)
posy.append(cury)

panel = {}
done = 0
while done == 0:
    if (curx,cury) not in panel:
        if curx == 0 and cury == 0: #part 2
            panel[(curx,cury)] = 1
        else:
            panel[(curx,cury)] = 0

    inputs = [panel[(curx,cury)]]
    outputs = []
    done = intCode(inputs,outputs)
    panel[(curx,cury)] = outputs[0]


    direction = (direction + 1)%4 if outputs[1] == 1 else (direction - 1)%4 
    


    dirs = {
        0: (0,1), 
        1: (1,0), 
        2: (0,-1),
        3: (-1,0) 
    }

    dx,dy = dirs[direction]
    curx += dx
    cury += dy
    posx.append(curx)
    posy.append(cury)



print(f"xrange: ({min(posx)},{max(posx)}), yrange: ({min(posy)},{max(posy)})")
print(len(panel))

for y in range(max(posy),min(posy)-1, -1):
    string = ""
    for x in range(min(posx),max(posx)+1):
        if not (x,y) in panel:
            panel[(x,y)] = 0
        c = '#' if panel[(x,y)] == 1 else '.'
        string += c
    print(string)

# print(panel[(0,-5)])