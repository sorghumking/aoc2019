import math
from inputs import parse_day10

def solve1(asteroids):
    visible_dict = {}
    for cur in asteroids:
        visible_count = 0
        for a in [a for a in asteroids if a != cur]:
            dx,dy = normalize_slope(cur, a)
            x,y = cur
            while True:
                x += dx
                y += dy
                if (x,y) == a: # clear path from cur to a
                    visible_count += 1
                    break
                elif (x,y) in asteroids: # path from cur to a is blocked
                    break
        visible_dict[cur] = visible_count
    best = max(visible_dict, key=lambda key: visible_dict[key])
    print(f"Best is {best} with {visible_dict[best]} visible asteroids")

def solve2(asteroids, station_pos):
    # build list of vectors between station_pos and each asteroid
    vectors = []
    for roid in [a for a in asteroids if a != station_pos]:
        vec = normalize_slope(station_pos, roid)
        if vec not in vectors: # (1,1) and (2,2) have same normalized slope
            vectors.append(vec)
        
    # sort list by angle
    angles = [(v, vec_angle(v[0], v[1])) for v in vectors]
    angles.sort(key=lambda t:t[1])

    # print(angles)
    # for each angle, fire laser and count destroyed asteroid if any
    asteroid_state = asteroids.copy()
    max_x = max(asteroids, key=lambda a:a[0])[0]
    max_y = max(asteroids, key=lambda a:a[1])[1]
    hit_count = 0
    for firing_vector, _ in angles:
        hit = fire_laser(station_pos, max_x, max_y, firing_vector, asteroid_state)
        if hit:
            hit_count += 1
            if hit_count == 200:
                print("200th asteroid vaporized, hooray!")
                break

def fire_laser(station_pos, max_x, max_y, vec, asteroid_state):
    x,y = station_pos
    dx,dy = vec
    while True:
        x += dx
        y += dy
        if (x,y) in asteroid_state: # hit! remove from state
            asteroid_state.remove((x,y))
            print(f"Vaporized asteroid at {(x,y)}!")
            return True
        if x < 0 or y < 0 or x > max_x or y > max_y:
            print(f"Laser out of bounds at {(x,y)}, missed.")
            break
    return False

# return angle of vector in degrees
def vec_angle(x, y):
    # In our coordinate system y values increase as we move downward.
    # Reverse y's sign to account for this in these calculations.
    y *= -1
    if x == 0:
        return math.degrees(0 if y >= 0 else math.pi)
    elif y == 0:
        return math.degrees(math.pi/2 if x > 0 else (3*math.pi)/2)

    ang = math.atan(y/x)
    return abs(math.degrees(ang)) + quadrant_adjustment(x, y)

# return angle in degrees by which to adjust result of atan(y,x),
# which ranges between -90 and 90 degrees
def quadrant_adjustment(x, y):
    if x >= 0 and y >= 0:
        return 0.0
    elif x >= 0 and y < 0:
        return 90.0
    elif x < 0 and y < 0:
        return 180.0
    elif x < 0 and y >= 0:
        return 270.0

# return normalized vector from a1 to a2
def normalize_slope(a1, a2):
    slope = (a2[0] - a1[0], a2[1] - a1[1])
    print(f"Slope from {a1} to {a2} = {slope}")
    gcd = math.gcd(slope[0], slope[1])
    normalized = (slope[0]/gcd, slope[1]/gcd)
    print(f"Normalized to {normalized}")
    return normalized

if __name__ == "__main__":
    asteroids, station_pos = parse_day10("day10input.txt")
    # solve1(asteroids)
    # asteroids, station_pos = parse_day10("day10pt2_angle_test.txt")
    solve2(asteroids, (37,25))
    # print(f"Station pos = {station_pos}")
    # solve2(asteroids, station_pos)
