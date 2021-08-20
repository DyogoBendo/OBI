from math import factorial

def main(file_input=input, test=False):
    n = int(file_input())
    valores = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(factorial(n) - 1):
        p = list(map(int, file_input().split()))        
        for i in range(n):            
            v = p[i] - 1
            valores[i][v] += 1
    c = ""

    aparicoes = factorial(n - 1)

    for i in range(n):
        for j in range(n):
            if valores[i][j] < aparicoes:                
                c += str(j + 1) + " "    
    if not test:        
        print(c[:-1])
    else:
        return [c[-1]]

if __name__ == '__main__':
    main()