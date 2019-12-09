import sys
from inputs import parse_day8

def solve(image):
    layer_size = 25 * 6
    layers = []
    layer_count = 0
    min_zeroes = 100000
    min_product = 0
    decoded = [2] * layer_size
    for idx, c in enumerate(image):
        if idx % layer_size == 0:
            layers.append([0,0,0])
            layer_count += 1
        layers[layer_count-1][int(c)] += 1
        if decoded[idx % layer_size] == 2 and int(c) in [0,1]:
            decoded[idx % layer_size] = int(c)

    for cl in layers:
        if cl[0] < min_zeroes:
            min_zeroes = cl[0]
            min_product = cl[1] * cl[2]

    print("Part 1: Minimum # of zeroes = {}, product of 1s and 2s = {}".format(min_zeroes, min_product))

    print("Part 2:")
    render(decoded, 25, 6)

def render(decoded_image, wid, hit):
    for h in range(hit):
        for w in range(wid):
            c = ' ' if decoded_image[wid*h + w] == 0 else 'X'
            sys.stdout.write(c)
        sys.stdout.write("\n")


if __name__ == "__main__":
    image = parse_day8("day8input.txt")
    solve(image)
