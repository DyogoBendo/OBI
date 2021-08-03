coordenadas_adicionadas = set()
tabuleiro = []

def adiciona_coordenada(barcos, existente, nova):
    for barco in barcos:
        if existente in barco:
            barco.append(nova)
            coordenadas_adicionadas.add(nova)

if __name__ == '__main__':
    n, m = map(int, input().split())
    barcos = []    
    for i in range(n):
        tabuleiro.append(input())
    for i in range(n):
        for j in range(m):
            if tabuleiro[i][j] == '#':
                coordenadas = (i, j)                
                if coordenadas not in coordenadas_adicionadas:
                    if j < m - 1:
                        vizinho_direita = (i, j + 1)
                        if vizinho_direita in coordenadas_adicionadas:
                            adiciona_coordenada(barcos, vizinho_direita, (i, j))
                        else:
                            barcos.append([(i,j)])
                            coordenadas_adicionadas.add(coordenadas)    
                    else:
                        barcos.append([(i,j)])
                        coordenadas_adicionadas.add(coordenadas)
                if j < m - 1:
                    if tabuleiro[i][j + 1] == '#':
                        coordenadas = (i, j + 1)
                        if coordenadas not in coordenadas_adicionadas:
                            adiciona_coordenada(barcos, (i, j), coordenadas)
                        else:
                            for barco in barcos:
                                if (i, j + 1) in barco:
                                    barco.append((i, j))
                                    coordenadas_adicionadas.add((i, j + 1))
                if i < n - 1:
                    if tabuleiro[i + 1][j] == '#':
                        coordenadas = (i + 1, j)
                        if coordenadas not in coordenadas_adicionadas:
                            for barco in barcos:
                                if (i, j) in barco:
                                    barco.append(coordenadas)
                                    coordenadas_adicionadas.add(coordenadas)
                        else:
                            for barco in barcos:
                                if (i + 1, j) in barco:
                                    barco.append((i, j))
                                    coordenadas_adicionadas.add((i + 1, j))
    k = int(input())

    barcos_destruidos = 0
    print(barcos)
    print()
    for i in range(k):
        l, c = map(int, input().split())  
        for barco in barcos:
            try:                
                barco.remove((l - 1, c - 1))
                if len(barco) == 0:
                    barcos_destruidos += 1
            except:
                pass    
    print(barcos)
    print(barcos_destruidos)