[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Para resolver esse problema, podemos pensar que temos que encontrar os dois extremos do grafo e então calcular a distância entre eles. 

Encontrar o primeiro extremo é possível fazendo uma busca em largura, partindo de qualquer ponto arbitrário, o lugar mais distante certamente é um extremo. Agora, em posse do primeiro extremo, basta fazer uma busca em largura novamente, mas partindo do primeiro extremo, que certamente chegaremos no segundo extremo, pois é o lugar mais distante possível de se alcançar do primeiro extremo. 

# Análise do Algoritmo
O algoritmo executa duas vezes uma BST, como ela visita cada elemento exatamente uma vez e verificamos cada aresta exatamente uma vez, seu tempo de execução é O(n + n), simplificadamente O(n). 