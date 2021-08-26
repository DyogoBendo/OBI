[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Precisamos converter caracteres para dígitos. Se os caracteres já forem digitos, eles ficam como estão. Então só precisamos fazer um mapeamento, para quando aparecer uma letra, colocarmos o número que ela representa. 

# Análise do Algoritmo
Para cada letra, verificamos se elas estão em cada um dos conjuntos. Como ao todo existem 26 letras, temos que para cada caracter podemos executar 26 verificações. Então o em tese o teto de execução seria O(c), sendo c o número de caractéres, mas como são apenas 15 caracteres no máximo, podemos considerar que a solução vai ter tempo constante para todos os casos de teste. 
