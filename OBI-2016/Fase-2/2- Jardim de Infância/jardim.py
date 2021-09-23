from math import dist

def dist_quadrado(i, j):
    return (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2

def cross(i, j, k):  # calcula o produto cruzado de dois pontos, com origem no ponto i
    return (x[j] - x[i]) * (y[k] - y[i]) - (x[k] - x[i]) * (y[j] - y[i])

def main(entrada=input, test=False):
    global x, y
    x = [0]
    y = [0]

    for i in range(7):
        xi, yi = map(int, entrada().split())
        x.append(xi)
        y.append(yi)
    
    c1 = dist_quadrado(1, 2) + dist_quadrado (1, 3) > dist_quadrado(2, 3)  
    # angulo p2p1p3 deve ser agudo, usamos pitagoras.

    c2 = dist_quadrado(1, 2) == dist_quadrado(1, 3)
    # p1p2 e p1p3 tem o mesmo comprimento

    c3 = cross(2, 3, 4) == 0 and cross(2, 3, 5) == 0
    # p2, p3, p4 e p5 são colineares

    c4 = (x[2] + x[3]) == (x[4] + x[5]) and (y[2] + y[3]) == (y[4] + y[5])
    # ponto médio de p2p3 é coincidente com o ponto médio de p4p5
    
    c5 = dist_quadrado(2, 3) > dist_quadrado(4, 5)
    # segmento p2p3 tem comprimento maior que p4p5

    c6 = dist_quadrado(2, 4) + dist_quadrado(4, 6) == dist_quadrado(2, 6) and \
    dist_quadrado(3, 5) + dist_quadrado(5, 7) == dist_quadrado(3, 7)
    # os segmentos p4p6 e p5p7 são perpendiculares ao segmento p2p3

    c7 = dist_quadrado(4, 6) == dist_quadrado(5, 7)
    # segmentos p4p6 e p5p7 tem o mesmo comprimento

    c8 = cross(2, 3, 1) * cross(2, 3, 6) < 0
    # p1 e p6 separados pela reta que contém p2p3

    print(c1, c2, c3, c4, c5, c6, c7, c8)
    if c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8:
        c = "S"
    else:
        c = "N"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()