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


def main(entrada=input, test=False):    
    n, m = map(int, entrada().split())
    a = list(map(int, entrada().split()))
    a.insert(0, 0)
    f = list(map(int, entrada().split()))    
    ogros = list(map(int, entrada().split()))    

    s = ''
    for o in ogros:
        s += str(f[pontuacao(a, o, n)]) + ' '    

    if not test:
        print(s[:-1])    
    else:
        return [s[:-1]]
if __name__ == '__main__':
    main()
