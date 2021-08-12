from math import sqrt

def main(file_input=input, test=False):
    n, d = map(int, file_input().split())
    c = True
    arvores = []
    for _ in range(n):
        x, y = map(int, file_input().split())
        arvores.append((x, y))
    for i in range(n):
        xi, yi = arvores[i]       
        ci = False 
        s = 0
        
        for j in range(n):
            if i == j:
                continue
            xj, yj = arvores[j]                        
            distancia = sqrt((((xi - xj) ** 2) + ((yi - yj) ** 2)))

                

            if distancia > d:
                s += 1
                # print(xi, yi, "-", xj, yj, ":", distancia)
            if distancia <= d :            
                if i == 20 or i == 35 or i == 61 or i == 67 or i == 95:
                    print("Atual i:", i, "Atual j:", j)
                    print("Distancia:", distancia, "-", "x e y:", xj, yj)
                    print()                
                ci = True                  
        if ci is False:
            c = False    

    if not test:
        if c:
            print("S")
        else:
            print("N")        
    else:
        if c:
            return["S"]
        else:
            return["N"]

if __name__ == '__main__':
    main()