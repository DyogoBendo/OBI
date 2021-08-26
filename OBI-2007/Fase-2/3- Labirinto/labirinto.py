from math import inf
from queue import Queue
global N, M, tab, dist, fila, DIRECTIONS

class Vertex():  # vertex representa os pontos do tabuleiro, suas coordenadas e seu valor 
    def __init__(self, l, c, t) -> None:
        self.l = l  # linha do vertex
        self.c = c  # coluna do vertex
        self.t = t  # valor do vertex, que pode ser entre 0 e 9, a altura da célula segundo o enunciado

def bfs():
    global fila, dist, tab         
    fila = Queue(maxsize=0)  # criamos uma fila para trabalhar com a bfs
    fila.put(Vertex(0, 0, 0))
    dist[0][0][0] = 0  # a distancia do ponto inicial em relação a si mesmo é 0
    
    while (not fila.empty()):
        v = fila.get()  # pegamos o vertex que "chegou primeiro"
        for d in range(5):  # verificamos cada uma das posições vizinhas para o vertex, incluindo ficar parado
            nl = v.l + DIRECTIONS[d][0]  # linha vizinha
            nc = v.c + DIRECTIONS[d][1]  # coluna vizinha
            nt = (v.t + 1) % 10   # valor do vertex nessa tentativa de chegar na vizinha
            # caso o valor seja igual a 10, voltamos para 0, como é dito pelo enunciado
            
            if nl < 0 or N <= nl or nc < 0 or M <= nc:  # não consideramos os casos em que a linha ultrapassa o número de linhas, ou o mesmo com as colunas
                continue
            if (tab[nl][nc] + v.t) % 10 - 1 >  (tab[v.l][v.c] + v.t) % 10:  # caso o valor da posição vizinha seja superior ao da posição atual não podem chegar nela
                continue
            if dist[nl][nc][nt] < inf:  # se já tivermos caido no caso dessa posição vizinha com esse valor, então não precisamos verificar novamente
                continue
            dist[nl][nc][nt] = dist[v.l][v.c][v.t] + 1  # se chegarmos aqui, significa que é válido ir da posição atual para a vizinha, então armazenamos a distância 
            fila.put(Vertex(nl, nc, nt))  # e agora adicionamos essa posição vizinha para ser analisada como uma posição "inicial" posteriormente

def main(entrada=input, test=False):
    global DIRECTIONS, dist, N, M, tab
    DIRECTIONS = [[0,0], [1, 0], [0, 1], [-1, 0], [0, -1]]  
    # direções -> mesmo lugar, baixo, direita, cima, esquerda
    #          [-1, 0]
    #  [0, -1] [0, 0] [0, 1]
    #          [1, 0]
    
    N, M = map(int, entrada().split())
    
    tab = [0 for _ in range(N)]  # criamos nosso tabuleiro, de n linhas
    dist = [[[inf for _ in range(10)]for _ in range(M) ]for _ in range(N)]  
    # criamos nossa matriz tridimensional de distâncias, em que consideramos a distância em relação ao ponto inicial dada a coordenada do ponto e o valor que possuía
    
    for i in range(N):
        tab[i] = list(map(int, entrada().split()))
    
    bfs()        
    ans = inf
    
    for i in range(10):
        ans = min(ans, dist[N-1][M-1][i])  
        # verificamos para qual valor na última linha e última coluna temos a menor distância e pegamos essa distância
    
    if not test:
        print(ans)
    else:
        return [ans]

if __name__ == '__main__':
    main()
    