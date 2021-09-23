from math import factorial

def main(entrada=input, test=False):
    n = int(entrada())
    valores = [[0 for _ in range(n)] for _ in range(n)]  # cada número pode estar em uma das n posições
    for i in range(factorial(n) - 1):
        p = list(map(int, entrada().split()))        
        for i in range(n):            
            v = p[i] - 1
            valores[i][v] += 1  # informamos que na posição i, o número v apareceu
    c = ""

    aparicoes = factorial(n - 1)  # cada número deve aparecer, em cada posição, n - 1!

    for i in range(n):
        for j in range(n):
            if valores[i][j] < aparicoes:  # se o número não apareceu o suficiente naquela posição, então o que falta considera esse número nessa posição                
                c += str(j + 1) + " "  # concatenamos o número então
    if not test:        
        print(c[:-1])
    else:
        return [c[:-1]]

if __name__ == '__main__':
    main()