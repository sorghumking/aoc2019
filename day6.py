from inputs import parse_day6

def part1(orbits):
    planets = list(set([item for o in orbits for item in o])) # list of unique planets

    omap = {} # key: child, value: parent
    for parent, child in orbits: # build map
        if child in omap:
            print("Child already exists in omap, something is wrong.")
        omap[child] = parent

    # brute force: count steps in path back to root for each planet
    total = 0
    for p in planets:
        while p in omap:
            total += 1
            p = omap[p]
    print("Total orbits = {}".format(total))

if __name__ == "__main__":
    # orbits = parse_day6("day6example.txt")
    orbits = parse_day6("day6input.txt")
    # print(orbits)
    part1(orbits)