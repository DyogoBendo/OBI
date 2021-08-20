def main(file_input=input, test=False):
    a = int(file_input())
    n = int(file_input())
    c = 0
    MINIMO_FOTONS = 40000000

    for _ in range(n):
        f = int(file_input())
        if f * a >= MINIMO_FOTONS:
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()