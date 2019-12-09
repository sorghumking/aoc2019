# Intcode computer
class Intcode:
    def __init__(self, program, initial_inputs):
        self.program = program
        self.inputs = initial_inputs
        self.output = None

    def put(self, val, dest_idx):
        # print("put {} at {}".format(val, dest_idx))
        self.program[dest_idx] = val

    def get(self, src_idx):
        val = self.program[src_idx]
        # print("get at {} = {}".format(src_idx, val))
        return val

    def add(self, val1, val2, dest_idx):
        self.put(val1 + val2, dest_idx)
        # print("adding {} and {}, storing in {}".format(val1, val2, dest_idx))

    def mul(self, val1, val2, dest_idx):
        self.put(val1 * val2, dest_idx)
        # print("multiplying {} and {}, storing in {}".format(val1, val2, dest_idx))

    def parse_instruction(self, inst, idx):
        # print("Current index: {}".format(idx))
        vals = []
        if inst > 99:
            # print("Parsing opcode {}".format(inst))
            strinst = str(inst)
            split_idx = len(strinst) - 2
            inst = int(strinst[split_idx:])
            params = list(reversed([int(c) for c in strinst[:split_idx]]))
            # print("Code {} = opcode {}".format(self.program[idx], inst))
            # print("Params = {}".format(params))
            if inst in [1,2,5,6,7,8]:
                while len(params) < 3:
                    params.append(0) # add zeroes for missing params

            if inst in [1,2,7,8]:
                val1 = self.get(self.program[idx+1]) if params[0] == 0 else self.program[idx+1]
                val2 = self.get(self.program[idx+2]) if params[1] == 0 else self.program[idx+2]
                val3 = self.program[idx+3]
                vals = [val1, val2, val3]
            elif inst == 3:
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
            elif inst == 7 or inst == 8:
                val1 = self.get(self.program[idx + 1])
                val2 = self.get(self.program[idx + 2])
                vals = [val1, val2, self.program[idx + 3]]
            else:
                print("Unexpected instruction: {}".format(inst))

        return inst, vals

    def process(self):
        idx = 0
        while True:
            inst = self.program[idx]
            if inst == 99:
                # print("Halt")
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
                cur_input = self.inputs.pop(0) # pop element 0
                # print("Input: putting {} at {}".format(cur_input, vals[0]))
                self.put(cur_input, vals[0])
                idx += 2
            elif inst == 4:
                print("Output: {}".format(vals[0]))
                self.output = vals[0]
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
