def main(entrada=input, test=False):
    l, n = map(int, entrada().split())
    c = (n - 1) + (l - n + 1) ** 2    
    # a melhor soma é sempre a que possuí o maior tapete, nesse caso todos os outros tapetes tem tamanho 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()