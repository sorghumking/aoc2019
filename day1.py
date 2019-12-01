from inputs import parse_day1

def part1(masses):
    fuels = [(m//3 - 2) for m in masses]
    # print(fuels)
    total = sum(fuels)
    # print(total)

def fuel_req(fuel):
    req = fuel//3 - 2
    if req <= 0:
        return 0
    else:
        return req + fuel_req(req)

def part2(masses):
    fuels = [(m//3 - 2) + fuel_req(m//3 - 2) for m in masses]
    print(fuels)
    print("total = {}".format(sum(fuels)))

if __name__ == "__main__":
    masses = parse_day1("day1input.txt")
    # part1(masses)
    part2(masses)

    # test
    # part2([12, 14, 1969, 100756])
