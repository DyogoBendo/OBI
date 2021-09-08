def main(entrada=input, test=False):    
    n, m = map(int, entrada().split())

    MAX_SIZE = (10 ** 6) + 1
    count = [0 for _ in range(MAX_SIZE)]  # em cada posição i, guardamos o número de escolhas ótimas possíveis com i chocolates
    forbiden = [0 for _ in range(MAX_SIZE)]  # em cada posição i, informamos qual escolha j "proibida", que se outro jogador escolhesse, quem teria  a vez com i chocolates perderia
    
    for i in range(n + 1):  # começamos a construir de baixo para cima 
        if count[i] == 0:  # caso não há nenhuma escolha possível
            for j in range(1, m + 1):  # significa que se o jogador anterior pegar qualquer valor que gerá essa posição, ele irá ganhar
                count[i + j] += 1  # assim, adicionamos 1 para cada um desses casos
                forbiden[i + j] = j 
                # adicionamos ao forbiden desse caso o próprio valor j
                # porque caso o seja pego j logo na jogada anterior, então ele não estará disponível
                # inviabilizando que seja escolhido agora, que seria uma escolha ótima                
        if count[i] == 1:  # só temos um caso ótimo, ou seja, ele pode ser "cancelado" por um forbiden
            count[i + forbiden[i]] += 1  # assim, na posição i + forbiden[i], ou seja, quando temos i + o número ótimo de i, temos a opção de ganhar escolhendo o número proibido de i
            forbiden[i + forbiden[i]] = forbiden[i] # e o proibido dessa escolha é justamente o proibido do i, pois é esse o valor que permite a vitória nesse caso    
    c = "Carlos" if count[n] == 0 else "Paula" # como a Paula sempre começa, Carlos só ganha quando na primeira escolha, não houver nenhuma opção ótima    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()