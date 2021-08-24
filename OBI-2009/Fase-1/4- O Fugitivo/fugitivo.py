from math import hypot
from sys import stdin

def main(entrada=stdin, test=False):    
    n, m = map(int, entrada().split())
    afastou = False    
    x = 0
    y = 0
    for _ in range(n):
        c, d = entrada().split()
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

    c = 1 if afastou else 0    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
    