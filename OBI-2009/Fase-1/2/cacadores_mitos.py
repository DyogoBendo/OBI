if __name__ == '__main__':
    n = int(input())    
    lista = [[0 for _ in range(501)] for _ in range(501)]
    is_mito = True
    for i in range(n):
        x, y = map(int, input().split())
        k = lista[x][y]
        if k == 1:
            is_mito = False
        lista[x][y] = 1

    if is_mito:
        print(0)
    else:
        print(1)
