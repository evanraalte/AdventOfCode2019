f = open("day8.input","r")
stream =  [char for char in f.readline()]

width  = 25
height = 6
layerSize = width*height
layers = []
numZeroes = []
# print(len(stream))

for i in range(0,len(stream)-1,layerSize):
    layer = stream[i:i+layerSize]
    # print(layer)
    layers.append(layer)
    numZeroes.append(layer.count("0"))

idx = numZeroes.index(min(numZeroes))
part1 = layers[idx].count("1") * layers[idx].count("2")
# print(layers[idx])
print(part1)

def iterate(color,colorOverlay):
    if color != 2:
        return color
    else: 
        return colorOverlay

finalLayer = [2]*layerSize

for layer in layers:
    layer = [int(x) for x in layer]
    finalLayer = [iterate(finalLayer[i],layer[i]) for i in range(layerSize)]

finalLayer = [str(x) for x in finalLayer]
for i in range(0,len(finalLayer),25):
    print(''.join(finalLayer[i:i+25]).replace('0',' '))