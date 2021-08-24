def main(entrada=input, test=False):
    n = int(entrada())

    soma_linhas = [0 for _ in range(n)]
    soma_colunas = [0 for _ in range(n)]
    diagonal_principal = 0
    valores_usados = set()

    is_magico = True
    for i in range(n):
        linha = list(map(int, entrada().split()))
        for j in range(n):
            valor = linha[j]
            valores_usados.add(valor)

            if valor > n ** 2:
                is_magico = False

            soma_linhas[i] += valor
            soma_colunas[j] += valor
            if i == j:
                diagonal_principal += valor
    soma_linhas = set(soma_linhas)
    soma_colunas = set(soma_colunas)

    if len(soma_linhas) > 1 or len(soma_colunas) > 1 or len(valores_usados) < n**2:
        is_magico = False    

    else:
        coluna = soma_colunas.pop()
        linha = soma_linhas.pop()        
        if not (coluna == linha == diagonal_principal):
            is_magico = False

    if not test:
        if is_magico:
            print(diagonal_principal)
        else:
            print(0)
    else:
        if is_magico:
            return[diagonal_principal]
        else:
            return[0]        

if __name__ == '__main__':
    main()