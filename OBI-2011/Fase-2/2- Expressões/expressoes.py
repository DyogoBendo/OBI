def main(entrada=input, test=False):
    n = int(entrada())
    r = []
    for i in range(n):
        pilha = []
        a = list(entrada().strip())
        is_valido = True

        for c in a:
            # colocamos em uma pilha o que esperamos para o fechamento do que foi aberto
            # pois o último que é aberto é o primeiro que é fechado
            if c == "{":
                pilha.append("}") 
            elif c == "[":
                pilha.append("]")
            elif c == "(":
                pilha.append(")")
            else:
                try:
                    esperado = pilha.pop()
                    if esperado != c:  # se o que fecha for diferente do que se esperava, então há um erro
                        is_valido = False
                except IndexError:  # assim como se estivermos tentando fechar sem nada aberto
                    is_valido = False
        if len(pilha) > 0:  # se sobraram elementos abertos, também está errado
            is_valido = False
        if is_valido:
            if not test:
                print("S")
            else:
                r.append("S")
        else:
            if not test:
                print("N")
            else:
                r.append("N")

    if test:
        return r

if __name__ == '__main__':
    main()