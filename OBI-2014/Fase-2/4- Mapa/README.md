[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia que eu utilizei para resolver o problema, é de que podemos agrupar os pares que se conectam sem nenhuma rua importante. Ou seja, são pares que se conectam apenas com arestas de valor 0. 
O que acontece é que isso cria vários grupos, e a única conexão entre esses grupos são as ruas importantes. Ou seja, partindo de qualquer elemento de um grupo para chegar a qualquer elemento de outro grupo, passamos por uma rua importante.
Temos aí a lógica para encontrar todos os pares que precisam de uma rua importante para se conectarem. 
Só que não precisamos verificar par por par, mas sim analisar grupo por grupo. Se um grupo possuí "a" elementos, e outro grupo "b" elementos, então o número de pares possíveis é a x b, calculando assim em tempo constante para um par de grupo. 
A ideia então é sempre pensar como se fossem dois grupos na hroa do cálculo, apesar de existirem diversos. Calculamos quantos pares existem entre o grupo "a" e todos os outros elementos que não está em "a". Depois, quantos pares existem entre  grupo "b" e todos os outros? Não, porque os pares entre os elementos do grupo "b" e "a" já foram contados, então temos que subtrair o número de elementos de "a" para realizar a multiplicação. Fazemos isso para cada grupo e depois somamos, chegando então no resultado do número de pares. 

# Análise do Algoritmo
No algoritmo, para formar os grupos fazemos isso em O(n), pois visitamos cada aresta exatamente uma vez, e existem n - 1 arestas. Após, fazemos o cálculo de pares dos grupos, que também leva O(n), já que verificamos cada grupo, e existem n grupos, com uma conta de tempo constante. Assim, a solução leva O(n). 