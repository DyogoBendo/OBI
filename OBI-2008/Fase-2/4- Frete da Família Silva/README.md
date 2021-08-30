[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, devemos avaliar qual a melhor forma de conectar todos as colônias. Isso é um problema de Árvore Geradora Mínima, em que devemos conectar todas os Vértices ao menor custo total de Arestas. 

Para fazer isso, basta implementar o Algoritmo de Prim. 

# Análise do Algoritmo
O algoritmo de Prim, pela forma como foi implementado, tem tempo polinomial de O(n^2), o que é suficiente para resolver a questão. 