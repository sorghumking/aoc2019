import re

def parse_day1(inputfile):
    listy = []
    with open(inputfile) as f:
        listy = [int(l.strip()) for l in f.readlines()]
    return listy

def parse_day2():
    orig = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
    orig[1] = 12
    orig[2] = 2
    return orig

def parse_day3(inputfile):
    numCharPattern = "([RLUD])([0-9]+)"
    with open(inputfile) as f:
        lines = f.readlines()
        wires = []
        for idx in range(2):
            strs = lines[idx].strip().split(',')
            # print(strs)
            w = []
            for s in strs:
                foo = re.match(numCharPattern, s)
                w.append((foo.groups()[0], int(foo.groups()[1])))
            wires.append(w)
    return wires

def parse_day6(inputfile):
    orbits = []
    pattern = "([A-Z0-9]+)\)([A-Z0-9]+)"
    with open(inputfile) as f:
        for l in f.readlines():
            tokens = re.match(pattern, l.strip())
            orbits.append(tokens.groups())
    return orbits

def parse_day8(inputfile):
    with open(inputfile) as f:
        image = f.readlines()[0].strip()
    return image

def parse_day10(inputfile):
    asteroids = []
    station_pos = None
    with open(inputfile) as f:
        for y, l in enumerate(f.readlines()):
            for x, c in enumerate(l):
                if c == '#':
                    asteroids.append((x,y))
                if c == 'X':
                    station_pos = (x,y)
    return asteroids, station_pos
