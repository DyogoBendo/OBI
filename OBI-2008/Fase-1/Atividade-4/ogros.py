def pontuacao(a, forca, n ):
    ini = 0
    fim = n

    while(fim - ini > 1):        
        med = (fim + ini) // 2        
        if a[med] <= forca:
            ini = med
        else:
            fim = med    
    return fim - 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    f = list(map(int, input().split()))    
    ogros = list(map(int, input().split()))    

    s = ''
    for o in ogros:
        s += str(f[pontuacao(a, o, n)]) + ' '
    print(s[:-1])    