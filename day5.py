class Intcode:
    def __init__(self, program, initial_input):
        self.program = program
        self.input = initial_input

    def put(self, val, dest_idx):
        print("put {} at {}".format(val, dest_idx))
        self.program[dest_idx] = val

    def get(self, src_idx):
        val = self.program[src_idx]
        print("get at {} = {}".format(src_idx, val))
        return val

    def add(self, val1, val2, dest_idx):
        self.put(val1 + val2, dest_idx)
        print("adding {} and {}, storing in {}".format(val1, val2, dest_idx))

    def mul(self, val1, val2, dest_idx):
        self.put(val1 * val2, dest_idx)
        print("multiplying {} and {}, storing in {}".format(val1, val2, dest_idx))

    def parse_instruction(self, inst, idx):
        # print("Current index: {}".format(idx))
        vals = []
        if inst > 99:
            # print("Parsing opcode {}".format(inst))
            strinst = str(inst)
            split_idx = len(strinst) - 2
            inst = int(strinst[split_idx:])
            params = list(reversed([int(c) for c in strinst[:split_idx]]))
            print("Code {} = opcode {}".format(self.program[idx], inst))
            print("Params = {}".format(params))
            if inst == 1 or inst == 2: # add zeroes for missing params
                while len(params) < 3:
                    params.append(0)
                # print("Extended params = {}".format(params))
                # bad_vals = []
                # for pidx, mode in enumerate(params):
                    # bad_vals.append(self.get(self.program[idx+pidx+1]) if mode == 0 else self.program[idx+pidx+1])
                    # print("pidx = {}, mode = {}, result = {}".format(pidx, mode, self.get(self.program[idx+pidx+1]) if mode == 0 else self.program[idx+pidx+1]))
                    # if mode == 0:
                    #     bad_vals.append(self.get(self.program[idx+pidx+1]))
                    # else:
                    #     bad_vals.append(self.program[idx+pidx+1])
                val1 = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                val2 = self.get(self.program[idx+2]) if params[1] == 0 else self.program[idx+2]
                val3 = self.program[idx+3]
                vals = [val1, val2, val3]
                # print("Good vals: {}, bad vals: {}".format(vals, bad_vals))

            elif inst == 3:
                # print("HELLO")
                vals = [self.get(self.program[idx + 1])]
            elif inst == 4:
                vals = [self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]]
        else:
            # print("Basic opcode = {}".format(inst))
            if inst == 1 or inst == 2:
                vals = [self.get(self.program[idx + v]) for v in range(1,3)]
                vals.append(self.program[idx + 3])
            elif inst == 3:
                vals = [self.program[idx + 1]]
            elif inst == 4:
                vals = [self.get(self.program[idx + 1])]
        return inst, vals

    def process_v2(self):
        idx = 0
        while True:
            inst = self.program[idx]
            if inst == 99:
                print("Halt")
                break

            inst, vals = self.parse_instruction(inst, idx)
            if inst == 1:
                # print("adding: {}".format(vals))
                self.add(vals[0], vals[1], vals[2])
                idx += 4
            elif inst == 2:
                # print("multiplying: {}".format(vals))
                self.mul(vals[0], vals[1], vals[2])
                idx += 4
            elif inst == 3:
                # print("putting {} at {}".format(self.input, vals[0]))
                self.put(self.input, vals[0])
                idx += 2
            elif inst == 4:
                print("Output: {}".format(vals[0]))
                idx += 2
            else:
                print("Unexpected instruction {}".format(inst))
                return

    def process(self):
        idx = 0
        while True:
            inst = self.program[idx]
            if inst == 99:
                print("Halt")
                break

            if self.program[idx] == 1 or self.program[idx] == 2:
                val1 = self.get(self.program[idx+1])
                val2 = self.get(self.program[idx+2])
                if self.program[idx] == 1:
                    self.add(val1, val2, self.program[idx+3])
                elif self.program[idx] == 2:
                    self.mul(val1, val2, self.program[idx+3])
                idx += 4
            elif self.program[idx] == 3:
                self.put(self.input, self.program[idx+1])
                idx += 2
            elif self.program[idx] == 4:
                print("Output: {}".format(self.get(self.program[idx+1])))
                idx += 2
            else:
                val = str(self.program[idx])
                split_idx = len(val) - 2
                opcode = int(val[split_idx:])
                params = list(reversed([int(c) for c in val[:split_idx]]))
                if opcode == 1 or opcode == 2: # add zeroes for missing params
                    while len(params) < 3:
                        params.append(0)
                print("Code {} = opcode {}".format(self.program[idx], opcode))
                # print("Params = {}".format(params))
                if opcode == 1 or opcode == 2:
                    val1 = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                    val2 = self.get(self.program[idx+2]) if params[1] == 0 else self.program[idx+2]
                    if opcode == 1:
                        self.add(val1, val2, self.program[idx+3])
                    elif opcode == 2:
                        self.mul(val1, val2, self.program[idx+3])
                    idx += 4
                elif opcode == 3:
                    # print("HELLO")
                    # dest_idx = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                    dest_idx = self.get(self.program[idx+1]) # ignore params since destination is always in position mode
                    # print("Writing to index {}".format(dest_idx))
                    self.put(self.input, dest_idx)
                    idx += 2
                elif opcode == 4:
                    val = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                    idx += 2
                    print("Output: {}".format(val))
                else:
                    print("Unexpected opcode {}".format(opcode))
                    return


                    # print(self.program)
                    # return

        return self.program[0]


def part1(program, initial_input):
    ic = Intcode(program, initial_input)
    ic.process_v2()
    # ic.process()

if __name__ == "__main__":
    program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,67,92,225,1101,14,84,225,1002,217,69,224,101,-5175,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1,214,95,224,101,-127,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,8,41,225,2,17,91,224,1001,224,-518,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,37,27,225,1101,61,11,225,101,44,66,224,101,-85,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,7,32,224,101,-224,224,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1001,14,82,224,101,-174,224,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,102,65,210,224,101,-5525,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,81,9,224,101,-90,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,71,85,225,1102,61,66,225,1102,75,53,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,419,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,434,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,599,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,629,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]
    # program = [1002, 4, 3, 4, 33]
    part1(program, 1)
