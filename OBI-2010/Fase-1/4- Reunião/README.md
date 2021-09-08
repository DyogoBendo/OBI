[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos encontrar a "menor maior distância", ou seja, encontrar partindo de qual cidade, a distância máxima, é a menor possível. 
Para fazer isso, podemos utilizar o algoritmo de Floyd-Warshall, em que encontramos a distância partindo de todos os pontos, e então, verificamos em cada uma qual é seu valor máximo, e se é o menor de todos.

# Análise do Algoritmo
O algoritmo é dominado pelo cálculo da distância de todos os pontos, que leva O(n^3). 