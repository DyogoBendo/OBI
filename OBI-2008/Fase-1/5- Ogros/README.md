[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O problema consiste em encontrar, para cada ogro, qual sua devida posição, dada uma faixa de valores de força e a força do ogro. Isso é um problema de encontrar um elemento em uma lista ordenada, e para fazer isso, é possível usar uma busca binária. 

Determinamos a posição dos ogros sempre pensando na posição do próximo elemento menos um, o que significa que a posição de um ogro é sempre anterior à primeira posição maior que a dele, o que faz sentidi. Se não houver elemento, ele é a última posição da lista. 

# Análise do Algoritmo
O algoritmo é uma busca binária executada para M ogros buscando numa lista de N valores, logo, o tempo de execução é O(M log N)