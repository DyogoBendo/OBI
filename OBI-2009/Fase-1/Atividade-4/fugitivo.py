from math import hypot

if __name__ == '__main__':
    n, m = map(int, input().split())
    afastou = False    
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
        
        euclian_distance = hypot(x, y)

        if euclian_distance > m:
            afastou = True

    if afastou:
        print(1)
    else:
        print(0)