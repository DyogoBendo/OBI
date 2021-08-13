def main(file_input=input, test=False):
    n = int(file_input())
    casas = set()
    for i in range(n):
        casas.add(int(file_input()))
    k = int(file_input())    
    
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