def main(entrada=input, test=False):
    ia, ib, fa, fb = map(int, entrada().split())    
    c = 0
    if ib != fb:  # se b está diferente da sua configuração desejada
        c += 1  # somos obrigados a realizar uma ação
        if ia == fa:  # como a ação é de inversão, então caso o estado desejado de a era igual ao inicial, precisamos realizar mais uma ação
            c += 1
    else:
        if ia != fa:  # se a for diferente do que queríamos
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()