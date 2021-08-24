def main(entrada=input, test=False):
    n = int(entrada())
    arvores = []
    for i in range(n):
        x, h = map(int, entrada().split())
        arvores.append((x, h))

    c=0
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()