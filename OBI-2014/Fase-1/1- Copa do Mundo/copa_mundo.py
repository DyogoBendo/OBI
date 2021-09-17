# problema de arvore geradora minima
from heapq import *

def main(entrada=input, test=False):
    n, f, r = map(int, entrada().split())
    cidades = [[] for _ in range(n)]    
    for _ in range(f):
        a, b, k = map(int, entrada().split())
        a -= 1
        b -= 1
        cidades[a].append((0, k, b))  # adicionamos as arestas de cada uma das ferrovias
        cidades[b].append((0, k, a))  # as ferrovias possuem prioridade maior, por isso adicionamos com um 0 a frente
    for _ in range(r):
        a, b, k = map(int, entrada().split())
        a -= 1
        b -= 1
        cidades[a].append((1, k, b))  # adicionamos as arestas das rodovias
        cidades[b].append((1, k, a))  # elas possuem uma menor prioridade, por isso adicionamos as arestas com 1 no início

    c = 0            
    arvore_minima_vertices = {0}  # mantemos as cidades adicionadas, iniciando pela 0
    arvore_minima_arestas = cidades[0]
    heapify(arvore_minima_arestas)            
    while arvore_minima_arestas:  # enquanto houverem arestas a serem consideradas
        _, k, b = heappop(arvore_minima_arestas)  # removemos a de maior prioridade    
        if b not in arvore_minima_vertices:  # se ainda não consideramos a cidade b            
            arvore_minima_vertices.add(b)  # adicionamos a cidade b nas cidades consideradas
            c += k  # aumentamos o custo das obras
            for t, w, u in cidades[b]:  # e adicionamos todas as arestas de b para serem consideradas
                heappush(arvore_minima_arestas, (t, w, u))    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()