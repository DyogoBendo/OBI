def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    arestas = [[0 for _ in range(n + 1)] for _ in range(n + 1)]    
    entros_max = -1
    for i in range(m):
        x, y, z = map(int, entrada().split())        
        arestas[x][y] = z
        arestas[y][x] = z

    
    for v in range(1, n + 1):
        e = 0  # entrosamento total de v        
        i1, i2 = (0, 0) # integrantes

        for u in range(v + 1, n + 1):    
            wu = arestas[v][u]  # valor de entrosamento do integrante u com v               
            for t in range(u + 1, n + 1):               
                wt = arestas[v][t]  # valor de entrosamento do integrante t com v
                wut = arestas[u][t]  # valro de entrosamento do integrante t com y
                w = wt + wu + wut
                if w > e:
                    i1, i2, e = u, t, w                
        if e > entros_max:
            entros_max = e
            integrantes = (v, i1, i2)    
    if m != 0:
        c = f'{integrantes[0]} {integrantes[1]} {integrantes[2]}'
    else:
        c = f'{integrantes[0]} 2 3'
    
# mostra resultado errado apesar de estar identico ao gabarito
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()