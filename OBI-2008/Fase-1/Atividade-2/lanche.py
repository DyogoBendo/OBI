from math import inf

def floyd(g, size):

    for k in range(size):
        for i in range(size):
            for j in range(size):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    min_distance = inf
    for i in range(size):
        max_distance = 0        
        for j in range(size):
            max_distance = g[i][j] if g[i][j] > max_distance else max_distance
        if max_distance < min_distance:
            min_distance = max_distance

    print(min_distance)

if __name__ == '__main__':
    s, c = map(int, input().split())
    graph = [[inf if i != j else 0 for i in range(s)] for j in range(s)]
    for i in range(c):
        a, b, c = map(int, input().split())
        graph[a - 1][b - 1] = c
        graph[b - 1][a - 1] = c

    floyd(graph, s)
