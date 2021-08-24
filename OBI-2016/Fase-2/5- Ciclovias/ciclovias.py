def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    arestas = [[] for _ in range(n + 1)]
    distancias = [1 for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, entrada().split())
        arestas[a].append(b)
        arestas[b].append(a)
    for i in range(n, -1, -1):
        for a in arestas[i]:
            distancias[i] = max(distancias[a] + 1, distancias[i])
    c = ""
    for i in range(n + 1):
        c += str(distancias[i]) + " "
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()