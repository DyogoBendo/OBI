# algoritmo do Prim
from math import inf
from typing import SupportsRound

def min_key(key, mstSet):
    min_value = inf

    for k in range(len(key)):
        if key[k] < min_value and not mstSet[k]:
            min_value = key[k]
            min_index = k
    return (min_value, min_index)

def prim(n, graph):
    total_cost = 0
    mstSet = [False for _ in range(n)]
    key = [inf if i > 0 else 0 for i in range(n)]

    for cout in range(n):
        p, u = min_key(key, mstSet)
        total_cost += p
        mstSet[u] = True

        for v in range(n):
            if mstSet[v] is False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
    return total_cost

if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[inf for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        p, q, u = map(int, input().split())
        graph[p][q] = u
        graph[q][p] = u
    print(prim(n, graph))
    