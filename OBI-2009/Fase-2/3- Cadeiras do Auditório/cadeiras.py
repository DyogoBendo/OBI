def main(entrada=input, test=False):    
    l, c = map(int, entrada().split())
    auditorio = []
    for _ in range(l):
        cadeiras = list(map(int, entrada().split()))
        auditorio.append(cadeiras)
    
    mark = [0 for _ in range(c)]
    col = [(auditorio[0][i] - 1) % c for i in range(c)]

    print(col)    
    nc = 0
    mc = []

    # arruma as colunas da primeira linha
    for i in range(c):
        if mark[i]:  # caso já tenha sido considerada essa coluna, pulamos a execução
            continue
        atual = col[i]
        while atual != i:  # enquanto o atual não for o número da posição atual da coluna que procuramos
            troca_coluna = (atual + 1, col[atual] + 1)  # trocamos o atual com a posição que o atual deveria estar
            mc.append(troca_coluna)
            nc += 1
            mark[atual] = 1  # e marcamos que essa coluna já foi considerada
            atual = col[atual]

    mark = [0 for _ in range(l)]
    lin = [(auditorio[i][0] - 1) // c for i in range(l)]

    nl = 0
    ml = []

    # e as linhas da primeira coluna, o código é identico
    for i in range(l):
        if mark[i]:
            continue
        atual = lin[i]
        while atual != i:
            troca_linha = (atual + 1, lin[atual] + 1)
            ml.append(troca_linha)
            nl += 1
            mark[atual] = 1
            atual = lin[atual]
    # logo, todo o resto deve estar correto
    r = []
    if not test:

        print(nc + nl)
        for i in range(nl):
            print(ml[i][0], ml[i][1])
        for i in range(nc):
            print(mc[i][0], mc[i][1])
    else:
        r.append(nc + nl)        
        return r
if __name__ == '__main__':
    main()
    