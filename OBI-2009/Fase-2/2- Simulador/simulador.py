def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    inversoes = []
    r = []
    for _  in range(m):
        l, i, f = entrada().split()
        i = int(i)
        f = int(f)
        if l == "I":
            inversoes.append((i, f))
        else:
            soma = ((i + f) * (f - i + 1) )/ 2            
            if not test:
                print(soma)
            else:    
                r.append(soma)
    if test:
        return r

if __name__ == '__main__':
    main()