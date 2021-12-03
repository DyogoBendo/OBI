def main(entrada=input, test=False):
    l, c = map(int, entrada().split())

    direcoes = [
        [0, 0],  # fica na posição
        [-1, 0], # sobe uma linha
        [1, 0],  # desce uma linha
        [0, 1],  # avança para direita
        [0, -1] # avança para a esquerda
    ]

    mapa = []    
    for i in range(l):
        linha = entrada()
        try:            
            coluna_inicial = linha.index('o')            
            linha_inicial = i 
        except:
            pass
        mapa.append(linha)
    
    linha_atual, coluna_atual = linha_inicial, coluna_inicial
    direcao_atual = 0

    while True:
        achou = False
        for i in range(1, 5):            
            if i != direcao_atual:
                linha_possivel = linha_atual + direcoes[i][0]
                coluna_possivel = coluna_atual + direcoes[i][1]
                if -1 < linha_possivel < l and -1 < coluna_possivel < c:
                    if mapa[linha_possivel][coluna_possivel] == 'H':                        
                        direcao_atual = i - 1 if i % 2 == 0 else i + 1
                        linha_atual = linha_possivel
                        coluna_atual = coluna_possivel                        
                        achou = True
        if not achou:
            break
    
    r = f'{linha_atual + 1} {coluna_atual + 1}'

    if not test:
        print(r)
    else:
        return [r]

if __name__ == '__main__':
    main()