def main(entrada=input, test=False):
    n = int(entrada())
    dario = 0
    xerxes = 0    

    for i in range(n):
        d, x = map(int, entrada().split())
        if x == (d + 1) % 5 or x == (d + 2) % 5:
            dario += 1
        else:
            xerxes += 1

    c = 'dario' if dario > xerxes else 'xerxes'

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()