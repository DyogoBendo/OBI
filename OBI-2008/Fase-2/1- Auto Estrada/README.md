[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
No problema, precisamos calcular a quantidade de painéis em uma pista, e de acordo com o que é cada trecho da pista, a quantidade de painéis necessários muda. 

Para resolver, basta verificar qual é o tipo de trecho, e somar de à quantidade total de painéis os painéis necessários para aquele trecho. 

# Análise do Algoritmo
O algoritmo é executado C vezes, pois verificamos cada caracter que representa um trecho de pista a qual valor ele se refere, logo ele é O(C). 