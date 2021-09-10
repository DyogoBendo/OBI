def main(entrada=input, test=False):
    n, s = map(int, entrada().split())
    quadrado = []
    m = 0  # variavel que define o valor que será inserido no quadrado: começamos com 0
    soma_atual = 0    

    for i in range(n):
        linha = []        
        for j in range(n):
            if i == j:
                soma_atual += m  # mantemos armazenado qual valor da soma está sendo gerado olhando a diagonal principal
            linha.append(m)
            m += 1  # a variavel aumenta de um em um
        quadrado.append(linha)    

    k = soma_atual - s  # vemos quão longe passamos da soma que foi requisitada pelo usuário
    if k != 0:  # caso não tenha sido igual
        if k > 0:  # se o valor que temos é maior do que se procura
            j = 0   # modificamos a primeira linha
        elif k < 0:  # se for menor do que se procura
            j = -1  # modificamos a última linha

        for i in range(n):
            quadrado[j][i] -= k  # se o valor for positivo, subtraimos, se for negativo somamos
    
    if not test:        
        for i in range(n):            
          print(" ".join(list(map(str, quadrado[i]))))
    else:
        return quadrado

if __name__ == '__main__':
    main()