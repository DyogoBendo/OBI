import sys
sys.setrecursionlimit(15000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = 0
m = 0

def time_for_recursion(i, j, id):    
    global barcos, tabuleiro
    barco_size = 1
    barcos[i][j] = id
    for k in range(4):
        i2 = i + dx[k]
        j2 = j + dy[k]

        if i2 < 0 or j2 < 0 or i2 >= n or j2 >= m:
            continue
        if tabuleiro[i2][j2] == "#" and barcos[i2][j2] == -1:
            barco_size += time_for_recursion(i2, j2, id)
    return barco_size

def main(entrada=input, test=False):    
    global tabuleiro, barcos, dx, dy,n, m
    n, m = map(int, entrada().split())          
    tabuleiro = []
    barcos = []
    for i in range(n):
        e = entrada()          
        tabuleiro.append(e)                
        barcos.append([-1 for _ in range(m)])
    
    tamanho = []        
    k = 0    
    for i in range(n):
        for j in range(m):                        
            if tabuleiro[i][j] == '#' and barcos[i][j] == -1:
                tamanho.append(time_for_recursion(i, j, k))
                k += 1
    s = int(entrada())

    barcos_destruidos = 0    
    for i in range(s):
        l, c = map(int, entrada().split())  

        barco_valor = barcos[l - 1][c - 1]
        if barco_valor != -1:
            tamanho[barco_valor] -= 1
            if tamanho[barco_valor] == 0:
                barcos_destruidos += 1
            barcos[l - 1][c - 1] = -1

    c = barcos_destruidos    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
