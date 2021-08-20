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

# Análise do Algoritmo

- Linhas 2 a 5 são constantes
- Linha 6 é executada n + 1 vezes
- Linhas 7 e 8 são executadas n vezes
- Linhas 9 a 15 são constantes
- Linha 16 executada n vezes, no pior caso
- Linhas 17 a 32 executadas n - 1 vezes, no pior caso 

P.S: O pior caso considerado aqui é quando a sequência é válida, então devemos iterar por todos os elementos

- Linhas 35 a 38 constantes

Somando todas as linhas, temos, aproximadamente: n + 1 + 2 (n) + n + 15 (n - 1) + c, sendo c uma constante qualquer

Temos então: 19n - 14 

Como se trata de um polinômio, podemos considerar simplesmente que: 

19n - 14 = O(n)

Tratamos então que esse algoritmo é linear. 

Analisando o loop invariante das linhas 16 a 32: 

- Consideramos como invariante que uma sequência é válida se S[0, ..., i - 1]:
    - Não apresentar nenhum "furo" 
    - Não apresentar nenhum valor maior que 1

- Inicialização: nesse momento, temos a sequência com um elemento. Nesse caso, temos certeza que o anterior não é 0 e ele 1, pois não há anterior. O único problema é se ele possui um valor > 1, mas dentro da iteração, ocorre essa verificação. 

- Manutenção: a cada iteração, aumentamos em um essa sequência, e verificamos na iteração se ela é válida. Caso não seja, o loop é encerrado

- Término: após todas as iterações temos: i = n, então a sequência é [0, ..., n - 1]. Podemos afirmar que não há nenhum dos problemas anteriores, pois se houvesse, a sequência teria sido encerrada antes. 


# [Análise de Tempo](https://www.inf.ufpr.br/maratona/tle.html)

A entrada contém:

 $$ 
 n <=  1.000.000 = 10 ^ 6
 $$

 Verificamos a validade de nosso algoritmo: 

 $$
f(n) = n 
 $$

 $$
f(10 ^ 6) = 10 ^ 6 <  10 ^ 7
 $$

No entanto, por algum motivo, esse código falha nos casos de testes, pois demora mais de 1 segundo para ler 1000000 dados. 




