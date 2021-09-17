[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, o que precisamos verificar é, dentro de cada número se eles são válidos. Para isso, temos que verificar se o número, ou pertence à A ou ele é a soma de dois elementos de B. 

# Análise do Algoritmo
Para verificar se o número é a soma de dois elementos em B, demoramos O(m), e como potencialmente podemos fazer isso para todos os m números, temos então que o tempo de execução é O(m^2). 