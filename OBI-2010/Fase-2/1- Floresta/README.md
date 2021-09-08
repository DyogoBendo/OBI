[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A minha solução para esse problema envolve uma equação, em que vamos testar cada valor de y na faixa [2, n//2]. Esse valor de y testado gerá um valor de x. Se x for um valor inteiro, então ele será considerado como um caso válido. 

Quando x for maior que y, significa que estaremos voltando e contando casos que já foram vistos anteriormente, apenas trocando a ordem. Por exemplo (5, 2) e (2, 5). 

A equação surge da seguinte lógica. O número de árvores plantadas é igual à xy + (x-1)(y-1). Isso porque, em cada linha y, são plantadas x árvores de carvalho. E no espaço interior, observamos que eles estão contidos dentro de cada um dos quadrados, sendo a quantidade de quadrados justamente (x-1)(y-1). 

xy + (x-1)(y-1) = n
xy + xy - x - y + 1 = n
2xy - x - y = n - 1
2xy - x = n - 1 + y
x(2y - 1) = n - 1 + x
x = (n - 1 + x) / (2y - 1)

E assim, podemos testar os valores válidos de x, sendo qualquer caso em que essa equação dá um resultado inteiro

# Análise do Algoritmo
O algoritmo é executado no tempo O(n). 