def main(entrada=input, test=False):
    n = int(entrada())
    x = int(entrada())
    y = int(entrada())
    z = int(entrada())
    lista = [x, y, z]
    lista.sort()
    c = 0
    for i in range(len(lista)):
        if lista[i] <= n:  # se for possível evoluir com o número de doces
            n -= lista[i]  # diminuimos o número de doces
            c += 1  

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()