[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Para esse problema, o que podemos pensar é que duas dimensões do colchão precisam passar na porta, já que a porta só tem duas dimensões. Pegamos então as duas menores dimensões do colchão e comparamos com as duas dimensões da porta. 

A menor dimensão do colchão tem que ser menor ou igual a menor dimensão da porta, pois se for maior, então significa que nenhuma entra dimensão passaria também. E verificamos a segunda menor dimensão do colchão com a maior dimensão da porta, na mesma lógica. 

# Análise do Algoritmo

Como são feitas apenas verificações o tempo de execução é O(1).