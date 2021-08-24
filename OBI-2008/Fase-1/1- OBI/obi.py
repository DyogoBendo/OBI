def main(entrada=input, test=False):    
    n, p = map(int, entrada().split())
    c = 0
    for i in range(n):
        f1, f2 = map(int, entrada().split())
        if f1 + f2 >= p:
            c += 1    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()

    