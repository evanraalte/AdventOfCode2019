import math

class Asteroid:
    numLos = 0
    los = []
    def __init__(self,x,y):
        self.x = x
        self.y = y

f = open("day10.input","r")
lines =  f.readlines()


# Find all asteroids
asteroids = []
for y, line in enumerate(lines):
    for x,char in enumerate(line):
        if char == '#':
            asteroids.append(Asteroid(x,y))

def bestBaseStation(asteroids):
    best = asteroids[0]
    for base in asteroids:
        me = id(base)
        los = []
        for a in asteroids:
            if not id(a) == me:
                dx = a.x - base.x 
                dy = base.y - a.y 
                angle = math.degrees(math.atan2(dx,dy))
                angle = angle + 360 if angle < 0 else angle
                los.append((angle,a.x,a.y))

        seen = set()
        los = [(a,b,c) for a,b,c in los if not (a in seen or seen.add(a))]
        los = sorted(los,key = lambda x: x[0])
        base.los = los
        base.numLos = len(los)
        best = base if base.numLos > best.numLos else best
    return best

base = bestBaseStation(asteroids)
print(f"Part 1: ({base.x},{base.y}) => {base.numLos}")

# print(base.los)
# for a in asteroids:
#     if a.los == maxLos:
#         print(f"({a.x},{a.y})")