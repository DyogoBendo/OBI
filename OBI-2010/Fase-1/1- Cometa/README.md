[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Para esse problema, precisamos encontrar quanto tempo falta para a próxima passagem do cometa. 
Primeiramente, precisamos saber há quantos anos se passou o último cometa. Para isso é simples, pois o cometa sempre passa em múltiplos de 76, a partir de 1986. Ou seja 1986 + 76, 1986 + 2*76...
Sabendo disso, basta subtrair de 76 (o tempo que falta para se passar o próximo cometa) o quanto já se passou do último cometa (o resto do tempo que se passou de 1986 até o ano pediu por 76)
Assim, a próxima passagem será o resultado do ano passado mais o cálculo falado acima. 

# Análise do Algoritmo
Como são feitos apenas cálculos de soma, subtração, etc, podemos dizer que o tempo do algoritmo é O(1). 
