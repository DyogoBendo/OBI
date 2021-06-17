if __name__ == "__main__":
    n = int(input())
    k = -1
    enviados = dict()
    recebidos = dict()
    
    for i in range(n):
        l, v = input().split()        
        if l == "T":
            k += int(v) - 1
        else:            
            k += 1            
            if l == "E":
                try:
                    enviados[v].append(k)
                except:
                    enviados[v] = [k]
            else:
                try:
                    recebidos[v].append(k)
                except:
                    recebidos[v] = [k]
            
    for key in sorted (recebidos.keys()):                        
        try:            
            r = recebidos[key]
            e = enviados[key]
            if len(r) == len(e):
                v1 = sum(r)
                v2 = sum(e)
                v = v2 - v1
                print(key, v)                
            else:
                print(key, "-1")
        except:
            print(key, "-1")        