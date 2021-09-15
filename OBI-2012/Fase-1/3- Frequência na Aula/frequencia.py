def main(entrada=input, test=False):
    n = int(entrada())
    c = set()  # guardamos a presenta em um set, que não possuí repetição de elementos
    for _ in range(n):
        c.add(int(entrada()))    

    if not test:
        print(len(c))
    else:
        return [len(c)]

if __name__ == '__main__':
    main()