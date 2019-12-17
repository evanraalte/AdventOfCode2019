def findDeps(orbit,relations):
    for r in relations:
        if orbit in relations:
            return 1 + findDeps(relations[orbit],relations)
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
for orbit in unique_orbits:
    deps = findDeps(orbit,orbit_relations)
    # print(f"{orbit}: {deps}")
    part1 += deps
print(f"part: {part1}")