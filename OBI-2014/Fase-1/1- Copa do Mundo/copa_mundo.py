# problema de arvore geradora minima
from heapq import *

def main(entrada=input, test=False):
    n, f, r = map(int, entrada().split())

    cidades = [[] for _ in range(n)]
    ferrovias = [[] for _ in range(n)]
    rodovias = [[] for _ in range(n)]
    for i in range(f):
        a, b, k = map(int, entrada().split())
        a -= 1
        b -= 1
        cidades[a].append((0, k, b))
        cidades[b].append((0, k, a))
    for i in range(r):
        a, b, k = map(int, entrada().split())
        a -= 1
        b -= 1
        cidades[a].append((1, k, b))
        cidades[b].append((1, k, a))

    c = 0            
    arvore_minima_vertices = {0}
    arvore_minima_arestas = cidades[0]
    heapify(arvore_minima_arestas)            
    while arvore_minima_arestas:        
        _, k, b = heappop(arvore_minima_arestas)    
        if b not in arvore_minima_vertices:            
            arvore_minima_vertices.add(b)
            c += k
            for t, w, u in cidades[b]:
                heappush(arvore_minima_arestas, (t, w, u))    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()