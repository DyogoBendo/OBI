def main(entrada=input, test=False):
    a = int(entrada())
    diferenca_passagem = a - 1986  # contamos quantos anos se passaram desde uma das passagens registradas
    tempo_proximo = 76 - diferenca_passagem % 76  # o tempo que falta para o próximo é justamente saber quando tempo se passou do último e quanto falta para o próximo
    ano_proximo = a + tempo_proximo  # somamos o ano inicial a quanto tempo falta
    c = ano_proximo
    
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()
    