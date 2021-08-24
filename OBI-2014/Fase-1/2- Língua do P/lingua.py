def main(entrada=input, test=False):
    entrada = entrada().split()
    c = ""
    for e in entrada:
        c += " " + e[1::2]

    if not test:
        print(c[1:])
    else:
        return [c[1:]]

if __name__ == '__main__':
    main()