from math import inf

if __name__ == '__main__':
    n, m = map(int, input().split())
    vertices = []
    dist = [ inf for _ in range(n + 2) ]
    dist[0] = 0
    for i in range(m):
        try:
            s, t, b = map(int, input().split())
        except:
            break
        vertices.append((s, t, b))        
        vertices.append((t, s, b))    
    for _ in range(n + 1):
        for v, u, b in vertices:
            if dist[u] > dist[v] + b:
                dist[u] = dist[v] + b
    print(dist[n+1])
