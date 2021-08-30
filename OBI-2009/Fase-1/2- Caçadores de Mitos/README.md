[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, só precisamos verificar se em alguma momento ocorre a repetição de coordenadas. Basta fazer um matriz em que cada coordenada armazena 0 se nenhum raio caiu ali e 1 se algum raio já caiu. Se um raio cair em uma coordenada que possuí valor 1, significa que dois raios caíram no mesmo lugar. 

# Análise do Algoritmo
O algoritmo tem tempo O(XY) pra criar a lista de coordenadas e O(N) para verificação de cada raio. Então o tempo é O(XY + N), que podemos considerar um algoritmo de tempo linear em relação a N, já que o maior valor de XY é menor que o maior valor de N. 
