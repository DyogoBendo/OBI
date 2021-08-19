def main(file_input=input, test=False):
    n = int(file_input())
    x = int(file_input())
    y = int(file_input())
    z = int(file_input())
    lista = [x, y, z]
    lista.sort()
    c = 0
    for i in range(len(lista)):
        if lista[i] <= n:
            n -= lista[i]
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()