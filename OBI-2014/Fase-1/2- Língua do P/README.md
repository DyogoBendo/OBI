[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, podemos observar que cada palavra da frase começa com "p". Pois o "p" antecede cada letra que temos. Por isso, a ideia é separar as palavras da frase, e dentro de cada palavra, iniciamos da segunda letra e pulamos de 2 em 2, ignorando assim os "p"s. 

# Análise do Algoritmo
Como verificamos cada um dos caracteres da frase verdadeira, podemos pensar que o tempo é O(n), sendo n o número de caracteres. 