[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, podemos observar que existe uma subestrutura. Vamos analisar o porquê. 
Se pegarmos o valor 22, podemos usar uma nota de 20, e agora, o problema se tornou de quantas formas podemos dar o valor 2. Se usarmos uma nota de 10, o problema se torna de quantas formas diferentes podemos dar o valor 12. Assim, ao usar uma nota, se torna um subproblema, no qual a sua solução é a solução para o problema principal. 

Iniciamos com um vetor que é 0 em todas as posições, menos na posição 0, pois nela temos uma opção "calculada": não devolver nada. Podemos então pensar na solução de cima para baixo, começando das notas de maior valor, verificando para cada valor até 0, em cada subtração possível pela nota que estamos avaliando agora neste valor, quantas possibilidades existem. No exemplo do 22, a maior nota que avaliamos é 20, e quando fazemos 22 - 20, avaliamos quantas possibilidades existem com o valor 2, que é inicialmente 0. No entanto, quando avaliamos o valor 20 - 20, o resultado é 0, então como existe uma possibilidade para 0, então existe uma possibilidade para 20. 
Continuamos fazendo isso até o final, ou seja, até avaliar todos os valores para a nota 2. Antes, o 22 - 20 deu 0 possibilidades, porque quando chegamos no 2 que calculamos esse caso, pois fazemos 22 - 2, caindo no caso 20, e em 20 temos a possibilidade calculada para a nota 20, e pelas outras notas também. 

# Análise do Algoritmo
O algoritmo verifica, para cada nota, cada valor entre 0 e S, cada uma das subtrações desse valor pela nota até ser 0 ou se esgotar a quantidade de notas, assim, simplificandamente, podemos pensar que a solução tem tempo O(SN), sendo N a quantidade máxima de cada nota. 
