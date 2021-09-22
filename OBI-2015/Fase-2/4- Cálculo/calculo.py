def main(entrada=input, test=False):
    m, n = map(int, entrada().split())
    x = list(map(int, entrada().split()))
    y = list(map(int, entrada().split()))

    if m > n:  # se o primeiro elemento tiver mais digitos
        k = m
        for i in range(m - n):  
            y.append(0)  # adicionamos 0 em y para que ele fique com o mesmo número de digitos
    else:  # senão
        k = n
        for i in range(n - m):  
            x.append(0)  # adicionamos dígitos ao x
    subiu = [0 for _ in range(k)]
    resposta = []
    apareceu_1 = False

    # realizamos uma soma binária normal
    for i in range(k-1, -1, -1):    
        s = x[i] + y[i] + subiu[i]
        if s == 2:  # se a soma for 2
            subiu[i -1] = 1  # sobe um valor para a próxima soma
            s = 0  # e fica 0 aqui
        if s == 3:  # se for 3
            subiu[i -1] = 1  # sobe 1
            s = 1  # e a soma aqui fica 1
        if s == 1:  # se tiver 1 na soma
            apareceu_1 = True  # quer dizer que apareceu 1
        if apareceu_1:  # a partir do momento que tiver aparecido algum 1 no resultado, passamos a adicionar             
            resposta.insert(0, s)
    c = " ".join(list(map(str, resposta)))

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()