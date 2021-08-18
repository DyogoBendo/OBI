def main(file_input=input, test=False):
    s = int(file_input())
    n2, n5, n10, n20, n50, n100 = map(int, file_input().split())

    valores = [2, 5, 10, 20, 50, 100]

    k = [[(valores[j] // valores[i], valores[j] % valores[i]) for j in range(6)] for i in range(6)]

    print(k)
    c = 0
    v = s

    notas_usadas = []
    for i in range(5, -1, -1):
        n = v//valores[i]
        v -= n * valores[i]        
        notas_usadas.insert(0, n)
    for i in range(6):
        for j in range(6):
            

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()