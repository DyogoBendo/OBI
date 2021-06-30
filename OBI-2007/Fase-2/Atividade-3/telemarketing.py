import heapq

if __name__ == '__main__':
    n, l = map(int, input().split())
    time = []   # time for each call
    k = 5
    w = [[0, i, 0] for i in range(n)] # workers
    result = [0 for _ in range(n)]
    heapq.heapify(w)        
    for _ in range(l):
        t = int(input())        
        item = w[0]
        item[0] += t
        item[2] += 1        
        result[item[1]] += 1
        heapq.heapreplace(w, item)    
    for i in range(n):
        print(i + 1, result[i])

    