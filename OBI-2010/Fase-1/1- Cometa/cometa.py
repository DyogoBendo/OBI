def main(entrada=input, test=False):
    a = int(entrada())
    diferenca_passagem = a - 1986
    tempo_proximo = 76 - diferenca_passagem % 76 
    ano_proximo = a + tempo_proximo
    c = ano_proximo
    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
    