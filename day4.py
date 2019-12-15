numValid1 = 0
numValid2 = 0

adjList = [str(i)+str(i) for i in range(0,10)]
def adj2(string,part):
    for subString in adjList:
        if subString in string:
            if part == 2:
                occ = 0
                for i in range(0,5):
                    if subString == (string[i]+string[i+1]):
                        occ += 1
                if occ == 1: 
                    return True
            if part == 1:
                return True

    return False

def incr(string):
    base = 0
    for c in string:
        cNum = int(c)
        if cNum >= base:
            base = cNum
            pass
        else:
            return False
    return True

for i in range(347312,805915):
    num = str(i)
    if adj2(num,1) and incr(num):
        numValid1 += 1
    if adj2(num,2) and incr(num):
        numValid2 += 1
    

print(f"Part 1: {numValid1}")
print(f"Part 2: {numValid2}")