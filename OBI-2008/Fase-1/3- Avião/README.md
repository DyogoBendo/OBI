[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Precisamos saber em que fileira e em qual coluna Zuki irá sentar. 

Vamos considerar F fileiras e C colunas em cada fileira. Dado quando Zuki comprou a passagem basta pensarmos que para preencher a primeira fileira é necessário C pessoas terem comprado passagem antes de Zuki, para a segunda é necessário 2 * C pessoas terem comprada passagens, e assim por diante. Então Zuki estará na fileira que é o número de passageiros que tem na frente dele dividido pela quantidade de pessoas que precisa pra encher uma fileira, no caso C e isso é somado com a fileira que se inicia a classe econômica. 

A coluna que ele se sentará é justamente o resto da divisão do número de passageiros pelo número de colunas, pois são os passageiros que ainda não estão em nenhuma "fileira fechada", e que sobraram para a fileira que o Zuki irá se sentar. 

Para verificar se ele caberá no avião, basta saber se a fileira que ele entrará é menor ou igual ao número de fileiras que existem no avião. 

# Análise do Algoritmo

A solução é em tempo constante O(1), pois só precisamos calcular divisão e restos. 