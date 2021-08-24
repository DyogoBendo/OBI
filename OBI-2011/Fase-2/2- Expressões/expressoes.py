def main(entrada=input, test=False):
    n = int(entrada())
    r = []
    for i in range(n):
        pilha = []
        a = list(entrada().strip())
        is_valido = True

        for c in a:
            if c == "{":
                pilha.append("}")
            elif c == "[":
                pilha.append("]")
            elif c == "(":
                pilha.append(")")
            else:
                try:
                    esperado = pilha.pop()
                    if esperado != c:
                        is_valido = False
                except IndexError:
                    is_valido = False
        if len(pilha) > 0:
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