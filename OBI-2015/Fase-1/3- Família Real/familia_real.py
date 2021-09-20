from queue import Queue

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())

    descendentes = [[] for _ in range(n + 1)]
    pais = list(map(int, entrada().split()))
    presentes = list(map(int, entrada().split()))    

    for i in range(n):
        p = pais[i]
        descendentes[p].append(i + 1)  # guardamos quais são os filhos de cada pai

    geracao = [0 for i in range(n + 1)]  # a qual geração cada um pertence
    fila = Queue()
    fila.put_nowait((0, 0))    
    while not fila.empty():  # fazemos uma busca em largura partindo do rei
        pai, geracao_pai = fila.get_nowait()        
        filhos = descendentes[pai]
        for f in filhos:
            geracao[f] = geracao_pai + 1  # a geração de cada filho é a geração do pai + 1
            fila.put_nowait((f, geracao_pai + 1))
    
    qtdd_geracao = [[0, 0] for _ in range(geracao_pai + 1)]  # quantas pessoas existem em cada geração, sendo o total a geração do último que foi incluído

    for i in range(1, n + 1):
        qtdd_geracao[geracao[i]][1] += 1  # adicionamos ao total de pessoas da geração que a pessoa pertence

    for p in presentes:
        qtdd_geracao[geracao[p]][0] += 1  # adicionamos ao total de pessoas da geração que estão presentes       

    c = " ".join([f'{qtdd_geracao[i][0] / qtdd_geracao[i][1] * 100:.2f}' for i in range(1, geracao_pai + 1)])  # e aqui fazemos a divisão da relação quantidade de presentes pela quantidade total.
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()