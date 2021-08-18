def main(file_input=input, test=False):
    m, n = map(int, file_input().split())
    x = list(map(int, file_input().split()))
    y = list(map(int, file_input().split()))

    if m > n:
        k = m
        for i in range(m - n):
            y.append(0)
    else:
        k = n
        for i in range(n - m):
            x.append(0)
    subiu = [0 for _ in range(k)]
    resposta = [0 for _ in range(k)]
    for i in range(k-1, -1, -1):
        s = x[i] + y[i] + subiu[i]
        if s == 2:
            subiu[i -1] = 1
            s = 0
        if s == 3:
            subiu[i -1] = 1
            s = 1
        resposta[i] = s
    c = " ".join(list(map(str, resposta)))

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()