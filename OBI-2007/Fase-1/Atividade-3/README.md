[Formatação utilizada](https://katex.org/docs/supported.html)

# Análise do Problema

O problema pede para que respondamos se é possível arquivar de forma perfeita a pasta. Para isso, é necessário que: 
- Para um elemento de aba < P, sendo P a maior aba, sempre deve ter um sucessor que tem o seu valor de aba + 1 ou nenhum. 
- Se a aba do elemento for P, então o sucessor deve ser 1 ou nenhum
- Todos os elementos devem ser armazenados. 

Segundo o enunciado, a sequência deve sempre iniciar pelo 1, então temos como exemplo a sequência: 

- 1, 2, 3, 4, 1, 2, 3, 4

Pensemos em algumas proposições que quando uma sequência é valida: 

- O número 1 nunca aparecerá em menor quantidade que outro número 

É simples essa ideia: se o número 1 aparece menos que os outros números, por exemplo (1, 2, 2, 3, 4): 

- 1, 2, 3, 4, ..., 2

Não consiguiriamos utilizar todos os números, pois, nesse caso, "falta um 1", para que a sequência possa ser completa. 

- As sequência são repetições, e podemos analisar apenas o caso base

Por exemplo, se temos (1, 1, 2, 2, 3, 3, 4, 4):

- 1, 2, 3, 4, 1, 2, 3, 4

Temos nesse caso, uma repetição da sequência (1, 2, 3, 4) duas vezes, que é a quantidade de vezes que aparece cada um dos números (2 vezes). 

E para qualquer sequência, repetimos o número de vezes os elementos, até chegarmos no momento em que um dos elementos é igual a 0 ou todos são iguais a 1. Por exemplo, na sequência (1, 1, 2, 3, 4, 4): 

- Realizamos 1x: 1, 2, 3, 4 
- Agora temos: 1, 3, 4

Precisamos analisar apenas essa última sequência, e percebemos como é uma sequência inválida. 

Assim, para todo caso, basta reduzirmos ao caso básico, e analisar se ele é possível. Para reduzir ao caso básico, podemos simplesmente ver quantas vezes cada número aparece. O número que menos aparece, representa quando a sequência acaba. Por exemplo: (1, 1, 1, 2,2, 2, 3, 3, 4, 4, 4), nesse caso, o número 3 aparece 2 vezes, assim, temos que a retiramos 2 da quantidade de vezes que cada número repetiu: 

1 = 3 - 2 -> 1
2 = 3 - 2 -> 1
3 = 2 - 2 -> 0
4 = 3 - 2 -> 1

Temos então a sequência formada apenas pelos que apresentam alguma quantia: 1, 2, 4 e precisamos analisar apenas ela para saber se a situação é válida. 

- Uma situação só é válida se, no seu caso básico, temos uma sequência sem 0 entre dois 1: 

Utilizando o exemplo acima, a sequência ficou: 1, 1, 0, 1 

Como temos um 0 entre dois 1, a sequência é inválida. 

- Se no caso básico, houver algum número superior a 1, a sequência é inválida

Pensando em um exemplo (1, 1, 2, 2, 2, 2, 3, 3, 4, 4): 

1 = 2 - 2 -> 0
2 = 4 - 2 -> 2
3 = 2 - 2 -> 0
4 = 2 - 2 -> 0

Temos a sequência formada por: 0, 2, 0, 0, e não tem como encaixar dois 2 nessa situação. 

## Resumindo

Temos que uma sequência é válida apenas quando: 

- A sequência base (a sequência de quando a quantidade de uma das posições é 0), tem uma sequência sem "furos", de 1. 


