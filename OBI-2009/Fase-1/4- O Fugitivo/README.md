[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Precisamos olhar se, em algum momento, o prisioneiro se afasta mais do que é permitido, dado suas coordenadas. 
Nesse caso, basta manter a coordenada dele a cada mudança de posição, e calcular a distância euclidiana dessa posição em relação a posição (0, 0), se ultrapassar o limite imposto, guardamos essa informação. 

# Análise do Algoritmo
O algoritmo é executado no tempo O(N), que é a quantidade de posições passadas, pois precisamos verificar cada uma das posições. 