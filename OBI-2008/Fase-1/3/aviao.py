if __name__ == '__main__':
    f, c, e, b = map(int, input().split())

    fs = ((b - 1) // c) + e
    cs = ((b - 1) % c)

    if fs > f:
        print("PROXIMO VOO")
    else:
        l = chr(ord("A") + cs)
        print(fs, l)