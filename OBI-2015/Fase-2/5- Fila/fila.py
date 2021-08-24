def main(entrada=input, test=False):
    n = int(entrada())
    fila = list(map(int, entrada().split()))
    q = int(entrada())
    for j in range(q):
        t, i, x = map(int, entrada().split())
        if t == 0:
            fila.insert(i, x)
        else:
            c = 0
            for k in range(i - 2, -1, -1):
                if fila[k] > fila[i - 1] + x:
                    c = k + 1
                    break
            if not test:                
                print(c)
            else:
                return [c]
            
            


if __name__ == '__main__':
    main()