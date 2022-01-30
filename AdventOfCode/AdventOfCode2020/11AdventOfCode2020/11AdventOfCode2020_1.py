"""
L = empty seat
# = occupied seat
. = floor

Wenn der Sitz L ist, und neben an keiner ist, wird der L zum #
Wenn der Sitz # ist, und vier oder mehr Sitze neben an ebenfalls # ist, wird der Sitz L

"""
def read_input():
    with open("11aoc_data") as f:
        M = [x.strip() for x in f]
        return M

def num_of_filled_seats(m, i0, j0):
    cnt = 0
    for i in range(max(0, i0 - 1), min(i0 + 2, len(m))):
        for j in range(max(0, j0 - 1), min(j0 + 2, len(m[i]))):
            if m[i][j] == '#':
                cnt += 1
    return cnt - (1 if m[i0][j0] == '#' else 0)

def step(m):
    new_m = []
    for i in range(len(m)):
        line = []
        for j in range(len(m[i])):
            if m[i][j] == 'L' and num_of_filled_seats(m, i, j) == 0:
                line.append('#')
            elif m[i][j] == '#' and num_of_filled_seats(m, i, j) >= 4:
                line.append('L')
            else:
                line.append(m[i][j])
        new_m.append(line)
    return new_m

def main():
    m_before = read_input()

    m_after = step(m_before)
    while m_after != m_before:
        m_before, m_after = m_after, step(m_after)
    print(sum([line.count("#") for line in m_after]))
main()

