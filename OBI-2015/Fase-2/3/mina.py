from math import inf, log2

# n ^ 4 da TLE

def main(file_input=input, test=False):
    n = int(file_input())
    matriz = []
    for i in range(n):
        linha = list(map(int, file_input().split()))
        matriz.append(linha)
    
    tabela_distancia = [[0 if i == 0 and j ==0 else inf for i in range(n)] for j in range(n)]

    for l in range(n):        
        for i in range(n):
            for j in range(n):                
                lado_d = tabela_distancia[i][j + 1] if j < n -1 else inf
                lado_e = tabela_distancia[i][j - 1] if j > 0 else inf
                cima = tabela_distancia[i - 1][j] if i > 0 else inf
                baixo = tabela_distancia[i + 1][j] if i < n - 1 else inf
                atual = tabela_distancia[i][j]
                tabela_distancia[i][j] = min(atual, lado_d, lado_e, cima, baixo) + matriz[i][j]
        c = tabela_distancia[n-1][n-1]
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()