if __name__ == '__main__':
    n, m = map(int, input().split())
    inversoes = []
    for _  in range(m):
        l, i, f = input().split()
        i = int(i)
        f = int(f)
        if l == "I":
            inversoes.append((i, f))
        else:
            soma = ((i + f) * (f - i + 1) )/ 2            