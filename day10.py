import math
from inputs import parse_day10

def solve1(asteroids):
    visible_dict = {}
    for cur in asteroids:
        visible_count = 0
        for a in [a for a in asteroids if a != cur]:
            dx,dy = normalize_slope(cur, a)
            x,y = a
            while True:
                x += dx
                y += dy
                if (x,y) == cur: # clear path from cur to a
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
        vec = normalize_slope(roid, station_pos)
        if vec not in vectors: # (1,1) and (2,2) have same normalized slope
            vectors.append(vec)
        
    # sort list by angle
    angles = [(v, vec_angle(v[0], v[1])) for v in vectors]
    angles.sort(key=lambda t:t[1])

    print(angles)

    # for each angle, fire laser and count destroyed asteroid if any

    
    # if count == 200, return coordinate of that asteroid
    # if destroyed_count == 200:
    #     pass

# return angle of vector in degrees
def vec_angle(x, y):
    if x == 0:
        ang = 0 if y > 0 else math.pi
    else:
        ang = math.atan(y/x)
    return abs(math.degrees(ang)) + quadrant_adjustment(x, y)

# return angle in degrees by which to adjust result of atan(y,x),
# which ranges between -90 and 90 degrees
def quadrant_adjustment(x, y):
    if x > 0 and y > 0:
        return 0.0
    elif x > 0 and y < 0:
        return 90.0
    elif x < 0 and y < 0:
        return 180.0
    elif x < 0 and y > 0:
        return 270.0
    return 0.0

def normalize_slope(a1, a2):
    slope = (a1[0] - a2[0], a1[1] - a2[1])
    # print(f"Slope from {a1} to {a2} = {slope}")
    gcd = math.gcd(slope[0], slope[1])
    normalized = (slope[0]/gcd, slope[1]/gcd)
    # print(f"Normalized to {normalized}")
    return normalized

if __name__ == "__main__":
    asteroids, station_pos = parse_day10("day10input.txt")
    solve1(asteroids)
    # solve2(asteroids, (37,25))
    # print(f"Station pos = {station_pos}")
    # solve2(asteroids, station_pos)
