def getCoordinates(line):
    dirs = {
        'R': (1,0), 
        'L': (-1,0), 
        'U': (0,1), 
        'D': (0,-1)
    }
    posx = 0
    posy = 0
    steps = 0
    points = {}
    for segment in line:
        dx, dy = dirs[segment[0]]
        for i in range(0,int(segment[1:])):
            posx += dx
            posy += dy
            steps += 1
            # Save as dictionary is way more efficient, thanks random dude on Reddit! 
            if (posx,posy) not in points:
                points[(posx,posy)] = steps
    return points


f = open("day3.input","r")

lines = ["",""]
lines[0] = f.readline().split(",")
lines[1] = f.readline().split(",")


c0 = getCoordinates(lines[0])
c1 = getCoordinates(lines[1])

matches = [p for p in c0 if p in c1]

part1 = min(map(lambda c: abs(c[0]) + abs(c[1]),matches))
part2 = min(map(lambda c: c0[c] + c1[c],matches))

print(f"part1: {part1}")
print(f"part2: {part2}")