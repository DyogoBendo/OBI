from heapq import *
from collections import deque  # constant time on removing first element


def main(file_input=input, test=False):
    c, n = map(int, file_input().split())
    num_pessoas_esperou_20min = 0

    fila_pessoas = deque()
    fila_caixas = []

    for i in range(n):
        t, d = map(int, file_input().split())        
        fila_pessoas.append((t, i, d))
    for i in range(c):
        heappush(fila_caixas, (0, i))

    while fila_pessoas:
        t, i, d = fila_pessoas.popleft()
        atendimento, j = heappop(fila_caixas)        

        inicio_atendimento = t if atendimento - t < 0 else atendimento

        if atendimento - t > 20:
            num_pessoas_esperou_20min += 1
        
        heappush(fila_caixas, (inicio_atendimento + d, j))
         

    if not test:
        print(num_pessoas_esperou_20min)
    else:
        return [num_pessoas_esperou_20min]

if __name__ == '__main__':
    main()