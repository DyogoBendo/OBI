[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O que temos que fazer nesse problema, é encontrar em qual círculo mais interno o dardo está contido. Podemos usar uma busca binárias, já que as distâncias estão ordenadas. 
Se encontrarmos exatamente a distância do dardo em relação ao centro igual a uma circunferência, contamos que o dardo foi acertado nesse círculo. Se o dardo acertou em um valor maior do que o que estamos chegando, verificamos a parte superior, e se for menor, a parte inferior, até que chegarmos ou em uma circunferência, ou em qual é o último círculo antes que i > j ocorra, e então podemos avaliar em qual círculo ele está contido. 

# Análise do Algoritmo
Como para cada dardo, verificamos cada vez dentre os círculos, e essa verificação é feita com um algoritmo de busca binária, temos o tempo de execução: O(t log c)