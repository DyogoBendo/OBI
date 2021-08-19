def main(file_input=input, test=False):
    n = int(file_input())
    valores = []
    for i in range(n):
        v = int(file_input())
        if i == 0:
            a = v
        elif i == n-1:
            b = v
        else:
            valores.append(v)
    m = min(a, b)
    c = 0
    k = 0
    ultimo_alto = 0

    for i in range(len(valores)):
        v = valores[i]
        if v < m:            
            c += 1
        else:
            if v < a:
                k += 1                            
            if v >= a:
                a = v                
                c += k
                ultimo_alto = i
                k = 0
    b = 0
    for i in range(ultimo_alto, len(valores)):
        v = valores[i]
        if v > b:
            b = v

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()