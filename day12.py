class Moon:
    def __init__(self, x, y, z, name):
        self.name = name
        self.initial_state = ((x,y,z),(0,0,0))
        self.init_axis = [(x,0), (y,0), (z,0)]
        self.pos = [x,y,z]
        self.vel = [0,0,0]

    def update_vel(self, delta):
        self.vel = [self.vel[i] + delta[i] for i in range(3)]

    def update_vel_axis(self, delta, axis):
        self.vel[axis] += delta

    def update_pos(self):
        self.pos = [self.pos[i] + self.vel[i] for i in range(3)]

    def update_pos_axis(self, axis):
        self.pos[axis] += self.vel[axis]
        # self.pos[axis] = tuple() # argh this is an annoying way to sim on one axis...fix

    def check_prev_state(self):
        return (tuple(self.pos), tuple(self.vel)) == self.initial_state

    def check_axis_state(self, axis): # 0 = x, 1 = y, 2 = z
        return (self.pos[axis], self.vel[axis]) == self.init_axis[axis]

    def energy(self):
        potential = sum([abs(self.pos[i]) for i in range(3)])
        kinetic = sum([abs(self.vel[i]) for i in range(3)])
        return potential * kinetic

    def __str__(self):
        return f"pos={self.pos} vel={self.vel}"
        

def update_moons(moons):
    for moon in moons:
        grav = [0,0,0]
        for cmp_moon in [m for m in moons if m != moon]:
            for i in range(3):
                grav[i] += get_grav(moon.pos[i], cmp_moon.pos[i])
        moon.update_vel(grav)
    for moon in moons:
        moon.update_pos()
        # print(moon)

def update_moons_axis(moons, axis):
    for moon in moons:
        grav = 0
        for cmp_moon in [m for m in moons if m != moon]:
            grav += get_grav(moon.pos[axis], cmp_moon.pos[axis])
        moon.update_vel_axis(grav, axis)
    for moon in moons:
        moon.update_pos_axis(axis)


def solve1(moons):
    steps = 0
    while steps < 1000:
        update_moons(moons)
        steps += 1

    total_energy = sum([m.energy() for m in moons])
    print(f"Total energy in system after {steps} steps = {total_energy}")

def solve2(moons):
    # Simulate system on an axis-by-axis basis, stopping when we return
    # to initial state on cur axis and moving to the next. Then find LCM
    # of step counts for each axis (using Wolfram because lazy)
    for axis in [0,1,2]:
        step = 0
        while True:
            update_moons_axis(moons, axis)
            step += 1
            if False not in set([m.check_axis_state(axis) for m in moons]):
                print(f"Repeated {chr(ord('x') + axis)}-axis at step {step}")
                break

def get_grav(pos1, pos2):
    if pos1 < pos2:
        return 1
    elif pos1 > pos2:
        return -1
    else:
        return 0


if __name__ == "__main__":
    # moons = [Moon(-1,0,2,'A'), Moon(2,-10,-7,'B'), Moon(4,-8,8,'C'), Moon(3,5,-1,'D')] # example 1
    # moons = [Moon(-8,-10,0,'A'), Moon(5,5,10,'B'), Moon(2,-7,3,'C'), Moon(9,-8,-3,'D')] # example 2
    moons = [Moon(0,6,1,'A'), Moon(4,4,19,'B'), Moon(-11,1,8,'C'), Moon(2,19,15,'D')] # input
    solve1(moons)
    # solve2(moons)