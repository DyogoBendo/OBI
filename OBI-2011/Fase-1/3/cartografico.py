from sys import stdin


def bst(grafo, pilha):
    visitados = set()
    mais_longe = -1
    while pilha:
        cidade, distancia = pilha.pop(0) 
        if cidade in visitados:
            continue
        visitados.add(cidade)      

        if distancia > mais_longe:
            mais_longe = distancia
            idx = cidade

        for b in grafo[cidade]:            
            if b not in visitados:
                pilha.append((b, distancia + 1))        
    return (mais_longe, idx)



def main(file_input=stdin.readline, test=False):
    n = int(file_input())

    grafo = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, file_input().split())
        grafo[a - 1].append(b - 1)
        grafo[b - 1].append(a - 1)

    pilha = []    
    pilha.append((0, 0))  # a pilha armazena a cidade e o seu valor    
    _, idx = bst(grafo, pilha)

    pilha.append((idx, 0))
    c, _ = bst(grafo, pilha)

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()