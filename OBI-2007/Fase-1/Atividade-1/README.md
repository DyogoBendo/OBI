[Formatação utilizada](https://katex.org/docs/supported.html)

# Análise do Problema
Segundo o enunciado, é necessário calcular quantos pedaços serão armazenados, depois de todas as divisões. 

Ainda no enunciado, é dito que, para cada divisão, é escolhido um pedaço, e o restante é guardado. 

Sendo assim, por indução, cheguei na seguinte constatação: 
- Para uma barra dividida em dois pedaços, um é guardado e outro é dividido novamente
- Para uma barra dividida em 5 pedaços, 4 pedaços são guardados, e um é usado. 
- Para uma barra dividida em n pedaços, n - 1 pedaços são guardados, e um é usado. 

Sempre que dividimos uma barra, e escolhemos um pedaço para ser dividido novamente, é um pedaço a menos que deixa de ser guardado, mas que se tornam vários outros, e dentre os que se tornou, um deixará de ser guardado também. 

Por exemplo, se dividimos em 4 partes, guardamos 3, e depois dividimos em 5 partes, guardamos 4: assim temos 3 + 4 pedaços guardados. 

Usando essa lógica para o algoritmo, temos que o resultado será dado por:

$$
\displaystyle\sum_{i=1}^n (a_{i} - 1)
$$

- n a quantidade de divisões que serão feitas, 
- a represente em quantas partes cada divisão deixará o chocolate


# Análise do Algoritmo

- As linhas 1 e 2 possuem tempo constante
- A linha 3 possui uma função que é executada n vezes. 
- A linha 4 é constante
- A linha 6 é executada n + 1 vezes
- A linha 7 é executada n vezes
- A linha 9 possui tempo constante

O tempo de execução do nosso algoritmo pode ser tanto por: 3n + d, sendo d uma constante qualquer. 

Consideramos então O(n) como um limite assintótico do algoritmo: 

3n = O(n)
3n <= cn

3n <= 4n  -> temos então que que c é igual a 4, para qualquer n. 

(a escolha foi pelo 4 para ficar mais claro, mas poderia ser qualquer c >= 3)

Para verificarmos que o loop é verdadeiro, utilizamos o conceito de loop invariante: 

O que consideraremos como invariante no loop será: 

$$
resultado = \displaystyle\sum_{i=1}^n (a_{i} - 1)
$$

A variável 'resultado' armazena a soma de pedaços não utilizados em cada divisão

- Inicialização: Antes da primeira iteração, temos que n = 0, então a somatória também é 0. 

- Manutenção: a cada iteração, é somado o número de partes que o chocolate foi dividido - 1 ao somatório de todas os chocolates que já foram armazenados. 

- Término: ao final da iteração, temos n é igual ao total de divisões que devem ser realizadas. Assim, temos a soma de todas as barras que foram armazenadas, atendendo ao que foi pedido no enunciado. 


# [Análise de Tempo](https://www.inf.ufpr.br/maratona/tle.html)
Consideramos a entrada de maior caso 1000, de forma geral, temos que:

O computador executa 10 ^ 7 ações por segundo. Podemos pensar em algumas funções que são aceitáveis para essa sentrada: 

$$
f(10^3) <= 10^7 
$$

A função pensada na resolução é uma função linear, então: 

$$
f(x) = x -> f(10^ 3) = 10 ^ 3
$$

Sabemos então que:

$$
10 ^ 3 < 10 ^ 7
$$

Logo, podemos precisar que o algoritmo atende a necessidade de tempo. 