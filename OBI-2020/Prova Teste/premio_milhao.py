if __name__ == '__main__':
    acessos = []
    dias = 0
    milhao = 1000000

    entradas = int(input())
    for i in range(entradas):
        acessos.append(int(input()))

    for i in range(len(acessos)):
        milhao -= acessos[i]
        dias += 1
        if milhao <= 0:
            break

    print(dias)