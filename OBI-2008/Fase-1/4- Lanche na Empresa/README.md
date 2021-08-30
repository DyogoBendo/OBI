[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
No problema, precisamos encontrar a sala que tem a "sala mais distante mais próxima". Bom, podemos pensar que cada sala é um vértice de um grafo, e os corredores são arestas. Assim, bastan calcularmos as distância de cada sala uma em relação a outra, e definir a partir de qual se tem o menor valor máximo. 

Para fazer isso, usamos o algoritmo de Floyd-Warshall, em que conseguimos calcular a distância de todas as arestas quando se parte de cada uma das arestas, e depois, basta verificar em qual o maior valor é o menor de todos. 

# Análise do Algoritmo
O algoritmo é dominado pelo algoritmo de Floyd-Warshall, que tem tempo de execução O(n^3)
