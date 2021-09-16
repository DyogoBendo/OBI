from math import sqrt

def main(entrada=input, test=False):
    n, d = map(int, entrada().split())
    d *= d  # distancia ao quadrado
    
    arvores = []
    for i in range(n):
        x, y = map(int, entrada().split())
        arvores.append((i, x, y))

    pilha = [arvores[0]]  # começamos verificando pela primeira árvore, poderia ser qualquer outra
    arvores_consideradas = [True if i == 0 else False for i in range(n)]  # mantemos um array que informa se naquela a árvore daquela posição já foi considerada

    while pilha:
        _, xi, yi = pilha.pop()  # removemos a última árvore adicionada

        for f, xf, yf in arvores:  # para comparar com cada uma das outras árvores
            if arvores_consideradas[f] == True:  # se ela já foi considerada, pulamos
                continue
            distancia = (xi - xf) ** 2 + (yi - yf) ** 2 # senão, verificamos sua distância em relação a árvore atual
            if distancia <= d :  # se for menor que a distância máxima, significa que ela pode ser adicionada ao grafo
                arvores_consideradas[f] = True  # assim, essa árvore conta como considerada
                pilha.append((f, xf, yf))  # e suas ligações serão chegadas posteriormente

    c = False
    for caso in arvores_consideradas:
        if caso is False:  # se tiver alguma árvore que não se conectou ao grafo, então é um caso inválido
            break      
    else:  # se todas as árvores se conectam
        c = True
        
    if not test:
        if c:
            print("S")
        else:
            print("N")        
    else:
        if c:
            return["S"]
        else:
            return["N"]

if __name__ == '__main__':
    main()