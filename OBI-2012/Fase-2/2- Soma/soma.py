def main(entrada=input, test=False):
    n = int(entrada())
    casas = set()
    for i in range(n):
        casas.add(int(entrada()))
    k = int(entrada())    
    
    for casa in casas:
        par = k - casa
        if par in casas:
            if par > casa:
                dupla = (casa, par)
            else:
                dupla = (par, casa)
            break

    if not test:
        print(dupla[0], dupla[1])
    else:
        return [f"{dupla[0]} {dupla[1]}"]

if __name__ == '__main__':
    main()