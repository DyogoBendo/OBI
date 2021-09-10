from sys import stdin

def bst(grafo, fila):
    visitados = set()
    mais_longe = -1
    while fila:  # enquanto houverem elementos a serem visitados
        cidade, distancia = fila.pop(0)  # pegamos a cidade e sua distância, na ordem do primeiro que entrou
        if cidade in visitados:  # se essa cidade já foi visitada, pulamos
            continue
        visitados.add(cidade)  # adicionamos a cidade em visitados para que não a visitemos novamente

        if distancia > mais_longe:  # se a distancia for maior que mais longe
            mais_longe = distancia  # essa é a nova distância
            idx = cidade  # e a cidade que tem a maior distancia

        for b in grafo[cidade]:            
            if b not in visitados:  # adicionamos todos os elementos que podem ser alcançados a partir da cidade que estamos avaliando agora na fila, que ainda não foram avaliados
                fila.append((b, distancia + 1))   # a distancia deles é a distância atual mais um, pois estão um nível "abaixo" a mais que a cidade atual em relação ao ponto inicial
    return (mais_longe, idx)  # retornamos a cidade mais distante e a sua distância



def main(entrada=stdin.readline, test=False):
    n = int(entrada())

    grafo = [[] for _ in range(n)]

    for _ in range(n - 1):        
        a, b = map(int, entrada().split())
        grafo[a - 1].append(b - 1) 
        grafo[b - 1].append(a - 1)
        # armazenamos cada uma das ligações no grafo

    fila = []    
    fila.append((0, 0))  # a fila armazena a cidade e a sua distância em relação ao ponto inicial, nesse caso, a distância é 0 porque é a distância em relação a si mesmo
    _, idx = bst(grafo, fila)

    fila.append((idx, 0)) # faremos a mesma busca, agora partindo da cidade mais distante que encontramos anteriormente
    c, _ = bst(grafo, fila)  # então obteremos a distância da cidade mais distante em relação a outra cidade mais distante, que é a distância máxima

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()