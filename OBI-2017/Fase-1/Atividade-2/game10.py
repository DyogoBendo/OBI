def main(file_input=input, test=False):
    n = int(file_input())
    d = int(file_input())
    a = int(file_input())

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