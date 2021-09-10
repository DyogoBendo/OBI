[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Esse é um problema de árvore geradora mínima, em que podemos utilizar a ideia do Algoritmo de Prim para encontrar o menor custo de conectar todos os pontos. 

# Análise do Algoritmo
Assim como o algoritmo de Prim, visitamos cada uma das cidades exatamente uma vez, e pegamos todas as suas arestas, adicionando a fila de prioridade mínima, em que cad adição custa O(lg n). Logo, o tempo de execução é O(m log n)