from inputs import parse_day6

def solve(orbits):
    planets = list(set([item for o in orbits for item in o])) # list of unique planets

    omap = {} # key: child, value: parent
    for parent, child in orbits: # build map
        if child in omap:
            print("Child already exists in omap, something is wrong.")
        omap[child] = parent

    # part 1
    # brute force: count steps in path back to root for each planet
    # total = 0
    # for p in planets:
    #     while p in omap:
    #         total += 1
    #         p = omap[p]
    # print("Total orbits = {}".format(total))

    # part 2
    # get paths back to root for YOU and SAN
    you_path = get_path("YOU", omap)
    san_path = get_path("SAN", omap)

    # find earliest common ancestor
    common = None
    for p in you_path:
        if p in san_path:
            common = p
            break

    print("Common planet = {}".format(common))
    print("Intersection of paths = {}".format(list(set(you_path).intersection(san_path))))

    you_transfers = you_path.index(common) - 1 # - 1 as initially orbited planet doesn't count
    san_transfers = san_path.index(common) - 1

    print("YOU transfers to common ancestor: {}, SAN: {}".format(you_transfers, san_transfers))
    print("Total transfers = {}".format(you_transfers + san_transfers))

        
def get_path(planet, omap):
    path = []
    p = planet
    while p in omap:
        path.append(p)
        p = omap[p]
    path.append(p) # don't forget root planet
    return path


if __name__ == "__main__":
    # orbits = parse_day6("day6example2.txt")
    orbits = parse_day6("day6input.txt")
    solve(orbits)