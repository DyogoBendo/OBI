def main(entrada=input, test=False):
    n = int(entrada())    
    MAX_SIZE = 101
    mar = [[False for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]  # criamos um vetor que representa todos os pontos possíveis do mar
    for _ in range(n):
        xi, xf, yi, yf = map(int, entrada().split())

        for i in range(xi, xf):
            for j in range(yi, yf):                
                mar[i][j] = True   # preenchemos cada um dos pontos que tem rede como True
        
    c = 0

    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            if mar[i][j]:  # procuramos por todos os pontos que tem rede
                c += 1  # e adicionamos a àrea total
  

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()