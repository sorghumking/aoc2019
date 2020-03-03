from common import Intcode

class Robot:
    def __init__(self, program, initial_inputs):
        self.ic = Intcode(program.copy() + [0]*10000, initial_inputs=initial_inputs)
        self.pos = (0,0)
        self.facing = (0,1)
        self.panel_state = {}
        self.output_count = 0

    def run(self):
        self.ic.add_output_listener(self.handle_output)
        self.ic.process()

    def handle_output(self):
        self.output_count += 1
        if self.output_count % 2 == 0:
            color = self.ic.output_log[-2:][0]
            turn_dir = self.ic.output_log[-2:][1]
            self.panel_state[self.pos] = color # paint current location
            self.rotate(turn_dir)
            self.forward()

            # provide new input: color of panel in new position
            if self.pos in self.panel_state:
                panel_color = self.panel_state[self.pos]
            else:
                panel_color = 0 # haven't visited this panel, so it's black
            self.ic.inputs.append(panel_color)
            
    # update self.facing based on turn_dir
    def rotate(self, turn_dir):
        facings = [(0,1), (1,0), (0,-1), (-1, 0)]
        if turn_dir == 0: # turn left
            new_idx = (facings.index(self.facing) - 1) % 4
        elif turn_dir == 1:
            new_idx = (facings.index(self.facing) + 1) % 4
        else:
            print(f"Unexpected turn dir {turn_dir}!!!")
        self.facing = facings[new_idx]

    # move forward in current direction
    def forward(self):
        self.pos = (self.pos[0] + self.facing[0], self.pos[1] + self.facing[1])

    def get_panel_bounds(self):
        min_x = min(self.panel_state, key=lambda pos:pos[0])[0]
        max_x = max(self.panel_state, key=lambda pos:pos[0])[0]
        min_y = min(self.panel_state, key=lambda pos:pos[1])[1]
        max_y = max(self.panel_state, key=lambda pos:pos[1])[1]
        return min_x, max_x, min_y, max_y


def solve1(program):
    robot = Robot(program, [0]) # first panel is black
    robot.run()
    print(f"Robot visited and painted {len(robot.panel_state)} panels")

def solve2(program):
    robot = Robot(program, [1]) # first panel is white
    robot.run()
    print(f"Robot visited and painted {len(robot.panel_state)} panels")

    # draw panel state
    min_x, max_x, min_y, max_y = robot.get_panel_bounds()
    y_list = list(range(min_y, max_y + 1))
    y_list.reverse()
    for y in y_list:
        line = ""
        for x in range(min_x, max_x + 1):
            if (x,y) in robot.panel_state:
                line += '.' if robot.panel_state[(x,y)] == 0 else '#'
            else:
                line += '.'
        print(line)


if __name__ == "__main__":
    program = [3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,29,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,50,1,2,19,10,1006,0,23,1,103,14,10,1,1106,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,88,1006,0,59,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,113,2,101,12,10,2,1001,0,10,2,1006,14,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,146,1,1106,11,10,1006,0,2,1,9,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,180,1,6,13,10,1,1102,15,10,2,7,1,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,213,1006,0,74,2,1005,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,243,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,264,2,104,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,290,101,1,9,9,1007,9,952,10,1005,10,15,99,109,633,104,0,104,1,21101,387512640296,0,1,21101,0,328,0,1106,0,432,21102,1,665749660564,1,21101,339,0,0,1106,0,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179318226984,1,1,21101,386,0,0,1105,1,432,21101,46266346499,0,1,21101,0,397,0,1105,1,432,3,10,104,0,104,0,3,10,104,0,104,0,21102,709580555028,1,1,21102,420,1,0,1106,0,432,21102,1,988220642068,1,21101,0,431,0,1106,0,432,99,109,2,21202,-1,1,1,21101,40,0,2,21102,1,463,3,21102,1,453,0,1106,0,496,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,0,1,458,109,-2,2105,1,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21101,0,0,-3,21201,-3,0,1,22101,0,-2,2,21102,1,1,3,21101,532,0,0,1106,0,537,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,22102,1,-4,-4,1105,1,628,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,579,0,1105,1,537,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,598,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,22101,0,-1,1,21102,620,1,0,106,0,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
    # solve1(program)
    solve2(program)