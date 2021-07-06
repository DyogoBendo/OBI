from math import inf

def bellman(g, size):
    max_distance = inf

    for i in range(size):
        dist = [inf for _ in range(size)]
        dist[i] = 0
        for _ in range(size):
            for j in range(size):
                for k in range(size):
                    if dist[j] + g[j][k] < dist[k]:
                        dist[k] = dist[j] + g[j][k]                
        dist.sort()
        b = dist[-1]

        if b < max_distance:
            max_distance = b

    print(max_distance)

if __name__ == '__main__':
    s, c = map(int, input().split())
    graph = [[inf if i != j else 0 for i in range(s)] for j in range(s)]
    for i in range(c):
        a, b, c = map(int, input().split())
        graph[a - 1][b - 1] = c
        graph[b - 1][a - 1] = c

    bellman(graph, s)
