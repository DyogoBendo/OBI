def main(file_input=input, test=False):
    n, q = map(int, file_input().split())
    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(q):
        entrada = file_input().split()
        if len(entrada) == 3:
            a, x, r = map(int, entrada.split())
            if a == 1:
                tabuleiro[x] = [r for _ in range(n)]
            else:
                for j in range(n):
                    tabuleiro[j][x] = r
        else:
            a, x = map(int, entrada.split())
            if a == 3:
                k = tabuleiro[x]
            else:
                k = []
                for j in range(n):
                    k.append(tabuleiro[j][x])

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()