[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Como existe apenas um único caminho até a saída, podemos partir da saída e chegar ao ponto inicial, pois existirá apenas uma forma de se fazer isso, e com certeza estaremos chegando na saída. 
A lógica é verificar qual posição é possível: existe apenas uma posição válida segundo o enunciado, assim, só temos que tomar cuidado em não voltar o caminho. Ao ir para a direita, não podemos na sequência ir para a esquerda, pois estaríamos voltando no mesmo lugar. 

# Análise do Algoritmo
Como potencialmente verificamos todas as posições da matriz, o tempo de execução é O(n^2). 
