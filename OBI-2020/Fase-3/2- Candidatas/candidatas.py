def calcula_mdc(n, d):
    r = n % d
    if d == 1 or r == 1:
        return 0
    if r == 0:
        return 1
    else:
        calcula_mdc(d, r)


def retorna_mdc(sequencia):
    if len(sequencia) == 1:
        if sequencia[0] > 1:
            return 1
        else:
            return 0

    sequencia.sort()

    for i in range(0, len(sequencia)):
        for j in range(i, len(sequencia)):
            d = sequencia[i]
            n = sequencia[j]
            if calcula_mdc(n, d) == 0:
                return 0
    return 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    sequencia = input().split()
    s = []
    for i in range(n):
        s.append(int(sequencia[i]))

    for i in range(m):
        tipo, a, b = map(int, input().split())
        a -= 1
        if tipo == 1:
            s[a] = b
        else:
            candidatos = 0
            sub_sequencia = s[a:b]
            for j in range(len(sub_sequencia)):
                for k in range(j + 1, len(sub_sequencia) + 1):
                    sequencia_teste = sub_sequencia[j:k]
                    candidatos += retorna_mdc(sequencia_teste)
            print(candidatos)
