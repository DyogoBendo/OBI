def main(file_input=input, test=False):
    n, k = map(int, file_input().split())

    mapa = [[False for _ in range(n)] for _ in range(n)]
    pistas = []
    
    c = 0    

    for _ in range(k):
        x, y, d = map(int, file_input().split())
        mapa[y][x] = d
        pistas.append((y, x, d))

    for i in range(n):
        for j in range(n):
            if mapa[i][j] is False:
                is_possible = True
                for y, x, d in pistas:
                    dy = abs(y - i)
                    dx = abs(x - j)
                    dt = dy + dx                    
                    if dt != d:
                        is_possible = False                    
                if is_possible:
                    c += 1
                    if c == 1:
                        solução = (j, i)
                    else:
                        solução = (-1, -1)

    if not test:
        print(solução[0], solução[1])
    else:
        return [f'{solução[0]} {solução[1]}']

if __name__ == '__main__':
    main()