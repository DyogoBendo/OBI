[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O que podemos usar nesse problema, é verificar cada caracter em cada linha. Quando for "{", significa que está abrindo chaves, e "}", um fechamento. Se quando um "}" for encontrado, e não houver "{" para fechar, então isso significa um erro. Agora, se terminarmos com uma quantia de "{" maior que de "}", também significa um erro de falta de fechamento. 

# Análise do Algoritmo
O algoritmo tem tempo de execução O(nc), sendo n o número de linhas e c o número de caracteres de cada linha. 