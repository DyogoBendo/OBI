def main(entrada=input, test=False):    
    l, c = map(int, entrada().split())
    auditorio = []
    for _ in range(l):
        cadeiras = list(map(int, entrada().split()))
        auditorio.append(cadeiras)
    
    mark = [0 for _ in range(c)]
    col = [(auditorio[0][i] - 1) % c for i in range(c)]

    nc = 0
    mc = []

    for i in range(c):
        if mark[i]:
            continue
        atual = col[i]
        while atual != i:
            troca_coluna = (atual + 1, col[atual] + 1)
            mc.append(troca_coluna)
            nc += 1
            mark[atual] = 1
            atual = col[atual]

    mark = [0 for _ in range(l)]
    lin = [(auditorio[i][0] - 1) // c for i in range(l)]

    nl = 0
    ml = []

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
    