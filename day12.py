import re
from itertools import combinations
import numpy as np


def calc(v,positions):
    for c in combinations([0,1,2,3],2):
        p0 = positions[c[0]]
        p1 = positions[c[1]]
        v0 = velocities[c[0]]
        v1 = velocities[c[1]]

        v0 = np.where(p0 > p1, v0 - 1, np.where(p0 < p1, v0 + 1, v0)) 
        v1 = np.where(p1 > p0, v1 - 1, np.where(p1 < p0, v1 + 1, v1)) 

        velocities[c[0]] = v0
        velocities[c[1]] = v1
        pass
    kin = np.sum(np.abs(v),axis=1)

    return (v,kin)
        
        
f = open("day12.input","r")
positionsRaw =  f.readlines()

positions = np.array(list(map(lambda x: list(map(int,re.sub("<|>| |\n|x|y|z|=","",x).split(","))),positionsRaw)))

velocities = np.array([[0]*3]*4)

velocitiesInitial = velocities
positionsInitial = positions

steps = 0
done = False

perX = 0
perY = 0
perZ = 0

while not done: 
    done = (perX > 0) and (perY > 0) and (perZ > 0)

    velocities,kinetic = calc(velocities,positions)
    positions = velocities + positions
    potential = np.sum(np.abs(positions),axis=1)  
    steps += 1

    perX = steps if np.all(positions[:,0] == positionsInitial[:,0]) else perX
    perY = steps if np.all(positions[:,1] == positionsInitial[:,1]) else perY
    perZ = steps if np.all(positions[:,2] == positionsInitial[:,2]) else perZ


    pass
# print(f"Total energy: {np.sum(potential * kinetic)}")
print(f"steps: {np.lcm.reduce([perX,perY,perZ])}")
