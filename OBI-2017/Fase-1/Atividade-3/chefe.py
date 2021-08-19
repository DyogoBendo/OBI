from math import inf, isinf

def main(file_input=input, test=False):
    n, m, i = map(int, file_input().split())
    empregados = [[0, [], []] for _ in range(n)]
    idades = list(map(int, file_input().split()))
    posicoes = [k for k in range(n)]
    for k in range(n):
        empregados[k][0] = idades[k]
    for k in range(m):
        x, y = map(int, file_input().split())
        x -= 1
        y -= 1
        empregados[x][2].append(y)  # gerencia y
        empregados[y][1].append(x)  # é gerenciado por x
    for k in range(i):
        entrada = file_input().split()
        if len(entrada) == 2:
            e = int(entrada[1]) - 1
            e = posicoes[e]
            mais_jovem = inf                     
            chefes = [c for c in empregados[e][1]]                                     
            empregados_contados = set()            
            while chefes:
                c= chefes.pop()                              
                if empregados[c][0] < mais_jovem:
                    mais_jovem = empregados[c][0]
                empregados_contados.add(c)
                chefes += empregados[c][1]            
            c = "*" if isinf(mais_jovem) else mais_jovem
            if not test:
                print(c)                
            else:
                return [c]
        else:
            a, b = map(int, entrada[1:])
            a -= 1
            b -= 1            
            posicoes[a], posicoes[b] = posicoes[b], posicoes[a]
            empregados[posicoes[a]][0], empregados[posicoes[b]][0] = empregados[posicoes[b]][0], empregados[posicoes[a]][0]

if __name__ == '__main__':
    main()