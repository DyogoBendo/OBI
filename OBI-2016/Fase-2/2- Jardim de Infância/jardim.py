from math import sqrt

def main(entrada=input, test=False):
    p1 = tuple(map(int, entrada().split()))
    p2 = tuple(map(int, entrada().split()))
    p3 = tuple(map(int, entrada().split()))
    p4 = tuple(map(int, entrada().split()))
    p5 = tuple(map(int, entrada().split()))
    p6 = tuple(map(int, entrada().split()))
    p7 = tuple(map(int, entrada().split()))

    p1p2 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    p1p3 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
    p2p3 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2

    c1 = p1p2 + p1p3 > p2p3 # analise se angulo formado entre os pontos p2p1p3 é agudo
    c2 = p1p2 == p1p3 

    tg_p2p3 = p3[0] - p2[0] / p3[1] - p2[1]    
    reta_p2p3_b = -(tg_p2p3 * p2[0]) + p2[1]
    
    tg_p3p4 = p4[0] - p3[0] / p4[1] - p3[1]    
    reta_p3p4_b = -(tg_p3p4 * p3[0]) + p3[1]
    
    tg_p4p5 = p5[0] - p4[0] / p5[1] - p4[1]    
    reta_p4p5_b = -(tg_p4p5 * p4[0]) + p4[1]
    
    c3 = tg_p2p3 == tg_p3p4 == tg_p4p5 and reta_p2p3_b == reta_p3p4_b == reta_p4p5_b # chega de os pontos p2, p3, p4 e p5 são colineares

    c4 = (p2[0] + p3[0]) / 2 == (p4[0] + p5[0]) / 2 and (p2[1] + p3[1]) / 2 == (p4[1] + p5[1]) / 2 # ponto medio de p2p3 e p4p5 são os mesmos

    c5 = (p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2 > (p5[0] - p4[0]) ** 2 + (p5[1] - p4[1]) ** 2  # checa se p2p3 é maior que p4p5

    p2p6 = (p2[0] - p6[0]) ** 2 + (p2[1] - p6[1]) ** 2
    p2p4 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
    p4p6 = (p6[0] - p4[0]) ** 2 + (p6[1] - p4[1]) ** 2

    p3p7 = (p3[0] - p7[0]) ** 2 + (p3[1] - p7[1]) ** 2
    p3p5 = (p3[0] - p5[0]) ** 2 + (p3[1] - p5[1]) ** 2
    p5p7 = (p5[0] - p7[0]) ** 2 + (p5[1] - p7[1]) ** 2

    c6 = p2p6 == p2p4 + p4p6 and p3p7 == p3p5 + p5p7
    c7 = p4p6 == p5p7

    tg_p1p6 = (p6[0] - p1[0]) / (p6[1] - p1[1])    
    reta_p1p6_b = -(tg_p1p6 * p1[0]) + p1[1]


    x = (p3[0] - p2[0])
    y = (p3[1] - p2[1])
    if x != 0 and y != 0:
        tg_p2p3 =  x/y
        reta_p2p3_b = -(tg_p2p3 * p2[0]) + p2[1]
    else:
        if y == 0:
            tg_p2p3 =  0
            reta_p2p3_b = -(tg_p2p3 * p2[0]) + p2[1]        
            
    print(f"reta P2P3: {tg_p2p3}x + ({reta_p2p3_b})")

    try:
        x_encontro = (reta_p1p6_b - reta_p2p3_b) / (tg_p2p3 - tg_p1p6)
        y_encontro = tg_p1p6 * x_encontro + reta_p1p6_b
        print(x_encontro, y_encontro)
        c8 = min(p1[0], p6[0]) <= x_encontro <= max(p1[0], p6[0]) and min(p1[1], p6[1]) <= y_encontro <= max(p1[1], p6[1])   # a reta p1p6 e o segmento p2p3 devem ser concorrentes
    except:        
        c8 = False

    print(c1, c2, c3, c4, c5, c6, c7, c8)

    c = "S" if c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 else "N"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()