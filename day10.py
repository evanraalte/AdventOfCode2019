import math

class Asteroid:
    los = 0
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
        angles = []
        for a in asteroids:
            if not id(a) == me:
                dx = a.x - base.x
                dy = a.y - base.y
                angle = math.degrees(math.atan2(dx,dy))
                # print(f"base ({base.x},{base.y}), a ({a.x},{a.y}) => {angle}")
                angles.append(angle)
        los = len(list(dict.fromkeys(angles)))
        base.los = los
        best = base if base.los > best.los else best
    return best

base = bestBaseStation(asteroids)
print(f"Part 1: ({base.x},{base.y}) => {base.los}")


# for a in asteroids:
#     if a.los == maxLos:
#         print(f"({a.x},{a.y})")