[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos encontrar a sequência de pedações de pizza que contém a maior quantidade de cebolas retirando a quantidade de azeitonas. O que é informado é apenas o resultado de diferença de quantidade de cebolas e azeitonas em uma fatia, assim, se existem 5 cebolas e 4 azeitonas em uma fatia, o valor daquela fatia é 1. 

Assim, o que de fato precisamos encontrar é a subsequência máxima de fatias. No entanto, existe um fator importante a ser considerado: a pizza é um círculo. Isso significa que a última fatia é vizinha da primeira. 

Uma solução seria calcular a maior subsequência tendo como início cada uma das fatias, e escolhemos a sunsequência de maior valor. 

Agora, como podemos realizar o cálculo da maior subsequência partindo de uma fatia? Podemos considerar a maior soma anterior àquela fatia ou que a considera e somarmos com a subsequência que está a frente da fatia. 

Imaginamos a seguinte sequência de fatias: [5, -3, -3, 2, -1, 3]

Temos que a soma até cada elemento é: [5, 2, -1, 1, 0, 3]
E a "melhor soma" anterior que pode incluir a fatia é: [5, 5, 5, 5, 5, 5], já que a "melhor soma" é justamente o 5, que é o primeiro elemento. 

Agora, como a pizza é um círculo, nós verificamos de cada fatia qual seria o resultado se partíssemos dela, fossemos para a frente, dando a volta e chegando na sua "melhor soma". 
A fim de ficar mais claro, vamos verificar cada uma das fatias do exemplo acima:
- 1: a maior soma é 5 e a soma dos seus elementos posteriores é -2, então se fizéssemos o caminho: -3 -> -3 -> 2 -> -1 -> 3 -> 5, o custo total seria o 3, que é o custo de chegar na "melhor soma" partindo do caminho após o número, e a "melhor soma" em si. 
- 2: a maior soma é 5 e a soma dos elementos posteriores é 1, o caminho seria: -3 -> 2 -> -1 -> 3 -> 5, que teria soma 6. 
- 3: a maior soma é 5 e a soma dos elementos posteriores é 4, o caminho seria: 2 -> -1 -> 3 -> 5, essa é a nossa solução ótima, e tem soma 9
- 4: a maior soma é 5 e a soma dos elementos posteriores é 2, o caminho seria: -1 -> 3 -> 5 e tem soma 7
- 5: a maior soma é 5 e a soma dos elementos posteriores é 3, o caminho seria: 3 -> 5 e tem soma 8

Dessa forma, sempre conseguimos encontrar a melhor soma quando ela "dá a volta". No entanto, precisamos ainda considerar o caso de quando isso não ocorre, por exemplo, se tivéssemos esse conjunto de fatias: [-2, -4, 5, 6, -2], é fácil perceber que a maior soma possível é 11, somando 5 e 6, e que eles não "dão a volta". 

Para fazer essa verificação, basta perceber que a maior soma contínua possível nunca inicia em um número negativo e sim sempre em um positivo. Então podemos ir somando os números, verificar se a soma é maior que a máxima, e também verificar se ela se tornou negativa, quando ela for negativa, basta iniciarmos uma nova soma no primeiro elemento após o elemento que tornou a soma negativa.

Então no algoritmo, precisamos considerar apenas esses dois casos: quando dá e quando não dá  a volta na pizza. 

# Análise do Algoritmo