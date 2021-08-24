def main(entrada=input, test=False):
    n = int(entrada())    
    direito = [0 for _ in range(61)]
    esquerdo = [0 for _ in range(61)]

    for i in range(n):
        numero, pe = entrada().split()
        numero = int(numero)
        if pe == "D":
            direito[numero] += 1
        if pe == "E":
            esquerdo[numero] += 1
    c = 0

    for i in range(61):
        c += min(direito[i], esquerdo[i])
        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()