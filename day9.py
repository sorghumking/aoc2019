from common import Intcode

def solve(program):
    pass

if __name__ == "__main__":
    # program = []
    # solve(program)
    c = Intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] + [0] * 1000, [])
    print("Output = {}".format(c.process()))