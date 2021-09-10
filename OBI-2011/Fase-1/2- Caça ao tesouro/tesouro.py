def main(entrada=input, test=False):
    n, k = map(int, entrada().split())

    mapa = [[False for _ in range(n)] for _ in range(n)]
    pistas = []
    
    c = 0    

    for _ in range(k):
        x, y, d = map(int, entrada().split())
        mapa[y][x] = d  # armazenamos no mapa cada uma das distâncias fornecidas
        pistas.append((y, x, d))  # e guardamos as pistas dadas

    for i in range(n):
        for j in range(n):
            if mapa[i][j] is False:  # agora verificamos apenas as posições que não tem pistas
                is_possible = True
                for y, x, d in pistas:  # verificamos em cada uma das pistas
                    dy = abs(y - i)
                    dx = abs(x - j)
                    dt = dy + dx                    
                    if dt != d:  # se a distância da pista e a distância de fato batem
                        is_possible = False  # senão, não é um caso possível                    
                if is_possible:  # se for
                    c += 1  # adicionamos um caso
                    if c == 1:  # se for a única solução
                        solução = (j, i)  # é as coordenadas passadas
                    else:
                        solução = (-1, -1)  # senão, existem múltiplas posições

    if not test:
        print(solução[0], solução[1])
    else:
        return [f'{solução[0]} {solução[1]}']

if __name__ == '__main__':
    main()