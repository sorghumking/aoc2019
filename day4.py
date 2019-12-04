
def part1(lo, hi):
    legit_passwords = []
    for pw in range(lo, hi+1):
        if legit(pw):
            legit_passwords.append(pw)
    print("Total legit passwords = {}".format(len(legit_passwords)))

def part2(lo, hi):
    legit_passwords = []
    for pw in range(lo, hi+1):
        if legit(pw, False) and legit2(pw):
            legit_passwords.append(pw)
    print("Total legit passwords = {}".format(len(legit_passwords)))

def legit(pw, double_check=True):
    # print("Testing {}".format(pw))
    spw = str(pw)
    if len(spw) != 6:
        # print("Bad length")
        return False
    double = False
    for idx, c in enumerate(spw):
        if idx <= 4:
            if double_check:
                if c == spw[idx + 1]:
                    double = True
            else:
                double = True
            if int(c) > int(spw[idx + 1]):
                # print("Non-ascending")
                return False
    # if double:
    #     print("Good")
    # else:
    #     print("No double found")
    return double

# f*cking gross, surely there's a better way
def legit2(pw):
    spw = str(pw)
    start_idx = 0
    next_idx = 1
    matches = []
    cur_match = 0
    while next_idx < 6:
        if spw[start_idx] == spw[next_idx]:
            cur_match += 1
        else:
            if cur_match > 0:
                matches.append(cur_match)
                cur_match = 0
            start_idx = next_idx
        next_idx += 1
        if next_idx == 6 and cur_match > 0:
            matches.append(cur_match)

    # print("testing password {}: matches = {}, legit = {}".format(pw, matches, 1 in matches))
    return 1 in matches
    

if __name__ == "__main__":
    part2(240298, 784956)
    # legit2(112233)
    # legit2(123444)
    # legit2(111122)