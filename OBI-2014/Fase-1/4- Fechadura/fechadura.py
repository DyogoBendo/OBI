# solução gulosa

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    fechaduras = list(map(int, entrada().split()))
    c = 0
    for i in range(n - 1):  # como a solução é garantida, percorremos do 1 ao penúltimo, pois o último deverá estar ordenado "automaticamente"
        k = m - fechaduras[i]  # pegamos a diferença da altura da fechadura pela altura que deveria estar
        fechaduras[i] += k  # adicionamos esse valor a fechadura, para agora ela estar correta
        fechaduras[i + 1] += k  # e somos obrigados a modificar o valor de seu vizinho junto
        c += abs(k)  # somamos o número de modificações feitas

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()