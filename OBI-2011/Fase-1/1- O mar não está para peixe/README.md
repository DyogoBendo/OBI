[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia de solução do problema é que podemos representar o mar como uma matriz, em que as linhas representam as coordenadas x e as colunas representam as coordenadas y, já que os valores são apenas números naturais. 

Dada as coordenadas dos retângulos, podemos marcar quais desses pontos de coordenadas eles cobrem. Então, se o retângulo inicia em (1, 1) e termina em (3, 3), vamos marcar todos os pontos que estão nessa área: (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3). Se observarmos, o número de pontos é exatamente 9, que é exatamente a área. Porque se pensarmos, temos 3 pontos em cada linha, e temos 3 linhas, então o valor é exatamente 9, e é exatamente o que o conceito de área representa. 

# Análise do Algoritmo
Temos dois loops aninhados diferentes no nosso algoritmo. O primeiro depende de n e do tamanho das nossas entradas de x e y, que generalizando no pior caso, são do mesmo tamanho 100. Já no segundo loop, depende apenas do tamanho máximo de x e y, que é 100. 
Então no pior caso, temos que a complexidade do algoritmo é O(n^ 3), apesar de ser improvável que ocorra. E em todo caso, temos O(MAX_SIZE ^ 2), ou seja, garantidamente executamos 10000 vezes o loop interno. 