[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia é pensar no problema como um grafo. Partimos de um ponto inicial e queremos chegar em outro, e vamos verificar cada uma das "arestas" desse grafo, que seriam cada uma das posições.  Só podemos passar de uma posição para a outra se o valor for adequado, como dito no enunciado. 

Então, podemos calcular a distância de um ponto para outro verificando sempre a distância de um ponto já calculado até aos de que ainda não foram calculados.

Um problema é que não necessariamente temos que sempre acessar uma posição a cada rodada, e podemos esperar uma para que os números mudem. Para lidar com isso, podemos pensar em armazenar a distância não só em relação à posição do ponto, mas também em qual valor ele possuía quando foi acessado.

A maneira com que podemos calcular a distância de cada um dos pontos é usando uma bst, pois assim calculamos todos os vizinhos de um ponto já calculado, e só então partimos para "os vizinhos dos vizinhos", pois como a única distância que conhecemos inicialmente é a posição inicial, a menor distância em relação a todos os pontos sempre vai ser em relação a essa distância inicial.  

Temos então que checar a cada posição, cada uma das suas cinco possibilidades: ir para direita, para cima, para esquerda, para baixo, ou ficar parado, e então depois para cada uma dessas possibilidades, chegar cada uma dessas possibilidades, e assim sucessivamente, até termos testado todas as possibilidades


# Análise do Algoritmo

O algoritmo testa exaustivamente cada uma das possibilidades. Assim, no pior caso, testamos todas as posições da matriz tridimensional das distâncias. Sendo assim, o tempo da solução é dominada pela função bfs, mais precisamente pelo loop que encerra apenas quando todos as possibilidades forem checadas, que é O(10NM), já que verificamos cada posição, que é NxM (número de linhas e colunas) 10 vezes, assim podemos dizer que o algoritmo é O(NM)