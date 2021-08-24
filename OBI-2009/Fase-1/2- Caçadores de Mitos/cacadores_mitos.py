def main(entrada=input, test=False):    
    n = int(entrada())    
    lista = [[0 for _ in range(501)] for _ in range(501)]
    is_mito = True
    for i in range(n):
        x, y = map(int, entrada().split())
        k = lista[x][y]
        if k == 1:
            is_mito = False
        lista[x][y] = 1

    c = 0 if is_mito else 1    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
    
