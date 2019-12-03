from inputs import parse_day3

# Works, but is incredibly inefficient, making a list of every
# coordinate visited by both wires. On the upside this made part 2
# very easy, as the index+1 of each coordinate is also the number of
# steps it took to get there.
def part1(wire1, wire2):
    w1coords = []
    x = 0
    y = 0
    for w in wire1:
        dx, dy, coords = get_coords(x, y, w)
        w1coords += coords
        x = dx
        y = dy
    print("Total w1 coords = {}".format(len(w1coords)))

    x = 0
    y = 0
    w2coords = []
    for w in wire2:
        dx, dy, coords = get_coords(x, y, w)
        w2coords += coords
        x = dx
        y = dy
    print("Total w2 coords = {}".format(len(w2coords)))

    # part 1
    overlaps = list(set(w1coords).intersection(w2coords))
    print("Total overlaps = {}".format(len(overlaps)))
    min_dist = min([abs(d[0]) + abs(d[1]) for d in overlaps])
    print("Smallest distance = {}".format(min_dist))

    # part 2
    # number of steps to reach a coord is its index in wire coordinates list + 1
    min_dist = min([w1coords.index(o) + w2coords.index(o) + 2 for o in overlaps])
    print("Smallest # of steps = {}".format(min_dist))


def get_coords(x, y, w):
    coords = []
    if w[0] == 'R':
        for c in range(x + 1, x + 1 + w[1]):
            coords.append((c, y))
        x = x + w[1]
    elif w[0] == 'L':
        for c in range(x - w[1], x):
            coords.append((c, y))
        x = x - w[1]
    elif w[0] == 'U':
        for c in range(y + 1, y + 1 + w[1]):
            coords.append((x, c))
        y = y + w[1]
    elif w[0] == 'D':
        for c in range(y - w[1], y):
            coords.append((x, c))
        y = y - w[1]
    else:
        raise Exception("SOMETHING IS WRONG")
    return x, y, coords

if __name__ == "__main__":
    wires = parse_day3("day3input.txt")
    part1(wires[0], wires[1])
