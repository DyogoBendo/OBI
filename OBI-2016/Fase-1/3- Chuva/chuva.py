def main(entrada=input, test=False):
    n = int(entrada())
    valores = []
    for i in range(n):
        v = int(entrada())
        if i == 0:
            a = v
        elif i == n-1:
            b = v        
        valores.append(v)    
    c = 0
    k = 0
    ultimo_alto = 0    

    m = a

    for i in range(1, len(valores)):
        v = valores[i]        
        if v >= m:            
            ultimo_alto = i
            m = v
        else:  # quando o valor é menor do que o maior da esquerda que encontramos, nós contamos
            c += 1            
        
    if ultimo_alto != n - 1:        
        m = b        
        for i in range(n - 1, ultimo_alto, -1):                                    
            v = valores[i]
            if v >= m:  # precisamos desconsiderar todos os limites que contamos anteriormente
                c -= 1    
                m = v                                        

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()