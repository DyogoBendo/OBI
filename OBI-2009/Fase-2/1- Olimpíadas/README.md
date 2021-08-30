[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, o que precisamos é ordenar os países pela ordem de medalhas de ouro, depois de prata e depois de bronze.
Para isso, basta usar a função embutida do python de ordenação de listas, informando justamente essa ordem de comparação. 


# Análise do Algoritmo
Como dependemos de uma função embutida do Python (Timsort), o tempo de execução é muito otimizado, e é próximo de O(n) na maioria dos casos, apesar do tempo ser O(n log n)