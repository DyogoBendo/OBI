def main(entrada=input, test=False):
    n, m = map(int, entrada().split())

    c = 0
    # caso m seja maior que n, não há nenhuma restrição, então todos os casos são possíveis
    if m >= n:
        for i in range(n):
            c += i  # o número de possibilidades para um valor i é n - i
    else:        
        piso = n - 2 * m  # é o valor mínimo que um número pode assumir para ainda ser possível formar um conjunto válido

        if piso > 0:  # se existir um piso
            k = m + 1 - piso  # faixa de valores que temos escolhas válidas
            for i in range(k + 1):            
                c += i  # mesma ideia do número de possibilidades
        else:  # se podemos considerar o 0
            inicial = 2*(m - (n // 2) + 1)  
            for i in range(1, n - m):  # pegamos os m primeiro elementos, em que a nossa soma é limitada
                c += inicial
                inicial += 1                
            for i in range(n -m, m + 1):
                c += n - i - 1  # aqui utilizamos explicitamente a lógica de somar a diferença de n por i, que é onde não temos restrição na soma

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()