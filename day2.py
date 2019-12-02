from inputs import parse_day2

def part1(program):
    result = process(program)

def process(program):
    idx = 0
    while True:
        if program[idx] == 99:
            print("Halt")
            break
        else:
            val1 = program[program[idx+1]]
            val2 = program[program[idx+2]]
            if program[idx] == 1:
                program[program[idx+3]] = val1 + val2
            elif program[idx] == 2:
                program[program[idx+3]] = val1 * val2
        idx += 4
    return program[0]
    # print(program)

def part2(program):
    for noun in range(100):
        for verb in range(100):
            print("Trying {}, {}".format(noun, verb))
            working = program.copy()
            working[1] = noun
            working[2] = verb
            result = process(working)
            if result == 19690720:
                print("Success! Noun = {}, verb = {}, answer = {}".format(noun, verb, 100 * noun + verb))
                return
    return


if __name__ == "__main__":
    program = parse_day2()
    # part1(program)
    part2(program)
    # tests = [[1,0,0,0,99], [2,3,0,3,99], [2,4,4,5,99,0], [1,1,1,4,99,5,6,0,99]]
    # for t in tests:
        # part1(t)