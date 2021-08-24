from math import inf
import heapq
REMOVED = '<removed-task>'

def get_top():
    global heap, entry_finder
    while heap:
        top_dist, _, top_position = heapq.heappop(heap)
        if top_position is not REMOVED:            
            del entry_finder[top_position]
            return (top_position, top_dist)    

def main(entrada=input, test=False):
    global heap, entry_finder
    x1, x2, y1, y2, heap = ([] for i in range(5))
    xi, yi, xf, yf = map(int, entrada().split())
    n = int(entrada())
    for i in range(n):
        a1, b1, a2, b2 = map(int, entrada().split())
        x1.append(a1)
        x2.append(a2)
        y1.append(b1)
        y2.append(b2)    

    x1.append(xi)
    x2.append(xi)

    y1.append(yi)
    y2.append(yi)

    x1.append(xf)
    x2.append(xf)

    y1.append(yf)
    y2.append(yf)
    n += 2        

    cost = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):            
            dx = max(0, max(x1[i], x1[j]) - min(x2[i], x2[j]))
            dy = max(0, max(y1[i], y1[j]) - min(y2[i], y2[j]))            
            cost[i][j] = dx + dy
    
    dist = [inf for _ in range(n)]
    marc  = [0 for _ in range(n)]
    entry_finder = {}

    dist[n - 2] = 0
    entry = [dist[n-2], n-2, n-2]
    heapq.heappush(heap, entry)
    entry_finder[n-2] = entry
    while entry_finder:                
        top_position, top_dist = get_top()                        
        marc[top_position] = 1
        for i in range(n):
            if marc[i]:
                continue
            ndist = top_dist + cost[top_position][i]
            if ndist < dist[i]:
                if i in entry_finder:
                    old_entry = entry_finder.pop(i)
                    old_entry[-1] = REMOVED 
                                
                dist[i] = ndist
                entry = [dist[i], i, i]
                entry_finder[i] = entry                
                heapq.heappush(heap, entry)                    
    c = dist[n-1]

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()