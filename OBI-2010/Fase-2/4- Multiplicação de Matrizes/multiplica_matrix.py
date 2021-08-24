def main(entrada=input, test=False):    
    n = int(entrada())
    p, q, r, s, x, y = map(int, entrada().split())
    i, j = map(int, entrada().split())

    c = 0
    for k in range(1, n + 1):
        a = ((p * i) + (q * k)) % x
        b = ((r * k) + (s * j)) % y        
        c += a * b
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
    