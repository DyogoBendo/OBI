from typing import List
import time


MAXR = 50
MAXN = 100000

ROW = 0
COL = 1

def add(idx: int, r: int, pos: int, valor: int):
    i = pos  # iniciamos da posiçãp
    while i < MAXN:  # e vamos até o limite de tamanho        
        bit[i][r][idx] += valor  # somamos o valor passado para a posição (aumentar em 1 a frequência ou diminuir)
        i += i & -i # e vamos a aproximadamente de 2^i passos, ou seja, o tempo é log n

def get(idx: int, r: int, pos: int):
    soma = 0
    i = pos
    while i > 0:  # quantos valores entre a posição e o idx
        soma += bit[i][r][idx]  # somamos a frequência
        i -= i & -i  # voltamos de forma "exponencial"

    return soma

def get_best(last_v: List[int], time_now: int, IS_COL: int):
    soma = 0
    best_count = -1
    best_save = -1
    last_r = last_v[0]
    last_idx = last_v[1]
    for r in range(51):  # verificamos cada um dos valores
        if r == last_r:  # se o valor for igual ao último, então pulamos
            continue
        cur = get(IS_COL, r, time_now) - get(IS_COL, r, last_idx)  # pegamos a frquência entre o momento agora e o da última mudança na linha/coluna
        soma += cur  # somamos
        if cur >= best_count:  # se a conta atual for melhor que a melhor
            best_count = cur  # então ela se a torna a melhor
            best_save = r  # e esse é o valor de maior frequência

    if n - soma > best_count:  # se a soma o número de elementos menos a soma for maior que a melhor contagem, então pegamos o último valor atribuído a essa linha/coluna
        best_save = last_r
    elif n - soma  == best_count:  # se for exatamente igual
        best_save = max(best_save, last_r)  # pegamos o que possuí maior valor
    return best_save  # então retornamos o melhor valor, o mais frequente


def main(entrada=input, test=False):
    global bit, n    
    
    a = time.time()
    bit = [[[0 for _ in range(3)] for _ in range(MAXR + 2)] for _ in range(MAXN + 2)]  # declaramos um vetor de três dimensões    
    print(time.time() - a)
    last_row = [[0, 0] for _ in range(MAXN + 1)]  # última linha
    last_col = [[0, 0] for _ in range(MAXN + 1)]  # última coluna
    # ambos são vetores de pares

    n, q = map(int, entrada().split())      

    if test:
        c = []

    for t in range(q):        
        e = tuple(map(int, entrada().split()))

        if len(e) == 3:  # se a entrada tem 3 valores
            opr, x, r = e
            if opr == 1:  # se for a operação de definir os valores de uma linha
                if last_row[x][1]:  # caso a linha x já tiver algum valor atribuído
                    add(idx=COL, r=last_row[x][0], pos=last_row[x][1], valor = -1)  # adiminuímos a frequência de todas as colunas em relação ao valor da última linha
                add(idx = COL, r=r, pos=t, valor=1)
                last_row[x] = [r, t]  # atruibimos isso ao ultimo valor que foi colocado nessa linha: o valor e quando
            else:
                if last_col[x][1]:  # caso a columa já tenha um valor atribuído
                    add(idx=ROW, r=last_col[x][0], pos=last_col[x][1], valor=-1)  # então diminuímos a frquência de todas as linhas em relação ao valor da última coluna
                add(idx=ROW, r=r, pos=t, valor=1)  # adicionamos a frequência desse valor a todas as linhas
                last_col[x] = [r, t]
        else:
            opr, x = e
            if opr == 3:                
                if test:
                    c.append(get_best(last_row[x], t, ROW))           
                else:
                    print(get_best(last_row[x], t, ROW))  # pegamos a maior frequência da linha
            else:
                if test:
                    c.append(get_best(last_col[x], t, COL))  # e a maior frequência da coluna
                else:
                    print(get_best(last_col[x], t, COL))
    if test:
        return c

if __name__ == '__main__':
    main()