def main(entrada=input, test=False):
    n, e, s, m = map(int, entrada().split())
    for i in range(m):
        a, b, t = map(int, entrada().split())
        
    c = a * b - t
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()