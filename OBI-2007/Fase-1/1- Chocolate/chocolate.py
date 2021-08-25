def main(entrada=input, test=False):
    n = int(entrada())
    a = list(map(int, entrada().split()))  # quantidade de partes que o chocolate é dividido
    resultado = 0  # número de partes que serão guardadas
    
    for i in a:
        resultado += (i - 1)    

    if not test:
        print(resultado)
    else:
        return [resultado]

if __name__ == '__main__':
    main()