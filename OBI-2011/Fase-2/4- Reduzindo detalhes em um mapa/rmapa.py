from heapq import *

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    arestas = [[] for _ in range(n)]

    for i in range(m):
        u, v, c = map(int, entrada().split())
        arestas[u - 1].append((v - 1, c))
        arestas[v - 1].append((u - 1, c))
    
    custo_total = 0
    cidades_visitadas = {0}
    arestas_faltando = []
    for v, w in arestas[0]:        
        a = (w, v)
        heappush(arestas_faltando, a)
    
    while len(cidades_visitadas) < n:        
        w, v = heappop(arestas_faltando)        
        if v in cidades_visitadas:            
            continue
        else:
            cidades_visitadas.add(v)            
            custo_total += w
            for u, c in arestas[v]:
                heappush(arestas_faltando, (c, u))    

    if not test:
        print(custo_total)
    else:
        return [c]

if __name__ == '__main__':
    main()