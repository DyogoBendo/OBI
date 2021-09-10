from heapq import *

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    arestas = [[] for _ in range(n)]

    for i in range(m):
        u, v, c = map(int, entrada().split())
        arestas[u - 1].append((v - 1, c))  # adicionamos as arestas
        arestas[v - 1].append((u - 1, c))
    
    custo_total = 0
    cidades_visitadas = {0}
    arestas_faltando = []
    for v, w in arestas[0]:        
        a = (w, v)
        heappush(arestas_faltando, a) # adicionamos as arestas próxima que partem da cidade 0
    
    while len(cidades_visitadas) < n:        
        w, v = heappop(arestas_faltando)  # pegamos a aresta de menor valor
        if v in cidades_visitadas:  # se já visitamos essa cidade, vamos para a próxima
            continue
        else:
            cidades_visitadas.add(v) # adicionamos às cidades visitadas
            custo_total += w  # aumentamos o custo total
            for u, c in arestas[v]:
                heappush(arestas_faltando, (c, u))  # adicionamos todas asarestas que partem dessa cidade    

    if not test:
        print(custo_total)
    else:
        return [custo_total]

if __name__ == '__main__':
    main()