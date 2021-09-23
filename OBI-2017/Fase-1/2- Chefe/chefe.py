from math import inf, isinf

def main(entrada=input, test=False):
    n, m, i = map(int, entrada().split())
    empregados = [[0, [], []] for _ in range(n)]
    idades = list(map(int, entrada().split()))
    posicoes = [k for k in range(n)]
    res = []
    for k in range(n):
        empregados[k][0] = idades[k]
    for k in range(m):
        x, y = map(int, entrada().split())
        x -= 1
        y -= 1
        empregados[x][2].append(y)  # gerencia y
        empregados[y][1].append(x)  # é gerenciado por x
    for k in range(i):
        e = entrada().split()
        if len(e) == 2:  # se for uma instrução de pergunta
            e = int(e[1]) - 1  # pegamos o empregado que se referencia  
            e = posicoes[e]  # pegamos que posição que e se refere
            mais_jovem = inf  # inicializamos o chefe mais jovem como infinito                      
            chefes = [c for c in empregados[e][1]]  # pegamos todos os chefes do empregado
            empregados_contados = set()  # mantemos quais empregados já contamos na busca do chefe mais jovem            
            while chefes:  # enquanto existirem chefes para serem verificados
                c= chefes.pop()  # pegamos o chefe                              
                if empregados[c][0] < mais_jovem:  # se ele for mais jovem do que o chefe mais jovem que temos
                    mais_jovem = empregados[c][0]  # ele se torna o novo chefe mais jovem
                empregados_contados.add(c)  # e agora ele está entre os empregados contados
                for e in empregados[c][1]:  # para cada chefe desse chefe
                    if e not in empregados_contados:  # que ainda não foi analisado
                        chefes.append(e)  # adicionamos para verificarmos
            c = "*" if isinf(mais_jovem) else mais_jovem  # se não tiver nenhum chefe, o mais jovem é infinito, senão é o que encontrarmos
            if not test:
                print(c)                
            else:
                res.append(c)                
        else:
            a, b = map(int, e[1:])
            a -= 1
            b -= 1            
            posicoes[a], posicoes[b] = posicoes[b], posicoes[a]  # trocamos a e b de posição
            empregados[posicoes[a]][0], empregados[posicoes[b]][0] = empregados[posicoes[b]][0], empregados[posicoes[a]][0]
            # trocamos as idades armazenadas em empregados na posição de a e na posição de b
            # assim, trocamos a posição que a e b referenciam, trocando quais são seus chefes e a posição hierarquica que eles ocupam
    return res

if __name__ == '__main__':
    main()