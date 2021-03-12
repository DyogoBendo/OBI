global n, t, grafo, presente, sinal, matrix

def convert_to_number(letra):
    if letra == "A":
        return 0
    else:
        return 1

def dfs(c, a, b):
    global matrix    
    global presente
    global sinal
    global n
    
    if not matrix[c][a][b]:
        matrix[c][a][b] = 1
    
    if a + b + presente[c] <= t:
        if not sinal[c]:
            dfs(c, a + presente[c], b)
        else:
            dfs(c, a, b + presente[c])
        
        for i in range(n):
            if grafo[c][i]:
                dfs(i, a, b)

if __name__ == "__main__":
    matrix = [[[0 for _ in range(32)] for _ in range(128)] for _ in range(128)]
    grafo = [[0 for _ in range(32)] for _ in range(32)]
    
    n = int(input())
    t = int(input())
    
    presente = [None for i in range(n)]
    sinal = [None for i in range(n)]
    
    for i in range(n):
        entrada = input().split()
        idc = int(entrada[0])
        presente[i] = int(entrada[1])
        tipo = entrada[2]
        nv = int(entrada[3])
        sinal[i] = convert_to_number(tipo)
        for j in range(4, 4 + nv):
            v = entrada[j]
            grafo[i][v] = 1
    
    dfs(0, 0, 0)
    
    r = 128
    
    for i in range(n):
        for j in range(128):
            for k in range(128):
                if j + k > 0 and matrix[i][j][k] and r > abs(j - k):
                    print(i, j, k)
                    r = abs(j - k)
    print(r)
    
    