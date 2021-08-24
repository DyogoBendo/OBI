def main(entrada=input, test=False):
    n, s = map(int, entrada().split())
    quadrado = []
    m = 0
    soma_atual = 0
    repete = set()

    for i in range(n - 1):
        linha = []        
        for j in range(n):
            m += 1
            k = (s // n) + 1  + (m * 10)
            repete.add(k)
            if i == j:
                soma_atual += k
            linha.append(k)
        quadrado.append(linha)
    linha_faltante = []

    valor_final = s - soma_atual    
    linha_faltante.append(valor_final)
    for i in range(1, n):
        k = valor_final - (i * 10)
        repete.add(k)
        linha_faltante.insert(0, k)
    quadrado.append(linha_faltante)    

    if not test:        
        for i in range(n):            
          print(" ".join(list(map(str, quadrado[i]))))
    else:
        return quadrado

if __name__ == '__main__':
    main()