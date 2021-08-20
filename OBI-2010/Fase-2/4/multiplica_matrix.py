def main(file_input=input, test=False):    
    n = int(file_input())
    p, q, r, s, x, y = map(int, file_input().split())
    i, j = map(int, file_input().split())

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
    