def main(entrada=input, test=False):    
    n = entrada().strip()  #  < 10 ^ 100 -> no máximo 100 dígitos    
    sequencia = entrada().strip()  # <= 10 ^ 5
    RESTO = 1000000007

    num_digitos = len(n)

    n = int(n)

    valores = [0 for i in range(len(sequencia))]
    valores[-1] = 1

    for i in range(2, num_digitos + 1):        
        if sequencia[-i] == "0":            
            continue
        soma = 0        
        for j in range(i):     
            if i == num_digitos and j == 0:
                k = int(sequencia[-i:]) if j == 0 else int(sequencia[-i:-j])                
                if k < n:
                    soma += 1                
            else:            
                if j == 0:
                    soma += 1
                else:
                    soma += valores[-j]              
        valores[-i] = soma

    for i in range(len(sequencia) - num_digitos - 1, -1, -1):
        if sequencia[i] == "0":            
            continue
        soma = 0
        for j in range(1, num_digitos):                        
            soma += (valores[i + j]) % RESTO        
        k = int(sequencia[i:i+num_digitos])
        if k < n:
            soma += valores[i+num_digitos]        
        valores[i] = soma % RESTO
        
    c = valores[0]       
    if not test:
        print(c)
    else:        
        return [c]

if __name__ == '__main__':
    main()
