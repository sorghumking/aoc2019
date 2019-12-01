import re

def parse_day1(inputfile):
    listy = []
    with open(inputfile) as f:
        listy = [int(l.strip()) for l in f.readlines()]
    return listy

