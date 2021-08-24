def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    toca = []
    posicao_inicial = (0, 0)
    posicao_final = (0, 0)
    for i in range(n):
        linha = list(map(int, entrada().split()))

        try:
            posicao_inicial = (i, linha.index(2))
        except:
            pass
        try:
            posicao_final = (i, linha.index(3))
        except:
            pass
        toca.append(linha)        
    c = 1
    i, j = posicao_final
    ii, ji = posicao_inicial
    ultimo_movimento = 0
    while i!=ii or j != ji:                
        c += 1        
        if j < m -1:            
            if toca[i][j + 1] != 0 and ultimo_movimento != 1:
                j += 1
                ultimo_movimento = 2
                continue
        if j > 0:
            if toca[i][j-1] != 0 and ultimo_movimento != 2:
                j -= 1
                ultimo_movimento = 1
                continue
        if i > 0:
            if toca[i - 1][j] != 0 and ultimo_movimento != 3:
                i -= 1
                ultimo_movimento = 4
                continue
        if i < n-1:
            if toca[i + 1][j] != 0 and ultimo_movimento != 4:
                i += 1
                ultimo_movimento = 3
                continue        

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()