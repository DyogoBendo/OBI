[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Para esse problema podemos pensar que cada abertura precisa de um fechamento. O que é necessário determinar é a ordem dos fechamentos. O primeiro que se fecha é o último que se abriu, então podemos aplicar a lógica de uma pilha da ordem dos elementos que se espera no fechamento. Caso ocorra qualquer problema com a pilha (o elemento não é o esperado, sobraram elementos a serem fechados ou ocorrer a tentativa de fechar um elemento sem ter nenhum aberto), então a cadeia é inválida

# Análise do Algoritmo
O algorimto executada n vezes, pois existem n cadeias, e dentro de cada cadeia, verifica cada um dos caracteres, diremos c caracteres. Então, o algoritmo tem tempo O(nc)