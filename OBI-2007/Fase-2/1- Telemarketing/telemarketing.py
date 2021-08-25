import heapq

def main(entrada=input, test=False):
    n, l = map(int, entrada().split())    
    w = [[0, i] for i in range(n)] # criamos um heap de prioridade mínima dos trabalhadores
    result = [0 for _ in range(n)]    
    for _ in range(l):
        t = int(entrada())        
        item = w[0]  # pegamos o elemento de maior prioridade
        item[0] += t        
        result[item[1]] += 1  # adicionamos uma ligação ao vendedor
        heapq.heapreplace(w, item)  # retiramos e adicionamos de volta o vendedor, com o tempo adicional da ligação

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
