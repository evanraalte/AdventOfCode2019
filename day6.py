def findDeps(orbit,relations,lst):
    for r in relations:
        if orbit in relations:
            lst.append((orbit,relations[orbit]))
            return 1 + findDeps(relations[orbit],relations,lst)
    return 0


f = open("day6.input","r")
orbits =  f.readlines()
orbit_relations = [ orbit.strip().split(")") for orbit in orbits]

# flatten list , filter unique
flat_orbits = []
for orbit_relation in orbit_relations:
    flat_orbits = flat_orbits + orbit_relation
unique_orbits = list(dict.fromkeys(flat_orbits))

orbit_relations = {sub[1] : sub[0] for sub in orbit_relations}

part1 = 0

you = []
san = []

for orbit in unique_orbits:
    lst = []
    deps = findDeps(orbit,orbit_relations,lst)
    # print(lst)

    def contains(lst,string):
        for e in lst:
            if e[0] == string:
                return True
        return False

    if contains(lst,'YOU'):
        you = lst[:]
    
    if contains(lst,'SAN'):
        san = lst[:]

    part1 += deps


print(f"you : {you}")
print(f"san : {san}")

print(f"difference : {set(san).difference(set(you))}")
print(f"difference : {set(you).difference(set(san))}")

print(f"symmetric difference: {len(set(you).symmetric_difference(san))-2}") # alternative

youCrossingLen = len(set(san).difference(set(you))) - 1
sanCrossingLen = len(set(you).difference(set(san))) - 1
part2 = youCrossingLen + sanCrossingLen


# part2 = len(you.union(san) - you.difference(san)) - 1

print(f"part: {part1}")
print(f"part: {part2}")