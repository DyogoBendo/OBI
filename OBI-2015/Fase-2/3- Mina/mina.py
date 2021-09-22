from heapq import *
from math import inf

class Elemento:
    def __init__(self, ai, aj):
        self.i = ai
        self.j = aj
    def __lt__(self, other):
        return self.i > other.i

class Quadrado:
    def __init__(self, av: int, ad: int, am: bool):
        self.v = av  # valor -> 0 se for um caminho livre, 1 se possuir pedras
        self.d = ad  # distância em relação ao ponto inicia
        self.m = am  # se essa posição foi marcada ou não, utilizada na verificação das posições

def main(entrada=input, test=False):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = int(entrada())    
    mina = [[Quadrado(0, inf, False) for j in range(n)] for i in range(n)]  # cada posição da mina é composta por um quadrado
    for i in range(n):
        linha = list(map(int, entrada().split()))
        for j in range(n):
            mina[i][j].v = linha[j]  # atribuímos a cada quadrado seu valor
    q = []
    d = [0, 1, 0, -1, 0]
    mina[0][0].d = 0  # a distancia do primeiro quadrado em relação a si é 0
    heappush(q, (0, Elemento(0, 0)))  # adicionamos o elemento de coordanada 0,0 que tem o valor 0

    while q:
        e = heappop(q)  # pegamos o elemento de menor distância/custo que já descobrimos
        f = e[1]  # f é as coordenadas do elemento
        if not mina[f.i][f.j].m:  # se a mina na posição do elemento não tiver sido descoberta ainda
            mina[f.i][f.j].m = True  # agora terá sido
            mina[f.i][f.j].d = e[0]  # a distância é igual a distância que foi inserida no heap em relação a esse ponto
            if f.i == n - 1 and f.j == n - 1: break  # se chegamos a última posição da mina, não tem porque continuar, pois é ele que estamos querendo
            for k in range(4):  # agora verificamos cada uma das posições adjacentes
                a = f.i + d[k]  # a é a linha
                b = f.j + d[k + 1]  # b a coluna
                if a >= 0 and a < n and b >= 0 and b < n and not mina[a][b].m:  # se essas posições não extrapolarem os limites da matriz e derem a posição de um quadrado que ainda não foi considerado
                    heappush(q, (e[0] + mina[a][b].v, Elemento(a, b)))  # então adicionamos o quadrado que as coordenadas a e b representam
                    # com o custo sendo o custo até chegar nelas, mais o valor que elas representam, isto é, mais 0 se for um caminho livre, e mais 1 se for um caminho com pedras
    c = mina[-1][-1].d  # custo para se chegar na última posição
    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()