def main(entrada=input, test=False):
    n = int(entrada())

    pecas = [1 for _ in range(10**6)]   
    palavra = ""     
    for i in range(n):
        e, l, d = entrada().split()
        e = int(e)
        d = int(d)                
        pecas[e] = (d, l)  # guardamos com que peça a peça e se liga e a letra
    
    atual = 0  # começamos pelo 0
    while atual != 1:  # e vamos até o 1
        atual, l = pecas[atual]  # pegamos a próxima peça e a letra dessa
        palavra += l  # concatenamos a letra à pelavra

    if not test:
        print(palavra)
    else:
        return [palavra]

if __name__ == '__main__':
    main()