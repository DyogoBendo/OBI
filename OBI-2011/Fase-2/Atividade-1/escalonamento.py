from heapq import *

def main(file_input=input, test=False):    
    n, m = map(int, file_input().split())

    num_dependencias = [0 for _ in range(n)]
    dependentes = [[] for _ in range(n)]

    queue = []

    for i in range(m):
        a, b = map(int, file_input().split())
        num_dependencias[b] += 1
        dependentes[a].append(b)

    for i in range(n):
        if num_dependencias[i] == 0:
            heappush(queue, i)

    c = []
    while queue:
        a = heappop(queue)        
        c.append(a)
        d = dependentes[a]
        for k in d:
            num_dependencias[k] -= 1
            if num_dependencias[k] == 0:
                heappush(queue, k)      
    if not test:
        if len(c) == n:
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