def main(entrada=input, test=False):
    n = int(entrada())
    c = set()
    for _ in range(n):
        c.add(int(entrada()))
    

    if not test:
        print(len(c))
    else:
        return [len(c)]

if __name__ == '__main__':
    main()