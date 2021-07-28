if __name__ == '__main__':
    n, m = map(int, input().split())
    afastou = False
    m_squared = m ** 2
    x = 0
    y = 0
    for _ in range(n):
        c, d = input().split()
        d = int(d)
        if c == 'N':
            y += d
        if c == 'S':
            y -= d
        if c == 'L':
            x += d
        if c == 'O':
            x -= d
        
        euclian_distance = (x ** 2) + (y ** 2)

        if euclian_distance > m_squared:
            afastou = True

    if afastou:
        print(1)
    else:
        print(0)