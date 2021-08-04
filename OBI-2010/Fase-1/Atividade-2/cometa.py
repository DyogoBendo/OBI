if __name__ == '__main__':
    a = int(input())
    diferenca_passagem = a - 1986
    tempo_proximo = 76 - diferenca_passagem % 76 
    ano_proximo = a + tempo_proximo
    print(ano_proximo)