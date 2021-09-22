def main(entrada=input, test=False):
    n, d = map(int, entrada().split())
    sanduiches = list(map(int, entrada().split()))

    c = 0
    s = 0
    j = 0
    for i in range(n):  # inciando em cada posição
        if j < i: # se o j "ficou pra trás" do i
            s += sanduiches[j + 1]
            j += 1  # equiparamos
        while j < n and s < d:  # enquanto o o tamanho de pedaçõs for menor do que queremos e ainda é possível somar
            s += sanduiches[j]  # pegamos um pedaço
            j += 1  # e avançamos
        if s == d: c += 1  # se o conseguimos formar um pedaço do tamanho que queríamos, então adicionamos um caso possível
        s -= sanduiches[i]  # apagamos o pedaço inicial da sequência, para que possamos continuar
    
    s = sanduiches[- 1]  # agora começamos a soma do final
    j = n - 1 
    while j - 1 > 0 and sanduiches[j - 1] + s < d:   # enquanto pudermos reduzir j, e a soma for menor que a desejada
        s += sanduiches[j - 1]  # aumentamos a soma dos pedaços
        j -= 1  # e diminuimos j
    # j termina na posição que ultrapassa ou é igual a d
    for i in range(n - 1):  # agora vamos do incio até o penultimo
        s += sanduiches[i]  # aumentamos o sanduiche
        while j < n- 1 and s > d:  # enquanto j for menor que o penúltimo e a soma tiver ultrapassado
            s -= sanduiches[j]  # retiramos pedaços do começo da sequência que está a direita  
            j += 1  # e aumentamos j, pois agora a sêquencia diminui, então j está apontando para o inicio da sequência novamente
        if i == j:  # se i e j forem iguais
            s -= sanduiches[j]  # desconsideramos o sanduíche, pois eles não podem estar "emendados"
            j += 1  # aumentamos j
        if s == d: c += 1  # se a soma resultante for igual ao tamanho que queremos, adicionamos um caso


    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()