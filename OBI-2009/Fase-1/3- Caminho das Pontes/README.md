[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Esse é um problema de grafos, em que podemos pensar nas pontes como arestas e onde elas se conectam os vértices. O peso de cada aresta é determinado pelo número de buracos da ponte. 

O que precisamos fazer é encontrar qual é o menor custo de se sair da posição inicial e chegar na posição final, ou seja, encontrar o caminho mínimo partindo de uma aresta até chegar em outra. 

Para fazer isso, podemos utilizar o algoritmo de Dijkstra. 

# Análise do Algoritmo
Como o algoritmo implementado é o de Dijkstra, o tempo de execução é O(E log V), sendo E o número de arestas e V o número de vértices, no caso do problema, o tempo de execução é O(M log N)