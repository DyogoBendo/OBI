[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos analisar se é possível chegar do ponto de entrada até o ponto de saída, e se for, qual a menor distância para isso. 
É fácil perceber que se trata de um problema com grafo, já que é nítida a existência de arestas e vértices. Como as arestas são todas de mesmo tamanho, então poderíamos fazer uma busca em largura, e teríamos o resultado. 

No entanto, essa busca em largura não pode ser concenvional, porque existe um outro elemento: podemos chegar em um mesmo vértice, a partir da mesma aresta, mas em momentos diferentes, então temos essa outra dimensão para se analisar. Assim, fazemos a busca em largura, verificando também em que momento estamos chegando em cada vértice. Verificamos apenas a primeira vez, pois por se tratar de uma BFS, a primeira visita é sempre a de menor custo. 
Sendo que a profundidade irá nos informar justamente o tempo que demoramos para chegar em um certo vértice. 


# Análise do Algoritmo
Como verificamos para cada aresta em três situações diferentes, nosso tempo de execução é igual ao de uma BFS comum, por se tratar de um tamanho constante a mais de visitas feita. Porém, para criar todos os possíveis valores, usamos uma tabela, e o tempo de execução é dominada por ela: O(n^2), enquanto a bfs tem tempo de execução O(n + m). 