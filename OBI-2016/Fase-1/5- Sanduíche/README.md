[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia para resolver o problema surge do fato de que os pedaços são apenas numeros positivos. 

Iniciamos na primeira posição, e vamos somando com os sucessores, até chegar num valor que supere o desejado ou que é igual a ele. Então, agora vamos para a segunda posição, mas não precisamos iniciar a verificação "do 0", pois se no primeiro "estourou" naquela posição, em uma soma que considerava o segundo, o valor naquela posição obrigatoriamente será menor, então ou se torna um valor válido, ou é um valor que podemos somar, avançando a partir dali. 
Fazemos isso até a última posição, encontrando todas as sequências seguidas. 

Agora, para as sequências que "dão volta", em que há uma parte em cada extremidade, podemos verificar a soma partindo do fim ao início, até chegar ou no inicio, ou numa soma que seja maior ou igual ao valor procurado. Agora verificamos posição por posição, partindo do início, e somando com esse valor. Caso o valor seja maior que o procurado, subtraímos, até que ele não seja mais, diminuindo o tamanho da sequência considerada na outra extremidade. 

# Análise do Algoritmo
i e j nunca assumem um valor mais de uma vez, assumindo n valores diferentes, sendo assim, o tempo de execução é O(n). 