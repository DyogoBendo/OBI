if __name__ == '__main__':
    linhas, colunas = map(int, input().split())
    pretas = int(input())

    tabuleiro = []
    conta_brancas = 0
    bloqueadores = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        tabuleiro.append(linha)

    for i in range(pretas):
        linha, coluna = map(int, input().split())
        linha -= 1
        coluna -= 1

        tabuleiro[linha][coluna] = 1

    for i in range(linhas):
        for j in range(colunas):
            if tabuleiro[i][j] == 1:
                if i < linhas - 1:
                    teste1, teste2, teste3, teste4 = False, False, False, False
                    if tabuleiro[i + 1][j] == 0:
                        linha_branco = i + 1
                        coluna_branco = j
                        if tabuleiro[linha_branco][coluna_branco] != 2:
                            if coluna_branco < colunas - 1:
                                if tabuleiro[linha_branco][coluna_branco + 1] != 2:
                                    teste1 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco + 1])
                            else:
                                teste1 = True
                            if coluna_branco > 0:
                                if tabuleiro[linha_branco][coluna_branco - 1] != 2:
                                    teste2 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco - 1])
                            else:
                                teste2 = True
                            if linha_branco < linhas - 1:
                                if tabuleiro[linha_branco + 1][coluna_branco] != 2:
                                    teste3 = True
                                else:
                                    bloqueadores.append([linha_branco + 1, coluna_branco])
                            else:
                                teste3 = True
                            if linha_branco > 0:
                                if tabuleiro[linha_branco - 1][coluna_branco] != 2:
                                    teste4 = True
                                else:
                                    bloqueadores.append([linha_branco - 1, coluna_branco])
                            else:
                                teste4 = True
                            if teste1 and teste2 and teste3 and teste4:
                                tabuleiro[linha_branco][coluna_branco] = 2
                                conta_brancas += 1
                if i > 0:
                    teste1, teste2, teste3, teste4 = False, False, False, False
                    if tabuleiro[i - 1][j] == 0:
                        linha_branco = i - 1
                        coluna_branco = j
                        if tabuleiro[linha_branco][coluna_branco] != 2:
                            if coluna_branco < colunas - 1:
                                if tabuleiro[linha_branco][coluna_branco + 1] != 2:
                                    teste1 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco + 1])
                            else:
                                teste1 = True
                            if coluna_branco > 0:
                                if tabuleiro[linha_branco][coluna_branco - 1] != 2:
                                    teste2 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco - 1])
                            else:
                                teste2 = True
                            if linha_branco < linhas - 1:
                                if tabuleiro[linha_branco + 1][coluna_branco] != 2:
                                    teste3 = True
                                else:
                                    bloqueadores.append([linha_branco + 1, coluna_branco])
                            else:
                                teste3 = True
                            if linha_branco > 0:
                                if tabuleiro[linha_branco - 1][coluna_branco] != 2:
                                    teste4 = True
                                else:
                                    bloqueadores.append([linha_branco - 1, coluna_branco])
                            else:
                                teste4 = True
                            if teste1 and teste2 and teste3 and teste4:
                                tabuleiro[linha_branco][coluna_branco] = 2
                                conta_brancas += 1
                if j < colunas - 1:
                    teste1, teste2, teste3, teste4 = False, False, False, False
                    if tabuleiro[i][j + 1] == 0:
                        linha_branco = i
                        coluna_branco = j + 1

                        if tabuleiro[linha_branco][coluna_branco] != 2:
                            if coluna_branco < colunas - 1:
                                if tabuleiro[linha_branco][coluna_branco + 1] != 2:
                                    teste1 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco + 1])
                            else:
                                teste1 = True
                            if coluna_branco > 0:
                                if tabuleiro[linha_branco][coluna_branco - 1] != 2:
                                    teste2 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco - 1])
                            else:
                                teste2 = True
                            if linha_branco < linhas - 1:
                                if tabuleiro[linha_branco + 1][coluna_branco] != 2:
                                    teste3 = True
                                else:
                                    bloqueadores.append([linha_branco + 1, coluna_branco])
                            else:
                                teste3 = True
                            if linha_branco > 0:
                                if tabuleiro[linha_branco - 1][coluna_branco] != 2:
                                    teste4 = True
                                else:
                                    bloqueadores.append([linha_branco - 1, coluna_branco])
                            else:
                                teste4 = True
                            if teste1 and teste2 and teste3 and teste4:
                                tabuleiro[linha_branco][coluna_branco] = 2
                                conta_brancas += 1
                if j > 0:
                    teste1, teste2, teste3, teste4 = False, False, False, False
                    if tabuleiro[i][j - 1] == 0:
                        linha_branco = i
                        coluna_branco = j - 1

                        if tabuleiro[linha_branco][coluna_branco] != 2:
                            if coluna_branco < colunas - 1:
                                if tabuleiro[linha_branco][coluna_branco + 1] != 2:
                                    teste1 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco + 1])
                            else:
                                teste1 = True
                            if coluna_branco > 0:
                                if tabuleiro[linha_branco][coluna_branco - 1] != 2:
                                    teste2 = True
                                else:
                                    bloqueadores.append([linha_branco, coluna_branco - 1])
                            else:
                                teste2 = True
                            if linha_branco < linhas - 1:
                                if tabuleiro[linha_branco + 1][coluna_branco] != 2:
                                    teste3 = True
                                else:
                                    bloqueadores.append([linha_branco + 1, coluna_branco])
                            else:
                                teste3 = True
                            if linha_branco > 0:
                                if tabuleiro[linha_branco - 1][coluna_branco] != 2:
                                    teste4 = True
                                else:
                                    bloqueadores.append([linha_branco - 1, coluna_branco])
                            else:
                                teste4 = True
                            if teste1 and teste2 and teste3 and teste4:
                                tabuleiro[linha_branco][coluna_branco] = 2
                                conta_brancas += 1
                
    print(conta_brancas)
