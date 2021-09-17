def main(entrada=input, test=False):
    frase = entrada().split()
    c = ""
    for e in frase:
        c += " " + e[1::2]  # pegamos cada elemento pulando 2, já que existe um p antes de cada caracter

    if not test:
        print(c[1:])  # pegamos a partir da posição 1 apenas pra ignorar o espaço da palavra inicial
    else:
        return [c[1:]]

if __name__ == '__main__':
    main()