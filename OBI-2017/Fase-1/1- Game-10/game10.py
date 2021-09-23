def main(entrada=input, test=False):
    n = int(entrada())
    d = int(entrada())
    a = int(entrada())

    if a > d:  # se precisamos subir para chegar na posição desejada
        c = n - a + d  # então temos que descer até o final e andar do inicio até a posição
    else:
        c = d - a  # senão, é só descer

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()