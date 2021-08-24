def main(entrada=input, test=False):
    s = int(entrada())
    n2, n5, n10, n20, n50, n100 = map(int, entrada().split())

    valores = [2, 5, 10, 20, 50, 100]

    k = [[(valores[j] // valores[i], valores[j] % valores[i]) for j in range(6)] for i in range(6)]    
    c = 0
    v = s

    notas_usadas = []
    for i in range(5, -1, -1):
        n = v//valores[i]
        v -= n * valores[i]        
        notas_usadas.insert(0, n)
    for i in range(6):
        for j in range(6):
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()