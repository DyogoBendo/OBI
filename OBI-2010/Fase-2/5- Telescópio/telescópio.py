def main(entrada=input, test=False):
    a = int(entrada())
    n = int(entrada())
    c = 0
    MINIMO_FOTONS = 40000000

    for _ in range(n):
        f = int(entrada())
        if f * a >= MINIMO_FOTONS:
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()