def main(entrada=input, test=False):
    n = int(entrada())
    c = 0
    atual = 0    
    for i in range(n):
        l = entrada()
        if i % 2 == 0:  # nas linhas pares, o pacman percorre da esquerda para direita
            for j in range(n):                        
                if l[j] == "o":  # se for comida, aumentamos o atual
                    atual += 1
                if l[j] == "A":  # se for fantasmas, zeramos o atual
                    atual = 0
                if atual > c:  # se o que temos de comida atualmente é maior que o máximo que já tivemos, esse é o nosso novo máximo
                    c = atual
        else:  # nas linhas impares o pacman percorre da direita para a esquerda
            for j in range(n - 1, -1, -1):                
                if l[j] == "o":
                    atual += 1
                if l[j] == "A":
                    atual = 0
                if atual > c:
                    c = atual        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()