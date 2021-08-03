coordenadas_adicionadas = set()
tabuleiro = []
barcos = []    

def adiciona_coordenada(existente, nova):
    for barco in barcos:
        if existente in barco:
            barco.add(nova)
            coordenadas_adicionadas.add(nova)

if __name__ == '__main__':
    n, m = map(int, input().split())
    repeated = []
    for i in range(n):
        tabuleiro.append(input())
    for i in range(n):
        for j in range(m):
            if tabuleiro[i][j] == '#':
                add = 0
                atual = (i, j)
                esquerda = (i, j-1)
                direita = (i, j + 1)
                cima = (i - 1, j)
                baixo = (i + 1, j)

                if esquerda in coordenadas_adicionadas:
                    adiciona_coordenada(esquerda, atual)
                    add += 1
                if direita in coordenadas_adicionadas:
                    adiciona_coordenada(direita, atual)
                    add += 1
                if cima in coordenadas_adicionadas:
                    adiciona_coordenada(cima, atual)
                    add += 1
                if baixo in coordenadas_adicionadas:
                    adiciona_coordenada(baixo, atual)
                    add += 1
                if add == 0:
                    barcos.append({atual})
                elif add > 1:
                    repeated.append(atual)      
                coordenadas_adicionadas.add(atual)                
    for coordenada in repeated:
        merged = set()
        for barco in barcos:
            if coordenada in barco:
                merged = merged.union(barco)
                barcos.remove(barco)
        barcos.append(merged)

    k = int(input())

    barcos_destruidos = 0    
    for i in range(k):
        l, c = map(int, input().split())  
        for barco in barcos:
            try:                
                barco.remove((l - 1, c - 1))
                if len(barco) == 0:
                    barcos_destruidos += 1
            except:
                pass        
    print(barcos_destruidos)