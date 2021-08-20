from math import inf
from queue import Queue
global N, M, tab, dist, fila, DIRECTIONS

class Vertex():
    def __init__(self, l, c, t) -> None:
        self.l = l
        self.c = c
        self.t = t

def wipe(v):
    v = [inf for _ in range(len(v))]
    print(v)

def bfs():
    global fila, dist, tab         
    fila = Queue(maxsize=0)
    fila.put(Vertex(0, 0, 0))
    dist[0][0][0] = 0
    
    while (not fila.empty()):
        v = fila.get()
        for d in range(5):
            nl = v.l + DIRECTIONS[d][0]
            nc = v.c + DIRECTIONS[d][1]
            nt = (v.t + 1) % 10
            
            if nl < 0 or N <= nl or nc < 0 or M <= nc:
                continue
            if (tab[nl][nc] + v.t) % 10 - 1 >  (tab[v.l][v.c] + v.t) % 10:
                continue
            if dist[nl][nc][nt] < inf:
                continue
            dist[nl][nc][nt] = dist[v.l][v.c][v.t] + 1
            fila.put(Vertex(nl, nc, nt))

if __name__ == "__main__":        
    DIRECTIONS = [[0,0], [1, 0], [0, 1], [-1, 0], [0, -1]]  # direções
    
    N, M = map(int, input().split())
    
    tab = [[0 for _ in range(M)] for _ in range(N)]
    dist = [[[inf for _ in range(10)]for _ in range(M) ]for _ in range(N)]
    
    for i in range(N):
        tab[i] = list(map(int, input().split()))
    
    bfs()        
    ans = inf
    
    for i in range(10):
        ans = min(ans, dist[N-1][M-1][i])
    
    print(ans)
    
    
    