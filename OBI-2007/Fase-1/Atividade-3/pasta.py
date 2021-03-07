if __name__ ==  "__main__":
    p, n = map(int, input().split())
    posic = [0 for i in range(p)]
    for i in range(n):
        entrada = int(input())
        posic[entrada - 1] += 1
    
    menor = min(posic)
    base_case = [ value - menor for value in posic]
    
    worked = True
    for i in range(1, len(base_case)):
        ant = base_case[i - 1]
        atual = base_case[i]
        if ant > 1:
            worked = False
            break
        if ant == 0 and atual == 1: 
            worked = False
            break
        if atual > 1:
            worked = False
            break
        
    if worked: 
        print("S")
    else:
        print("N")