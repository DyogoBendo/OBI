def main(entrada=input, test=False):
    m, n = map(int, entrada().split())
    x = list(map(int, entrada().split()))
    y = list(map(int, entrada().split()))

    if m > n:
        k = m
        for i in range(m - n):
            y.append(0)
    else:
        k = n
        for i in range(n - m):
            x.append(0)
    subiu = [0 for _ in range(k)]
    resposta = []
    apareceu_1 = False
    for i in range(k-1, -1, -1):                
        s = x[i] + y[i] + subiu[i]
        if s == 2:
            subiu[i -1] = 1
            s = 0
        if s == 3:
            subiu[i -1] = 1
            s = 1
        if s == 1:
            apareceu_1 = True
        if apareceu_1:            
            resposta.insert(0, s)
    c = " ".join(list(map(str, resposta)))

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()