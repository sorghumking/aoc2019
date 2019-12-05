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
            if inst in [1,2,5,6,7,8]:
                while len(params) < 3:
                    params.append(0) # add zeroes for missing params

            if inst in [1,2,7,8]:
                val1 = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                val2 = self.get(self.program[idx+2]) if params[1] == 0 else self.program[idx+2]
                val3 = self.program[idx+3]
                vals = [val1, val2, val3]
                # print("Good vals: {}, bad vals: {}".format(vals, bad_vals))
            elif inst == 3:
                # print("HELLO")
                vals = [self.get(self.program[idx + 1])] # wrong? Never gets hit but should drop the self.get I think....
            elif inst == 4:
                vals = [self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]]
            elif inst == 5 or inst == 6:
                val1 = self.get(self.program[idx + 1]) if params[0] == 0 else self.program[idx + 1]
                val2 = self.get(self.program[idx + 2]) if params[1] == 0 else self.program[idx + 2]
                vals = [val1, val2]
        else:
            # print("Basic opcode = {}".format(inst))
            if inst == 1 or inst == 2:
                vals = [self.get(self.program[idx + v]) for v in range(1,3)]
                vals.append(self.program[idx + 3])
            elif inst == 3:
                vals = [self.program[idx + 1]]
            elif inst == 4:
                vals = [self.get(self.program[idx + 1])]
            elif inst == 5 or inst == 6:
                vals = [self.get(self.program[idx + 1]), self.get(self.program[idx + 2])]
                # test = self.get(self.program[idx + 1])
                # if (test == 0 and inst == 6) or (test != 0 and inst == 5):
                #     # do jump
                #     new_idx = self.get(self.program[idx + 2])
                #     idx = new_idx
            elif inst == 7 or inst == 8:
                val1 = self.get(self.program[idx + 1])
                val2 = self.get(self.program[idx + 2])
                vals = [val1, val2, self.program[idx + 3]]
                # new_val = 1 if (val1 < val2 and inst == 7) or (val1 == val2 and inst == 8) else 0
                # self.put(new_val, self.program[idx + 3])
            else:
                print("Unexpected instruction: {}".format(inst))

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
            elif inst == 5 or inst == 6:
                # test = self.get(self.program[idx + 1])
                test = vals[0]
                if (test == 0 and inst == 6) or (test != 0 and inst == 5):
                    # do jump
                    new_idx = vals[1] #self.get(self.program[idx + 2])
                    idx = new_idx
                else:
                    idx += 3
            elif inst == 7 or inst == 8:
                new_val = 1 if (vals[0] < vals[1] and inst == 7) or (vals[0] == vals[1] and inst == 8) else 0
                self.put(new_val, vals[2])
                idx += 4
            else:
                print("Unexpected instruction: {}".format(inst))
                return


def part1(program, initial_input):
    ic = Intcode(program, initial_input)
    ic.process_v2()

def part2(program, initial_input):
    ic = Intcode(program, initial_input)
    ic.process_v2()


if __name__ == "__main__":
    program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,67,92,225,1101,14,84,225,1002,217,69,224,101,-5175,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1,214,95,224,101,-127,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,8,41,225,2,17,91,224,1001,224,-518,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,37,27,225,1101,61,11,225,101,44,66,224,101,-85,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,7,32,224,101,-224,224,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1001,14,82,224,101,-174,224,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,102,65,210,224,101,-5525,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,81,9,224,101,-90,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,71,85,225,1102,61,66,225,1102,75,53,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,419,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,434,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,599,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,629,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]
    # program = [1002, 4, 3, 4, 33]
    # part1(program, 1)
    # program = [3,9,8,9,10,9,4,9,99,-1,8]
    # program = [3,9,7,9,10,9,4,9,99,-1,8]
    # program = [3,3,1107,-1,8,3,4,3,99]
    # program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    # program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    part2(program, 5)
