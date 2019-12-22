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

print(positions)
for i in range(1,1000+1):
    velocities,kinetic = calc(velocities,positions)
    positions = velocities + positions
    potential = np.sum(np.abs(positions),axis=1)  
print(f"Total energy: {np.sum(potential * kinetic)}")

