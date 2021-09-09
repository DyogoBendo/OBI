def main(entrada=input, test=False):    
    n = entrada().strip() 
    sequencia = entrada().strip()
    RESTO = 1000000007  # enunciado pede para que o resultado seja o resto desse número

    num_digitos = len(n)  # pegamos o tamanho do alfabeto
 
    n = int(n)  # agora convertemos em um número para comparações futuras

    valores = [0 for i in range(len(sequencia))]  # criamos o vetor que armazena os números de possibilidades
    valores[-1] = 1  # definimos que o último dígito sempre tem uma possibilidade válida

    for i in range(2, num_digitos + 1):  # iniciando no penúltimo dígito, até o "n-ultimo", aqui visamos analisar apenas os n últimos valores
        if sequencia[-i] == "0":  # caso o digito que estamos considerando seja 0 pulamos, pois não existe nenhuma possibilidade válida começando com 0
            continue
        soma = 0        
        for j in range(i):  # agora avaliamos cada uma das possibilidades do n-ultimo até o n-1-ultimo...ultimo
            if i == num_digitos and j == 0:  # significa que estamos considerando todos os dígitos e o número de dígitos é o mesmo do número de dígitos limite, assim, é possível que o valor seja maior que o tamanho do alfabeto e precisamos conferir
                k = int(sequencia[-i:])
                if k < n:  # se for menor
                    soma += 1  % RESTO    # somamos 1, pois estamos considerando todos os dígitos
            else:            
                if j == 0:  # nesse caso, estamos avaliando do n-ultimo até o último, assim, todos os caracteres disponíveis até o momento, e por isso somamos 1
                    soma += 1 % RESTO
                else:
                    soma += valores[-j] % RESTO  # se não estamos olhando todos os digitos, significa que sobraram dígitos. Somamos então o número de possibilidades dessa quantia de digitos que sobraram
        valores[-i] = soma  # e agora armazenamos todas as possibilidades nessa quantia de digitos avaliada

    for i in range(len(sequencia) - num_digitos - 1, -1, -1):  # aqui visamos analisar todos os valores restantes
        if sequencia[i] == "0":   # se começar em 0 pulamos
            continue
        soma = 0
        for j in range(1, num_digitos):   # agora vamos considerar quantas possibilidades temos de 1 à n-1 digitos              
            soma += (valores[i + j]) % RESTO        
        k = int(sequencia[i:i+num_digitos])  # fazemos separado com o caso de n dígitos, pois é possível que o valor supere o número do alfabeto
        if k < n:
            soma += valores[i+num_digitos]        
        valores[i] = soma % RESTO  # adicionamos o resto da soma pela divisão pela constante passada no enunciado
        
    c = valores[0]  # e aqui está o valor que estamos procurando
    if not test:
        print(c)
    else:        
        return [c]

if __name__ == '__main__':
    main()
