def find_translation(palavra: str):    
    try:                
        return dicionario[palavra]  # se existir a palavra, retornamos o que ela representa no dicionário
    except:  # senão        
        tamanho_pastas.append(len(palavra) + 1)  # adicionamos o tamanho dessa pasta em tamanho_pastas
        position = len(dicionario)  # a posição em que ela é inserida é na última posição do dicionário
        dicionario[palavra] = position  # e mantemos nessa palavra essa informação: a posição que ela foi inserida no dicionário
        return dicionario[palavra]
            

def separate_string(path: str) -> list:
    string_begin = 0  # de onde a string começa 
    ret = [0]  # posições das palavras , começamos pela raiz
    for i in range(len(path)):  # verificamos cada caracter do path passado
        if path[i] == "/":  # se for uma / indica que antes dela é o nome de uma pasta
            mounted = path[string_begin:i]  # pegamos o nome dessa pasta que está antes dessa barra                    
            idx_mapa = find_translation(mounted)  # encontramos a "tradução" desse nome de pasta, que é a posição da palavra no dicionário                        
            ret.append(idx_mapa)  # adicionamos essa posição 
            string_begin = i + 1  # e agora o inicio é na posição posterior ao "/", pois é a partir dali que é formada a próxima palavra
    return ret  # retornamos a lista de posições das palavras dos arquivos

def achar_arquivos_recursivamente(idx: int):        
    for u in adj[idx]:  # verificamos cada uma das subpastas de uma pasta 
        if already_searched[u]:  # se a palavra já foi "olhada", pulamos
            continue        
        achar_arquivos_recursivamente(u)  # verificamos então as subpastas dessa subpasta
        already_searched[u] = True  # informamos que já foi visitado
        arquivo_subpastas[idx] += arquivo_subpastas[u]  # e adicionamos todas as subpastas da nossa subpasta na pasta atual    


def busca_melhor_solucao(idx:int, solucao_idx:int):    
    global melhor_solucao
    for u in adj[idx]:   # verificamos cada subpasta de uma pasta          
        if already_searched[u]:  # se ela já foi verificada, pulamos
            continue
        nova_solucao = solucao_idx - (tamanho_pastas[u] * arquivo_subpastas[u]) + (3 * (n - arquivo_subpastas[u]))        
        # a nova possível solução será o número de caracteres partindo da pasta pai, subtraindo pelo número de arquivos que partem de u multiplicado pelo tamanho de u, pois para todos esses removemos a palavra do arquivo u do caminho, somado com 3 vezes o número de arquivos que não está em u, já que para todos que não estão em u, adicionamos "../"        
        melhor_solucao = min(melhor_solucao, nova_solucao)  # pegamos o menor entre o novo caminho e o que se tinha                

        busca_melhor_solucao(u, nova_solucao)  # buscamos a solução partindo da subpasta u 
        already_searched[u] = True  # informamos que u já foi pesquisado

def main(entrada=input, test=False):
    global dicionario, tamanho_pastas, arquivo_subpastas, adj, n, melhor_solucao, already_searched

    arquivo_subpastas = [0 for _ in range(10 ** 5)]  # número de subpastas de um arquivo
    tamanho_pastas = [0]  # tamanho das pastas de cada arquivo
    adj = [[] for _ in range(10 ** 5)]  # pastas adjacentes  

    tamanho_inicial = 0  # tamanho da cadeia começando pela raiz
    dicionario = {"": 0}  # dicionário dos nomes de pastas e seus tamanhos, iniciamos com um valor

    n = int(entrada())

    for i in range(n):
        file_path = entrada().strip()  # caminho até um arquivo
        tamanho_inicial += len(file_path)  # aumenta o tamanho inicial
        caminho = separate_string(file_path)  # separamos o caminho nas posições de cada palavra no dicionário
        arquivo_subpastas[caminho[-1]] += 1  # na posição da última pasta que encontramos, adicionamos a informação de um arquivo nela        
        for j in range(len(caminho) - 1):  # para cada pasta no caminho            
            u = caminho[j]  # pegamos uma pasta
            v = caminho[j + 1]  # e a que vem logo após ela            
            adj[u].append(v)  # e armazenamos que essa pasta v é uma subpasta de u

    already_searched = [False for _ in range(10 ** 5)]
    achar_arquivos_recursivamente(0)  # agora verificamos recursivamente os arquivos            

    already_searched = [False for _ in range(10**5)]
    melhor_solucao = tamanho_inicial  # começamos com a melhor soluçao sendo a solução inicial
    busca_melhor_solucao(0, tamanho_inicial)  # e então verificamos se escolhendo outra pasta que não seja a raiz teremos uma solução melhor, começando da primeira
    
    if not test:
        print(melhor_solucao)
    else:         
        return [melhor_solucao]

if __name__ == '__main__':
    main()