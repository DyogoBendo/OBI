[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O que podemos utilizar para resolver esse problema é uma fila de prioridade. Nessa fila, inserimos apenas as tarefas que não dependem de ninguém para serem executados, e será retirado cada vez quem tem maior prioridade. 

O ponto é como determinar quais elementos não dependem de ninguém, e quando um elemento é executado, determinar quais que antes dependiam dessa tarefa que agora estão livres para serem executados.

O que podemos fazer é guardar em cada um quantas tarefas ele depende. Além do mais, guardamos na tarefa quais tarefas depende dela. Assim, verificamos se a quantidade de tarefas que ele depende é 0, se for, pode ser adicionado na fila. Quando uma tarefa é executada, reduzimos em um cada uma das tarefas que dependem dela, e verificamos se agora dependem de 0 tarefas, e então adicionamos na fila. 

# Análise do Algoritmo
O que fazemos é verificar cada tarefa no máximo uma vez, e cada uma das relações cada uma vez. Então, o tempo do algoritmo é exutado no tempo O(N + M). 