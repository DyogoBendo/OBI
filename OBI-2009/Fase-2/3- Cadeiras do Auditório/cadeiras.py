def main(entrada=input, test=False):    
    l, c = map(int, entrada().split())
    auditorio = []
    for _ in range(l):
        cadeiras = list(map(int, entrada().split()))
        auditorio.append(cadeiras)
    
    movements = []    
    for i in range(l):
        for j in range(c):
            expected_value = (i) * c + j + 1
            actual_value = auditorio[i][j]
            if actual_value != expected_value:                
                # analisamos 3 casos
                # caso 1: mesma linha mas coluna errada
                coluna_correta = actual_value - (c * i ) - 1
                linha_correta = (actual_value - j - 1) / c
                if 0 < coluna_correta < c:                    
                    movements.append(["C", j + 1, coluna_correta + 1])                    
                    for k in range(l):
                        auditorio[k][j], auditorio[k][coluna_correta] = auditorio[k][coluna_correta], auditorio[k][j]
                # caso 2: coluna certa linha errada
                elif linha_correta < l and int(linha_correta) == linha_correta:
                    linha_correta = int(linha_correta)
                    movements.append(["L", i + 1, linha_correta + 1])                    
                    auditorio[i], auditorio[linha_correta] = auditorio[linha_correta], auditorio[i]
                # caso 3: tudo errado                
                else:
                    linha = int(linha_correta)
                    coluna = round((linha_correta - linha) * c)

                    movements.append(["L", i + 1, linha + 1])
                    movements.append(["C", j + 1, coluna + 1])   

                    auditorio[i], auditorio[linha] = auditorio[linha], auditorio[i]                    
                    for k in range(l):
                        auditorio[k][j], auditorio[k][coluna] = auditorio[k][coluna], auditorio[k][j]
    r = []
    k = len(movements)
    if not test:
        print(len(movements))
        for a, b, c in movements:
            print(a, b, c)
        print(c)
    else:
        r.append(k)
        for a, b, c in movements:
            r.append(f'{a} {b} {c}')
        return r

if __name__ == '__main__':
    main()
    