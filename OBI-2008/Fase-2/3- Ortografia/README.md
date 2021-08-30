[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos avaliar para cada palavra se ela corresponde à alguma palavra em um dicionário de palavras.

O ponto maior é: como avaliar se é possível transformar uma palavra dada em uma palavra do dicionário. 

Para isso, podemos pensar em programação dinâmica, em que consideramos LS linhas com LT colunas, sendo LS o tamanho da palavra dada e LT a palavra no dicionário que estamos procurando.  
A primeira linha é preenchida com valor da coluna, e o da primeira coluna com o valor da linha e os restantes valem 0, exemplo:

[0, 1, 2]
[1, 0, 0]
[2, 0, 0]

E que informação que essa tabela passa? A linha informa quantos caracteres foram considerados da palavra informada e a coluna quantos caracteres da palavra do dicionário, e o valor armazenado indica quantas alterações foram feitas. 

Depois, verificamos o valor de cada posição nessa matriz, verificando da primeira linha para a última e da primeira coluna para a última. O valor de cada posição é o valor mínimo da escolha de cada uma das três operações dada pelo enunciado: 
- remoção: retiramos um caracter da palavra dada, então consideramos o número de alterações pelo caracter anterior e somamos um, já que acabamos de fazer a alteração de remoção. 
- inserção: adicionamos um caracter na palavra dada, isso significa que temos que a quantidade de alterações é o número de alterações que ocorreram com um caracter a menos do dicionário, mais um, já que realizamos a alteração de adição. 
- troca: nesse caso temos que considerar a situação com um caracter a menos tanto para a palavra do dicionário, quanto para a palavra dada. Assim, se os dois "atuais" caracteres forem iguais, nada muda, se eles forem diferentes ocorre a soma de uma mudança que foi feita. 

Na última posição, teremos considerado todos os caracteres, e então podemos afirmar se é possível ou não a correpondência entre as duas palavras. 


# Análise do Algoritmo
O algoritmo é executado: O(M N LS LT), como M e N são bem maiores que LS e LT, podemos resumir o tempo para: O(MN)