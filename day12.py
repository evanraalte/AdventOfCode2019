import re
from itertools import combinations
import numpy as np


def calcVelocities(velocities,positions):
    v = velocities[:]
    
    np.greater()
    # for d in range(0,3):
    for c in combinations([0,1,2,3],2):
        np.greater(positions[c[0]],positions[c[1]])
        # p0 = positions[c[0]][d]
        # p1 = positions[c[1]][d]
        # print(f"p0: {p0}, p1: {p1}")      
        # if p1 > p0:
        #     v[c[0]][d] += 1
        #     v[c[1]][d] -= 1                 
        # elif p1 < p0:
        #     v[c[0]][d] -= 1
        #     v[c[1]][d] += 1
        # print(v)   
    print(v)
    return v
        
        

f = open("day12.input","r")
positionsRaw =  f.readlines()

positions = list(map(lambda x: list(map(int,re.sub("<|>| |\n|x|y|z|=","",x).split(","))),positionsRaw))
# print(positions)
velocities = [[0]*3]*4

for _ in range(0,10):
    velocities = calcVelocities(velocities,positions)   
    # print(velocities) 
    # positions = list(map(list,list(np.add(velocities,positions))))
    # print(positions)

