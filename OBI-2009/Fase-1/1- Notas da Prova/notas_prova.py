def main(entrada=input, test=False):    
    notas = list('EDCBA')
    values=[(0, 0), (1, 35), (36, 60), (61, 85), (86, 100)]
    k = int(entrada())
    for i in range(5):
        a, b = values[i]
        if a <= k <= b:
            c = notas[i]
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
