[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Esse problema é claramente associado à uma fila de prioridade mínima. Podemos pensar que cada vendedor começa com uma prioridade 0, a cada ligação que um vendedor atende, sua prioridade diminui pela duração da ligação, assim, quem termina uma ligação primeiro será quem fará a próxima ligação, ou seja, quem tem o menor valor de tempo de ligação acumulado, tem a maior prioridade. 

Sabendo quem faz cada uma das ligações, basta apenas armazenar a quantidade de ligações que cada um realiza. 

# Análise do Algoritmo

O problema é executado O(l log n) já que, para cada ligação, removemos o elemento de maior prioridade do heap, e o adicionamos de volta com o valor da ligação diminuindo sua prioridade, essas duas tarefas são executadas em tempo O(log n)