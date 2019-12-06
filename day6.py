from inputs import parse_day6

def part1(orbits):
    omap = {}
    planets = list(set([item for o in orbits for item in o]))
    for o in orbits: # build map
        if o[0] not in omap:
            omap[o[0]] = [o[1]]
        else:
            omap[o[0]].append(o[1])

    # find leaves - planets with no direct orbit
    leaves = []
    for p in planets:
        if p not in omap:
            leaves.append(p)
    
    for leaf in leaves:
        depth = 0
        for key, val in omap.items():
            if leaf in val:
                depth += 1
                # key is parent planet

    # print(omap)

def get_depth(node, omap):
    pass
    
if __name__ == "__main__":
    orbits = parse_day6("day6example.txt")
    # orbits = parse_day6("day6input.txt")
    # print(orbits)
    part1(orbits)