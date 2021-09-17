[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Para esse problema, podemos pensar em uma solução gulosa. A ideia é que quando resolvemos um pino da fechadura, ele não será mais "tocado". Então, iniciando do primeiro pino, fazemos as modificações necessárias para ele ficar na posição certa e modificamos o seu vizinho. Passamos para o seu vizinho ao lado e fazemos a mesma coisa, sucessivamente, até o penúltimo. 
Isso funciona porque, ao arrumar um pino, não existe situação que faça sentido modificá-lo novamente e ter menos modificações totais, pois ele já está pronto. 

# Análise do Algoritmo
O algoritmo tem tempo de execução O(n), pois verificamos n - 1 pinos. 