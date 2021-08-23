# Análise do Problema

Esse problema é o mais complexo da primeira fase. É, para mim, foi até de certa forma complicado entender qual seria a solução ideal. Tão difícil, que o que eu fiz foi uma adaptação do código em C que é uma solução do problema, pois não consegui pensar em nada. Farei então a explicação do que eu entendi do código original. 

A ideia principal para resolver esse problema, é pensar em uma matriz de 3 dimensões: 
- A primeira dimensão indica a cidade
- A segunda dimensão indica os gastos com presentes do tipo A
- A terceira dimensão indica gastos com presentes do tipo B
Por exemplo, na posição [1][4][10], temos que na cidade 1, nesse momento da viagem, há um gasto de 4 com presentes do tipo A e 10 com presentes do tipo B 

Outra ideia importante, é que a conexão dos caminhos das diversas cidades é um grafo. A partir desse conceito, podemos percorrer esse grafo, analisando os custos de cada caminho, que serão armazenados nessa matriz. 

Realizamos uma busca em profundidade do grafo, percorrendo cada um de seus caminhos. A cada verificação, preenchemos na cidade um valor de gasto naquele momento. Então, quando visitamos a cidade C, indicamos quanto está sendo gasto na cidade A e na cidade B. Fazemos isso apenas quando não há uma repetição dos valores. Então informamos apenas uma vez aquele custo para a cidade C, evitando entrar em loops infinitos. 

Depois de termos preenchido a matriz com todos os valores gastos, em cada um dos possíveis caminhos (que na verdade, seria cada uma das possibilidades de gasto que uma pessoa pode chegar em uma cidade), iteramos em cada um dos elementos da matriz, e verificamos se a diferença entre gastos com os presentes A e presentes B é a mínima possível. 

# Análise do Algoritmo

Nesse caso, eu não farei uma análise completa, apenas simplificada: 
- Temos que receber os dados, que são n linhas, e cada uma podemos ter que interar m vezes, consideramos n² o tempo para receber todos os dados
- Realizamos a DFS, de forma geral, uma DFS tem tempo linear, já que percorremos cada um dos vértices. Nesse caso, não percorremos cada um dos vértices também, mas analisamos o cada uma das posições da matriz. No pior dos casos, é um algoritmo cúbico
- Verificamos cada uma das posições da matriz para determinar a menor diferença, temos um tempo cúbico 

Assim, temos uma predominância do tempo cúbico, e podemos dizer que o tempo de execução é: 

$$
\Omega(n ^ 3)
$$

# [Análise de Tempo](https://www.inf.ufpr.br/maratona/tle.html)

Como a maior entrada é 100, um algoritmo cúbico é aceitável, já que: 

$$
(10^ 2) ^3 < 10 ^ 7
$$