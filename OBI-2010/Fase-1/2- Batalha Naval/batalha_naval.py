import sys
sys.setrecursionlimit(15000)  # precisamos definir isso porque entramos em mais recursões que o limite padrão
dx = [1, 0, -1, 0]  # movimentos x
dy = [0, 1, 0, -1]  # movimentos y
n = 0
m = 0

def time_for_recursion(i, j, id):    # analisamos recursivamente o tabuleiro
    global barcos, tabuleiro
    barco_size = 1
    barcos[i][j] = id  # informamos que essa posição pertence ao barco com esse id
    for k in range(4): # verificamos cada uma das 4 posições possíveis
        i2 = i + dx[k]
        j2 = j + dy[k]

        if i2 < 0 or j2 < 0 or i2 >= n or j2 >= m: # se passar das bordas pulamos esse caso
            continue
        if tabuleiro[i2][j2] == "#" and barcos[i2][j2] == -1:  # caso seja um barco e não tenha um grupo ainda
            barco_size += time_for_recursion(i2, j2, id)  # aumentamos o tamanho do barco desse id
    return barco_size  # retornamos o tamanho total do barco

def main(entrada=input, test=False):    
    global tabuleiro, barcos, dx, dy,n, m
    n, m = map(int, entrada().split())          
    tabuleiro = []
    barcos = []
    for i in range(n):
        e = entrada()          
        tabuleiro.append(e)                
        barcos.append([-1 for _ in range(m)])  # adicionamos todos as posições como sem barco
    
    tamanho = []        
    k = 0    
    for i in range(n):
        for j in range(m):                        
            if tabuleiro[i][j] == '#' and barcos[i][j] == -1:
                tamanho.append(time_for_recursion(i, j, k))  # fazemos a verificação para cada barco e adicionamos o tamanho desse barco
                k += 1
    s = int(entrada())

    barcos_destruidos = 0    
    for i in range(s):
        l, c = map(int, entrada().split())  

        barco_valor = barcos[l - 1][c - 1]
        if barco_valor != -1:
            tamanho[barco_valor] -= 1  # reduzimos o tamanho do barco se ele for != -1
            if tamanho[barco_valor] == 0:  # se após isso o tamanho é 0
                barcos_destruidos += 1  # então temos um barco destruído
            barcos[l - 1][c - 1] = -1  # e essa posição fica sem barco

    c = barcos_destruidos    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
