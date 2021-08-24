def main(entrada=input, test=False):
    n = int(entrada())

    pecas = [1 for _ in range(10**6)]   
    palavra = ""     
    for i in range(n):
        e, l, d = entrada().split()
        e = int(e)
        d = int(d)                
        pecas[e] = (d, l)
    
    atual = 0
    while atual != 1:
        atual, l = pecas[atual]
        palavra += l

    if not test:
        print(palavra)
    else:
        return [palavra]

if __name__ == '__main__':
    main()