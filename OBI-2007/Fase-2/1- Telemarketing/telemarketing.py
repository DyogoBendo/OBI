import heapq

def main(entrada=input, test=False):
    n, l = map(int, entrada().split())
    time = []   # time for each call
    k = 5
    w = [[0, i, 0] for i in range(n)] # workers
    result = [0 for _ in range(n)]
    heapq.heapify(w)        
    for _ in range(l):
        t = int(entrada())        
        item = w[0]
        item[0] += t
        item[2] += 1        
        result[item[1]] += 1
        heapq.heapreplace(w, item)    

    if not test:
        for i in range(n):
            print(i + 1, result[i])
    else:
        r = []
        for i in range(n):
            linha = str(i + 1) + " " + str(result[i])
            r.append(linha)            
        return r        

if __name__ == '__main__':
    main()
