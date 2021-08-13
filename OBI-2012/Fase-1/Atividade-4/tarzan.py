from math import sqrt

def main(file_input=input, test=False):
    n, d = map(int, file_input().split())
    d *= d
    c = True
    arvores = []
    for _ in range(n):
        x, y = map(int, file_input().split())
        arvores.append((x, y))
    for i in range(n):
        xi, yi = arvores[i]       
        ci = False         
        
        for j in range(n):

            if i == j:
                continue                        

            xj, yj = arvores[j]                        
            distancia = (xi - xj) ** 2 + (yi - yj) ** 2

            if i == 20:
                print("Distancia loka:", distancia)
                print("Com quem: ", j)
            
            if distancia <= d :                            
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