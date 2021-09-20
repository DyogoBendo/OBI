from queue import Queue

def main(entrada=input, test=False):
    n = int(entrada())
    esquinas = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b, c = map(int, entrada().split())
        a -= 1
        b -= 1
        esquinas[a].append([a, b, c])  # guardamos quem liga com quem, será útil posteriormente
    
    grupos = [1 for _ in range(n)]  # criamos os grupos, eles são o número de elementos que cada grupo possui, inicialmente, cada elemento pertence a um grupo com si mesmo
    id_grupo = [i for i in range(n)]  # id que identifica a que grupo cada elemento participa, inicialmente cada elemento está no seu próprio grupo

    fila = Queue()
    for e in esquinas[0]:  # começamos do elemento 0, poderia ser qualquer outro
        fila.put_nowait(e)    
    vertices_contados = {0}  # colocamos como um elemento contado

    # loop executado exatamente n - 1 vezes
    while not fila.empty():  # enquanto ainda temos arestas a visitar     
        vertice_origem, vertice_destino, tipo = fila.get_nowait()  # pegamos o vértice de origem e de destino , além do tipo
        if vertice_destino in vertices_contados:  # se já visitamos o vértice de destino significa que ele já pertence à um grupo, então pulamos
            continue        

        vertices_contados.add(vertice_destino)  # adicionamos o vértice destino aos vértices que já foram considerados em um grupo
        for e in esquinas[vertice_destino]:  # e adicionamos todas as suas arestas para serem visitadas posteriormente
            fila.put_nowait(e)
        if tipo == 1:  # se essa aresta for uma rua importante, não iremos colocar no grupo            
            continue        

        id_grupo[vertice_destino] = id_grupo[vertice_origem]  # o id do vértice destino se torna o id do vértice de origem
        grupos[id_grupo[vertice_origem]] += 1  # a quantidade de elementos no grupo no id do vértice de origem é aumentado em 1
        grupos[vertice_destino] -= 1  # e no grupo de vértice destino diminuímos em 1, pois ele não faz mais parte daquele grupo

    r = 0  # número de pares importantes
    contados = 0
    for c in grupos:  # agora pegamos quantos elementos tem em cada grupo
        contados += c  # somamos ao número de contados
        r += c * (n - contados)  # somamos o número de pares que podem ser formados que passam por uma rua importante

    if not test:
        print(r)
    else:
        return [r]

if __name__ == '__main__':
    main()