if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))  # quantidade de partes que o chocolate é dividido
    resultado = 0  # número de partes que serão guardadas
    
    for i in a:
        resultado += (i - 1)
    
    print(resultado)