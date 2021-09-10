from heapq import *

def main(entrada=input, test=False):    
    n, m = map(int, entrada().split())

    num_dependencias = [0 for _ in range(n)]
    dependentes = [[] for _ in range(n)]

    queue = []

    for i in range(m):
        a, b = map(int, entrada().split())
        num_dependencias[b] += 1  # armazenamos de quantos b depende para ser executado
        dependentes[a].append(b)  # adicionamos b aos que dependem de a

    for i in range(n):
        if num_dependencias[i] == 0:
            heappush(queue, i)  # adicionamos a fila de prioridade todos que não dependem de ninguém inicialmente

    c = []
    while queue:
        a = heappop(queue)  # retiramos o elemento de maior prioridade
        c.append(a)  # adicionamos na lista para ser impresso
        d = dependentes[a]  # pegamos todos que dependem de a
        for k in d:
            num_dependencias[k] -= 1  # agora cada um deles depende de 1 a menos que antes
            if num_dependencias[k] == 0:  # se dependiam apenas de a, então agora estão livres para serem realizados
                heappush(queue, k)  # e são adicionados a fila de prioridade
    if not test:
        if len(c) == n:  # caso todos possam ser resolvidos
            for tarefa in c:
                print(tarefa)
        else:
            print("*")
    else:
        if len(c) == n:
            return c
        else:
            return ["*"]

if __name__ == '__main__':
    main()