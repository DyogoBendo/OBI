from bisect import bisect_left

def calc(p, q):   
    return bisect_left(arestas[p], q + 1)        

def dfs(p, a):
    print(p, a)
    global vis, arestas    
    if a == len(vis[p]):         
        return 0

    res = vis[p][a]
    if res:         
        return res
    
    res = max(dfs(arestas[p][a], calc(arestas[p][a], p)) + 1, dfs(p, a + 1))    

    vis[p][a] = res
    return res

def main(entrada=input, test=False):
    global vis, arestas

    n, m = map(int, entrada().split())
    arestas = [[] for _ in range(n + 1)]
    vis = [[] for _ in range(n + 1)]    

    for i in range(m):
        a, b = map(int, entrada().split())
        arestas[a].append(b)
        arestas[b].append(a)

        vis[a].append(0)  # valor de distâncoa máxima
        vis[b].append(0)
    
    for i in range(1, n + 1):
        arestas[i].sort()  # ordenamos as arestas de de cada vértice         
        
    c = ""
    for i in range(1, n + 1):        
        if i > 1:
            c += " "
        c += str(1 + dfs(i, 0))        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()