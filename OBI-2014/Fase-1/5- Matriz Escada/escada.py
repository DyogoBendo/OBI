def main(entrada=input, test=False):
    n, m = map(int, entrada().split())    
    p = True
    for i in range(n):  # verificamos cada linha
        linha = list(map(int, entrada().split()))
        if i > 0:  # se for a segunda linha para frente 
            if sum(linha[0:k + 1]) > 0:  # se a soma até a coluna que deveria ser de apenas 0 for maior que 0, significa que existe um não 0                 
                p = False  # dessa forma, não é uma matriz escada válida
        k = n - 1  # iniciamos k como a última coluna
        for j in range(m):
            if linha[j] > 0:
                k = j  # k recebe a primeira coluna diferente de 0 
                break
    c = "S" if p else "N"
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()