def main(entrada=input, test=False):
    n = int(entrada())
    m = list(map(int, entrada().split()))

    px = 4
    py = 3
    c = 0

    for movimento in m:
        c += 1
        if movimento == 1:
            px += 1
            py += 2
        if movimento == 2:
            px += 2
            py += 1
        if movimento == 3:
            px += 2
            py -= 1
        if movimento == 4:
            px += 1
            py -= 2
        if movimento == 5:
            px -= 1
            py -= 2
        if movimento == 6:
            px -= 2
            py -= 1
        if movimento == 7:
            px -= 2
            py += 1
        if movimento == 8:
            px -= 1
            py += 2
        if px == 1 and py == 3:
            break
        if px == 2 and py == 3:
            break
        if px == 2 and py == 5:
            break
        if px == 5 and py == 4:
            break

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()