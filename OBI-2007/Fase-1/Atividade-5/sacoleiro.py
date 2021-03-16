global n, t, grafo, presente, sinal, matrix  # declaramos variáveis globais a fim de facilitar o trabalho

def convert_to_number(letra):  # realiza a conversão de letra em número
    if letra == "A":
        return 0
    else:
        return 1

def dfs(c, a, b):
    global matrix    
    global presente
    global sinal
    global n
    
    # Verificamos se aquela posição, para aquela cidade, com aquele valor de A e aquele valor de B, já foi considerado
    if matrix[c][a][b] == 0:  
    # Se não, passamos a considerar
    # Se sim, a chamada é encerrada
        matrix[c][a][b] = 1
    
        if a + b + presente[c] <= t:
        # Verificamos se, somando o que já foi gasto com A, gasto com B e somado com o que podemos gastar na cidade C, ainda temos dinheiro
        # Se tivermos, continuamos
        # Se não tivermos, a chamada é encerrada
            if sinal[c] == 0:
            # Verificamos o sinal da cidade, ou seja, qual o tipo de presente dela
            # Se for uma cidade do tipo A, então chamamos recursivamente essa função, mas considerando o valor de A como o valor que tinha sido gastado com A até agora, mais o valor que pode ser gasto de A nessa cidade
                dfs(c, a + presente[c], b)
            else:
            # Se for uma cidade do tipo B, fazemos a mesma coisa que com o do tipo A, mas trocado. Ou seja, consideramos o valor somado aos gastos com o tipo B
                dfs(c, a, b + presente[c])
            
            # Para cada cota de gastos que tivemos com a cidade, verificamos todas as cidades que podemos visitar a partir dela
            for i in range(n):
                if grafo[c][i]:
                    dfs(i, a, b)  # Consideramos os gastos atuais com A e B, apenas troccamos de cidade

if __name__ == "__main__":
    matrix = [[[0 for _ in range(128)] for _ in range(128)] for _ in range(32)]  
    # Matriz que guarda os valores de cada uma das rotas
    # As linhas representam as cidades
    # As colunas representam os gastos com presentes do tipo A
    # A terceira dimensão da matriz, que seria a posição do vetor armazenado em cada posição da matriz, indica os gastos com presentes do tipo B
    # Por exemplo, na posição [1][9][8], temos que na cidade 1, gastamos 9 com presentes do tipo A e 8 com presentes do tipo B, se o valor armazenado nessa posição for 1
    
    grafo = [[0 for _ in range(32)] for _ in range(32)]
    # Grafo que representa a interligação entre as cidades
    # Cada linha e cada coluna é uma cidade 
    # A linha indica a cidade que nos referimos
    # A coluna indica as cidades que a cidade daquela linha pode visitar
    
    presente = [0 for _ in range(32)]
    # Valor do presente de cada cidade
    
    sinal = [0 for _ in range(32)]
    # Tipo do presente de cada cidade
    
    n = int(input())  # número de cidades
    t = int(input())  # dinheiro máximo que o sacoleiro possui para gastar
    
    for i in range(n):
        entrada = input().split()  # recebemos a entrada como um vetor
        
        idc = int(entrada[0])  # íncide que representa a cidade -> É inútil nesse caso, pois consideramos que as cidades serão colocadas em ordem
        presente[i] = int(entrada[1])  # guardamos o presente da cidade i
        
        tipo = entrada[2]  # O tipo da cidade A ou B
        sinal[i] = convert_to_number(tipo)  # Convertemos para 0 se for A e 1 se for B, facilitando análises futuras
        
        nv = int(entrada[3])  # Indica quantas cidades podem ser visitadas a partir da cidade i 
        
        for j in range(4, 4 + nv):
            v = int(entrada[j])  # cidade que pode ser visitada pela cidade i
            grafo[i][v] = 1  # guardamos no grafo, em que a coluna guardada é o número que representa a cidade e a linha é a cidade atual 

    dfs(0, 0, 0)  # chamamos a busca em profundidade
    
    r = 128  # variavel de inicialização, já que nenhuma diferença pode ser maior que 100
    
    for i in range(n):
        for j in range(128):
            for k in range(128): 
                # Verificamos o valor de cada posição
                # Fazemos três testes:
                    # Se a posição não é a primeira coluna, na sua primeira posição
                    # Se o valor naquela posição é diferente de 0, ou seja, igual a 1
                    # Se o valor que consideramos como a menor diferença, é maior que a diferença entre a coluna j e a posição k, já que essa diferença denota a diferença de gastos com A e B
                if j + k > 0 and matrix[i][j][k] and r > abs(j - k):
                    r = abs(j - k)  # recemos a menor diferença se esse for o caso
    print(r)  # imprimimos a menor diferença
    
    