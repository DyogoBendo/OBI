from heapq import *
from collections import deque  # constant time on removing first element


def main(entrada=input, test=False):
    c, n = map(int, entrada().split())
    num_pessoas_esperou_20min = 0 

    fila_pessoas = deque()  # fila de pessoas
    fila_caixas = []  # caixas que estão "esperando" para atender

    for i in range(n):
        t, d = map(int, entrada().split())        
        fila_pessoas.append((t, i, d))  # adicionamos cada pessoa e o momento que elas chegaram
    for i in range(c):
        heappush(fila_caixas, (0, i))  # adicionamos agora cada caixa, com a prioridade sendo o tempo delas

    while fila_pessoas:  # enquanto houverem pessoas
        t, i, d = fila_pessoas.popleft()  # removemos a primeira pessoa da fila
        atendimento, j = heappop(fila_caixas)  # caixa que irá atender é o de menor tempo        

        inicio_atendimento = t if atendimento - t < 0 else atendimento  
        # caso o caixa está a disposição antes da pessoa ter chegado na fila, então o atendimento inicia quando a pessoa chega
        # senão, inicia quando o caixa estiver disponível

        if atendimento - t > 20:  # caso a pessoa esperou mais de 20 minitos
            num_pessoas_esperou_20min += 1
        
        heappush(fila_caixas, (inicio_atendimento + d, j))  # o caixa agora está com o tempo em que termina o atendimento: o momento que iniciou mais o tempo que demora o atendimento
         

    if not test:
        print(num_pessoas_esperou_20min)
    else:
        return [num_pessoas_esperou_20min]

if __name__ == '__main__':
    main()