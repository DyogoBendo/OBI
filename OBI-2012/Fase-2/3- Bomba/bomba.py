from math import inf, isinf 
from queue import Queue  # utilizamos uma fila

def main(entrada=input, test=False):    
    n, e, s, m = map(int, entrada().split())
    arestas = [[] for _ in range(n)]
    for i in range(m):
        a, b, t = map(int, entrada().split())
        arestas[a].append((b, t))  # inserimos cada uma das arestas     

    grafo = [[[inf for _ in range(3)] for _ in range(n)] for _ in range(n)] # criamos o grafo tridimensional

    fila = Queue()
    fila.put((e, 0))  # iniciamos a fila com inicio na entrada e com profundidade 0

    while not fila.empty():  # enquanto houverem vértices que pudermos visitar
        rotatoria_atual, profundidade = fila.get(block=False)  # pegamos o elemento que foi por primeiro inserido
        momento = profundidade % 3  # o momento para se passar no semáforo é ou não um múltiplo de 3 
        for prox_rotatoria, semaforo in arestas[rotatoria_atual]:   # verificamos cada uma das rotatarias que podem ser alcançadas pela a que estamos verificando atualmente
            if semaforo == 1:  # se o semaforo da rua que liga as duas abre apenas com múltiplos de 3
                if momento == 0:
                    if isinf(grafo[rotatoria_atual][prox_rotatoria][momento]):  # verificamos se já consideramos essa rotatória
                        grafo[rotatoria_atual][prox_rotatoria][momento] = profundidade + 1  # se não, então adicionamos a profundidade atual
                        fila.put((prox_rotatoria, profundidade + 1))  # e adicionamos para verificar essa próxima rotatória, na sua profundidade
            else:  # fazemos a mesma coisa se o semáforo abre fora dos múltiplos de 3
                if momento != 0:                
                        if isinf(grafo[rotatoria_atual][prox_rotatoria][momento]):
                                grafo[rotatoria_atual][prox_rotatoria][momento] = profundidade + 1
                                fila.put((prox_rotatoria, profundidade + 1))        

    # agora verificamos todos que chegam na saída, em todos os momentos diferentes, e dentre desses, qual tem o menor valor. 
    menor = inf
    for i in range(n):
        for j in range(3):
            menor = min(menor, grafo[i][s][j])
    c = "*" if isinf(menor) else menor  # caso não tenha nenhuma forma de chegar na saída, o valor será infinito
    
    if not test:
        print(c)
    else:
        return [c]    

if __name__ == '__main__':
    main()