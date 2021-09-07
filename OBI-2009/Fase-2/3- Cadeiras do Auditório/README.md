[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos descobrir o menor número de movimentos para se voltar a configuração inicial. 

Para a configuração que recebemos, só pode ser mudado linhas com linhas e colunas com colunas. Isso significa que em qualquer linha que pegarmos, nunca teremos dois números que precisam estar na mesma coluna: cada número pertence a uma coluna diferente. E o mesmo vale para o inverso: para qualquer coluna que escolhermos, nenhum número pertence a mesma linha. Pois para isso, seria necessário trocar uma linha com coluna, o que não é possível. 

Tendo isso em mente, podemos verificar quais trocas de colunas são necessárias na primeira linha, e essas são as trocas de colunas necessárias para todo o problema. Assim como podemos verificar a troca de linhas na primeira coluna, e assim resolver o problema. 

# Análise do Algoritmo
O algoritmo é dominado pelo tempo de leitura das entradas, então o tempo de execução é O(MN). 
