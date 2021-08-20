def main(file_input=input, test=False):
    n = int(file_input())
    notas = list(map(int, file_input().split()))

    valores = [0 for _ in range(101)]

    for i in range(n):
        k = notas[i]
        valores[k] += 1
    
    c = 0
    d = 0
    for i in range(100, -1, -1):
        if valores[i] > d:
            c = i
            d = valores[i]

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()