from math import inf

def main(entrada=input, test=False):
    n, k = map(int, entrada().split())
    valores = list(map(int, entrada().split()))
    valores.sort()  # ordenamos os valores do mais próximo do inicio da avenida ao mais distante

    l = n - k - 1  # quantidade de prédios restantes a partir de um dado prédio
    c = inf

    for i in range(n - l): 
        a = valores[i]  # o primeiro (o mais perto da avenida) prédio que mantemos é o prédio i
        b = valores[i + l]  # e o último (o mais longe da avenida) prédio que manteemos é o prédio i + l, o que dá uma quantidade n - k de prédio mantidos
        c = b - a if b - a < c else c  # verificamos se esse é caso com a menor distância do prédio inicial em relação ao final.

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()