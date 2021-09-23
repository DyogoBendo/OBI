def main(entrada=input, test=False):
    n = int(entrada())    
    direito = [0 for _ in range(61)]
    esquerdo = [0 for _ in range(61)]

    for i in range(n):
        numero, pe = entrada().split()
        numero = int(numero)
        if pe == "D":
            direito[numero] += 1  # número de botas no pé direito daquele tamanho
        if pe == "E":
            esquerdo[numero] += 1  # número de botas no pé esquerdo daquele tamanho
    c = 0

    for i in range(61):
        c += min(direito[i], esquerdo[i])  # pegamos o menor número  de botas entre esquerdas e direita daquele tamanho, pois é a quantidade de pares que será possível formar.
        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()