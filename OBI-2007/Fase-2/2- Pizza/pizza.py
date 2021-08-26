def sum_max_sublist(pizza, n):    
    init = 0
    end = 0
    max_sum = 0
    while init < n:
        s = 0
        while end < n:                                    
            s += pizza[end]
            end += 1
            if s < 0:                
                break
            if s > max_sum:
                max_sum = s            
        init = end
    return max_sum

def main(entrada=input, test=False):    
    n = int(entrada())
    fatias = list(map(int, entrada().split()))    
    n = len(fatias)

    somas = [0 for _ in range(n + 1)]    
    melhor = [0 for _ in range(n + 1)]

    for i in range(n):  
        somas[i + 1] = somas[i] + fatias[i]  # realizamos o cálculo da soma para que possa ser acessado em tempo constante qualquer soma
        melhor[i + 1] = max(melhor[i], somas[i + 1])  # guardamos a melhor soma anterior à fatia

    m = 0
    for i in range(n + 1):
        m = max(m, melhor[i] + somas[n] - somas[i]) 
        # verificamos o melhor caso em que a soma "da volta", então é soma dos números partindo de i até n e então somamos com a melhor soma que vai até i
    
    atual = 0
    for i in range(n):        
        atual = max(0, atual + fatias[i])
        # fazemos a verificação para a melhor soma contínua sem dar voltas
        # se a soma for negativa, então zeramos a nossa variavel atual
        # para na próxima iteração começarmos a somar do 0 
        # e assim encontrar a maior soma seguida
        m = max(atual, m)

    if not test:
        print(m)
    else:
        return [m]

if __name__ == '__main__':
    main()
