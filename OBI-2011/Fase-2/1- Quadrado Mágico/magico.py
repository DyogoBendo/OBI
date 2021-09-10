def main(entrada=input, test=False):
    n = int(entrada())

    soma_linhas = [0 for _ in range(n)]  # mantemos as somas de todas as linahs
    soma_colunas = [0 for _ in range(n)] # colunas
    diagonal_principal = 0  # e da diagonal principal
    valores_usados = set()  # além dos valores usados, para que não ocorra repetição

    is_magico = True
    for i in range(n):
        linha = list(map(int, entrada().split()))
        for j in range(n):
            valor = linha[j]
            valores_usados.add(valor)

            if valor > n ** 2:  # caso o valor seja maior que n ^ 2 ele não é mágico
                is_magico = False

            soma_linhas[i] += valor  # somamos à linha
            soma_colunas[j] += valor  # e à coluna
            if i == j:
                diagonal_principal += valor  # além da diagonal principal
    soma_linhas = set(soma_linhas)
    soma_colunas = set(soma_colunas)

    if len(soma_linhas) > 1 or len(soma_colunas) > 1 or len(valores_usados) < n**2:  # verificamos se existe mais de uma soma nas linhas, colunas e se foram usados exatamente n ^ 2 valores, ou seja, nenhum valor repetido
        is_magico = False    

    else:
        coluna = soma_colunas.pop()
        linha = soma_linhas.pop()        
        if not (coluna == linha == diagonal_principal):  # agora verificamos se a soma das colunas, linhas e da diagonal principal não é a mesma
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