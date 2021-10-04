def main(file_input=input, test=False):
    n = int(file_input())
    alturas = list(map(int, file_input().split()))

    c = 2
    menor = False
    for i in range(1, n):
        if alturas[i] < alturas[i - 1]:
            menor = True
        else:
            if menor: 
                c += 1
            menor = False


    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()