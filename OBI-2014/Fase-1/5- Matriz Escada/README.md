[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O que fazemos nesse problema é verificar cada linha. Se for a primeira linha ela é sempre válida, já as próximas, devemos verificar se até o valor onde se deve ser 0, se todos os valores são 0. 

A posição em que se deve ser 0 é definida sempre pela linha anterior, que é onde surge o primeiro valor que é diferente de 0. 

# Análise do Algoritmo
Como verificamos cada linha e potencialmente cada coluna, o tempo de execução é O(n^ 2). 