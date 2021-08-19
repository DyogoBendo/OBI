def main(file_input=input, test=False):
    n, k = map(int, file_input().split())
    primos = list(map(int, file_input().split()))
    numeros = [i for i in range(n + 1)]    
    for i in primos:
        for j in range(i, n + 1, i):            
            numeros[j] = 0    
    c = n - numeros.count(0) + 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()