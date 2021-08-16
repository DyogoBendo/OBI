def main(file_input=input, test=False):
    n, m = map(int, file_input().split())

    familias = [i for i in range(n + 1)]
    filhos = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, file_input().split())
        familias[a] = familias[b]

        filhos[b].append(a)
        filhos[b] += filhos[a]
        for f in filhos[a]:
            familias[f] = familias[b]

    print(familias)
    print(filhos)
    
    diferentes = set(familias[1:])
    c = len(diferentes)

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()