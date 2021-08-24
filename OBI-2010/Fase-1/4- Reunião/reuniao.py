from math import inf

def main(entrada=input, test=False):            
    c, a = map(int, entrada().split())
    caminhoneiros = [[inf for _ in range(c)] for _ in range(c)]
    for i in range(a):
        u, v, w = map(int, entrada().split())
        caminhoneiros[u][v] = w
        caminhoneiros[v][u] = w        
    for k in range(c):
        for i in range(c):
            for j in range(c):      
                if i != j: 
                    caminhoneiros[i][j] = min(caminhoneiros[i][j], (caminhoneiros[i][k] + caminhoneiros[k][j]))                                 
    menor_maior = inf           
    for i in range(c):        
        maior = 0
        for j in range(c):                                  
            if caminhoneiros[i][j] > maior and i != j:
                maior = caminhoneiros[i][j]        
        if maior < menor_maior:
            menor_maior = maior        
    if not test:
        print(menor_maior)
    else:
        return [menor_maior]

if __name__ == '__main__':    
    main()