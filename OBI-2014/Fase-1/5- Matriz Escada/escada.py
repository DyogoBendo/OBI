def main(entrada=input, test=False):
    n, m = map(int, entrada().split())    
    p = True
    for i in range(n):
        linha = list(map(int, entrada().split()))
        if i > 0:        
            if sum(linha[0:k + 1]) > 0:                
                p = False
        k = n - 1
        for j in range(m):
            if linha[j] > 0:
                k = j
                break
    c = "S" if p else "N"
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()