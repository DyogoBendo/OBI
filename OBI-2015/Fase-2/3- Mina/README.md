[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia da resolução desse problema é pensar na matriz como um grafo, e que o custo das arestas que ligam os pontos adjacentes é o valor 0 se não tiver nenhum empecilho e 1 se houver. 

Sendo assim, para encontrar o menor caminho do ponto inicial ao ponto final, basta usarmos o conceito do algoritmo de Dijkstra. 

# Análise do Algoritmo
Como verificamos cada ponto uma vez, o loop é executado n^2 vezes. Dentro do loop, extraimos o elemento de maior prioridade em tempo constante, verificamos cada uma das 4 posições adjacentes, executando assim 4 vezes, em que cada uma delas inserimos um elemento no tempo O(log n), no heap. Assim, o tempo de execução é O(n^2 log n)