if __name__ == '__main__':
    menor = []

    doces = int(input())
    for i in range(3):
        menor.append(int(input()))

    menor.sort()
    evolucoes = 0

    for i in range (3):
        if doces - menor[i] >= 0:
            doces -= menor[i]
            evolucoes += 1

    print(evolucoes)