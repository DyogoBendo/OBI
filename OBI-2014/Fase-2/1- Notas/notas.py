def main(entrada=input, test=False):
    n = int(entrada())
    notas = list(map(int, entrada().split()))

    valores = [0 for _ in range(101)]  # os valores que são possíveis

    for i in range(n):
        k = notas[i]
        valores[k] += 1 
    
    c = 0
    d = 0
    for i in range(100, -1, -1):
        if valores[i] > d:  # verificamos se o valor é o mais frequente
            c = i
            d = valores[i]

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()