def main(entrada=input, test=False):
    c, n = map(int, entrada().split())
    local = {}
    internet = {}
    for i in range(c):
        id, version = entrada().split()
        local[id] = int(version)
    
    for i in range(n):
        id, version = entrada().split()
        try:
            if internet[id] < int(version):
                internet[id] = int(version)
        except:
            internet[id] = int(version)


    r = []
    chaves = list(map(int, internet.keys()))
    chaves.sort()    
    for id in chaves:
        id = str(id)
        resposta = id + " " + str(internet[id])
        try: 
            if local[id] < internet[id]:                
                if not test:
                    print(resposta)
                else:
                    r.append(resposta)                    
        except:
            if not test:
                print(resposta)
            else:
                r.append(resposta)
    if test:
        return r                            

if __name__ == '__main__':
    main()