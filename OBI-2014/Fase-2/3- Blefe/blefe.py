def main(entrada=input, test=False):
    n,m = map(int, entrada().split())

    a = set(map(int, entrada().split()))
    b = list(map(int, entrada().split()))
    contados_b = set()    

    p = True
    invalido = 0

    for i in range(m):
        caso = False
        if b[i] in a:
            caso = True
        else:
            for j in range(i):
                if b[i] - b[j] in contados_b:
                    caso = True
        if caso is True:
            contados_b.add(b[i])
        else:
            p = False
            invalido = b[i]
    c = "sim" if p else invalido
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()