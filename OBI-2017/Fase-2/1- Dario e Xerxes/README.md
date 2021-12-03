[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia usada aqui, é que um número 'A' sempre ganha de um número 'B' quando ele está 1 ou 2 valores à frente. Como existem apenas 5 números, o 4 por exemplo "dá a volta", e ganha do 0 e 1. Por isso, podemos usar essa soma, junto com % 5, pois somando 4 com 2, temos 6, que % 5 dá 1. 

# Análise do Algoritmo
O tempo de execução é dominado pelo loop, que tem tempo O(n). 