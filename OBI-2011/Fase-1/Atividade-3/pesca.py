def main(file_input=input, test=False):
    n = int(file_input())    
    squares = []
    for i in range(n):
        xi, xf, yi, yf = map(int, file_input().split())
        squares.append((xi, xf, yi, yf))
    c = 0

    for xi, xf, yi, yf in squares:
        c += (xf - xi) * (yf - yi)  # calculo das areas totais

    quadrados_resolvidos = []

    for xi, xf, yi, yf in squares:
        retangulos_intersec = []
        for sxi, sxf, syi, syf in quadrados_resolvidos:
            intersecta_x = False
            intersecta_y = False                        

            if xi < sxi:        
                if sxi < xf:
                    intersecta_x = True
                    ixi = sxi
                    ixf = xf                
            elif xi > sxi:
                if xi < sxf:
                    intersecta_x = True
                    ixi = xi
                    ixf = sxf
            else:
                intersecta_x = True
                ixi = xi
                ixf = xf if xf < sxf else sxf
            
            if yi < syi:        
                if syi < yf:
                    intersecta_y = True
                    iyi = syi
                    iyf = yf                
            elif yi > syi:
                if yi < syf:
                    intersecta_y = True
                    iyi = yi
                    iyf = syf
            else:
                intersecta_y = True
                iyi = yi
                iyf = yf if yf < syf else syf

            if intersecta_x and intersecta_y:
                rect_interc = (ixi, ixf, iyi, iyf)
                retangulos_intersec.append(rect_interc)
        
        

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()