from math import inf
from heapq import *

REMOVED = '<removed-vertice>'

def extract_min():
    while min_queue:
        distancia, _, vertice = heappop(min_queue)
        if vertice is not REMOVED:
            del entry_finder[vertice]
            return  vertice

if __name__ == '__main__':
    n, m = map(int, input().split())
    arestas = [[] for _ in range(n + 2)]
    dist = [ inf for _ in range(n + 2) ]
    dist[0] = 0
    for i in range(m):
        try:
            s, t, b = map(int, input().split())
        except:
            break
        arestas[s].append((t, b))
        arestas[t].append((s, b))

    entry_finder = {}
    min_queue = []
    for i in range(1, n + 2):
        entry = [inf, i, i]
        min_queue.append(entry)
        entry_finder[i] = entry
    
    heappush(min_queue, [0, 0, 0])
    entry_finder[0] = [0, 0, 0]
    
    while entry_finder:
        u = extract_min()
        for v, w in arestas[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
                old_entry = entry_finder.pop(v)
                old_entry[-1] =  REMOVED

                entry = [dist[v], v, v]
                entry_finder[v] = entry
                heappush(min_queue, entry)                
    
    print(dist[n+1])