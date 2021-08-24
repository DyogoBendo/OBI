def main(entrada=input, test=False):
    n = int(entrada())
    d = int(entrada())
    a = int(entrada())

    if a > d:
        c = n - a + d
    else:
        c = d - a

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()