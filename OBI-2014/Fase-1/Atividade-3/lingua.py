def main(file_input=input, test=False):
    entrada = file_input().split()
    c = ""
    for e in entrada:
        c += " " + e[1::2]

    if not test:
        print(c[1:])
    else:
        return [c[1:]]

if __name__ == '__main__':
    main()