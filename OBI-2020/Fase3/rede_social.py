if __name__ == '__main__':
    mensagens = int(input())
    indice_repostagem = []
    fator_influencia = 0

    for i in range(mensagens):
        indice_repostagem.append(int(input()))

    for i in range(mensagens):
        atinge_influencia = 0
        for j in range(mensagens):
            if i <= indice_repostagem[j]:
                atinge_influencia += 1
        if atinge_influencia < i:
            break
        fator_influencia = i
    print(fator_influencia)
