from math import inf
import heapq
REMOVED = '<removed-task>'

def get_top():  # método para pegar primeiro valor válido do heap
    global heap, entry_finder
    while heap:
        top_dist, _, top_position = heapq.heappop(heap)
        if top_position is not REMOVED:  # removemos agora valores que ja foram virtualmente removidos
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
    # adicionamos a posição inicial do robo como um "retangulo de uma dimensão" - um ponto

    x1.append(xf)
    x2.append(xf)
    y1.append(yf)
    y2.append(yf)
    # e fazemos o mesmo para a posição final

    n += 2        

    cost = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):            
            dx = max(0, max(x1[i], x1[j]) - min(x2[i], x2[j]))  
            dy = max(0, max(y1[i], y1[j]) - min(y2[i], y2[j]))            
            cost[i][j] = dx + dy
            # calculamos a distância entre dois retângulos cadastrados, fazemos esse cálculo para todos os pares que existem
    dist = [inf for _ in range(n)]  # armazena a distância em relação ao ponto inicial
    marc  = [0 for _ in range(n)]  # guarda os valores que já foram considerados -> 0 não foi e 1 foi
    entry_finder = {}

    dist[n - 2] = 0  # n-2 é onde está a posição inicial
    entry = [dist[n-2], n-2, n-2]
    heapq.heappush(heap, entry)  # criamos um heap que inicia apenas com o valor inicial, esse heap é um heap de valor minimo de distancia em relação ao ponto inicial
    entry_finder[n-2] = entry
    while entry_finder:  # iteramos enquanto houver elemento a ser visitado
        top_position, top_dist = get_top()                        
        marc[top_position] = 1  # indicamos que a posição já foi considerada
        for i in range(n):  # agora comparamos essa posição com todas as outras...
            if marc[i]:  #... que ainda não foram consideradas
                continue
            ndist = top_dist + cost[top_position][i]  # a distância desse retangulo considerado em relação ao ponto inicial é a distância desse retangulo com o retangulo minimo somado com a distancia do retangulo minimo em relação ao ponto inicial
            if ndist < dist[i]:  # se essa distância for menor que estava sendo considerada
                if i in entry_finder:  # caso já tivessemos adicionado ao heap, precisamos desconsiderar aquela entrada anterior 
                    old_entry = entry_finder.pop(i)
                    old_entry[-1] = REMOVED 
                                
                dist[i] = ndist
                entry = [dist[i], i, i]
                entry_finder[i] = entry                
                heapq.heappush(heap, entry)  # adicionamos um novo retângulo no heap de retângulos mínimos
    c = dist[n-1]  # é a distância da posição final em relação à posição inicial

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()