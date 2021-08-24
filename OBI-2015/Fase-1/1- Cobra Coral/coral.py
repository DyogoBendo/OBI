def main(entrada=input, test=False):
    w, x, y, z = map(int, entrada().split())

    c = "F" if w == z else "V"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()