def main(file_input=input, test=False):
    w, x, y, z = map(int, file_input().split())

    c = "F" if w == z else "V"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()