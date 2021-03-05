if __name__ ==  "__main__":
    p, n = map(int, input().split())
    posic = {}
    
    for i in range(n):
        entrada = input()
        try:
            posic[entrada] += 1
        except:
            posic[entrada] = 1  
    
    maior = max(posic.values())
    menor = min(posic.values())
    
    if (maior - menor) >= 2:
        print("N")
    else:
        last_key = 0
        check = True
        if len(posic.keys()) == 1:
            check = False
        for value, key in posic.items():
            if value == maior:
                if last_key == 0:
                    last_key = key
                else:
                    if int(key) == int(last_key) + 1:
                        last_key = key
                    else:
                        check = False                        
                        break
        
        if check:
            print("S")
        else:
            print("N")
    