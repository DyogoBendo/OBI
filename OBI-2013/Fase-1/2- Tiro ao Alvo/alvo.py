from math import sqrt
from sys import stdin

def search(circulos, i, j, distancia):    
    # utilizamos uma busca binária para encontrar a posição do círculo
    if i > j: 
        return False  # caímos nessa caso quando o valor não é uma borda
    m = int((i + j) / 2)  # pegamos na posição intermediária
    if circulos[m][0] < distancia:  # se o valor que temos atualmente é maior do que na posição intermediária
        is_borda = search(circulos, m + 1, j, distancia)  # verificamos se é uma borda, olhando os elementos maiores
        if is_borda:  # se for uma borda
            return is_borda  # retornamos
        else:
                if i == j == len(circulos) - 1:   # se a distância é maior que o valor do círculos na última posição, então não pontuamos
                    return (0, 0)
                else:
                    return circulos[m + 1]  # senão, retornamos a primeira borda maior que a distância

    elif circulos[m][0] > distancia:  # se a distância for menor que a posição do círculo que estamos verificando
        is_borda = search(circulos, i, m - 1, distancia)  
        if is_borda:  # testamos se é uma borda, olhando os elementos menores
            return is_borda
        else:
            return circulos[m]  # se não for uma borda, significa que está contido pela borda atual e a retornamos. 
    else:  # caimos nesse caso quando se é uma borda
        return circulos[m]
    


def main(entrada=stdin.readline, test=False):
    c, t = map(int, entrada().split())    

    circulos = []
    k = 0

    for i in range(c):
        ci = int(entrada())
        circulos.append((ci, c-i))  # armazenamos a distancia em relação ao centro do circulo, e também o número de círculos que contém esse círculo, pois esse é o valor da pontuação de um círculo

    for i in range(t):
        x, y = map(int, entrada().split())

        d = sqrt((x ** 2) + (y ** 2))  # calculamos a distância de onde o dardo acertou em relação ao ponto central

        p = search(circulos, 0, len(circulos) - 1, d)[1]  # dada essa distância procuramos em que círculo ele se encaixa
        k += p  # somams a pontuação que vale o círculo que foi acertado

    if not test:
        print(k)
    else:
        return [k]

if __name__ == '__main__':
    main()