def main(entrada=input, test=False):
    n,m = map(int, entrada().split())

    a = set(map(int, entrada().split()))
    b = list(map(int, entrada().split()))
    contados_b = set()    

    p = True
    invalido = 0

    for i in range(m):  # vamos verificar cada número
        caso = False
        if b[i] in a:  # se o número está em a, então é válido
            caso = True
        else:
            for j in range(i):
                if b[i] - b[j] in contados_b:  # se ele for a noma de dois números considerados, também
                    caso = True
                    break
        if caso is True:
            contados_b.add(b[i])  # se for um caso válido, então ele entra para os números que estamos considerando para verificação de pertinência
        else:
            p = False
            invalido = b[i]
            break
    c = "sim" if p else invalido
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()