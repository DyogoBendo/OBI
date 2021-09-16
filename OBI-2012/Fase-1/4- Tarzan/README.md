[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O que precisamos verificar é uma coisa: se todas as árvores se conectam. O que podemos pensar é que elas são vértices de um grafo, e as arestas ocorrem quando a distância de uma árvore a outra é menor do que a estipulada. 

Para isso, podemos para cada árvore, verificar com quais árvores ela conectam, adicionar essa árvore no grafo, e então verificar as árvores conectadas por essa, até que todas as árvores sejam verificadas. 

# Análise do Algoritmo

Como verificamos para cada árvore todas as outras árvores, o tempo de execução do algoritmo é O(n ^ 2). 