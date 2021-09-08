[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, temos que fazer duas coisas: agrupar os barcos e depois descobrir quais são destruídos. 
Para agrupar os barcos, podemos fazer isso de forma recursiva: verificamos cada posição do tabuleiro, se ali encontrarmos uma posição que é de um barco e ele não pertencer a nenhum grupo ainda, então procuramos em todos os seus vizinhos, se existem mais "pedaços de barcos" que não pertencem a nenhum grupo, até não existir mais nenhum vizinho que atenda a esse requisito. 

Depois, para olhar se eles são destruídos, basta verificar se as posições passadas levam a um pedaço de barco. Se sim, verificamos se o grupo que ele pertence é unitário, ou seja, só contém ele. Se for, então temos um barco destruído, senão, temos um barco de tamanho menor apenas. 

# Análise do Algoritmo
O que fazemos no algoritmo de maior tempo são as chamadas recursivas. Só que elas tem o limite do tamanho do tabuleiro, já que verificamos cada posição do tabuleiro apenas uma vez. Assim, o tempo de execução do algoritmo é O(MN)