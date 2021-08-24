# solução gulosa

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    fechaduras = list(map(int, entrada().split()))
    c = 0
    for i in range(n - 1):
        k = m - fechaduras[i]
        fechaduras[i] += k
        fechaduras[i + 1] += k
        c += abs(k)

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()