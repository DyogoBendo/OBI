[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A lógica para resolver esse problema é se perceber que todas as somas devem ser iguais a da diagonal principal. Além do mais, que a "distância" entre os valores entre duas colunas, em qualquer linha, precisa ser sempre o mesmo. Então, por exemplo, se escolhermos a linha 1 e sibtrairmos o valor na linha 1 coluna 3 pelo valor na linha 1 coluna 2, ele precisa ser o mesmo que o valor na linha 2 coluna 3 pelo valor na linha 2 coluna 2. 

Então, para resolver esse problema, precisamos construir com um padrão de distância, e o mais fácil de todos é a distância 1. Então começamos em 0, e vamos somando 1, preenchendo cada linha. Assim, ao final, a distância de valor de cada coluna é 1. 

No entanto, a soma da diagonal principal pode não estar correta. Se tivermos um valor maior que pedido, temos que diminuir a soma. Então, alteramos a primeira linha, pois assim teremos números negativos, de forma a não ocorrer repetições, subtraindo todos os números pelo mesmo, a quantidade que a nossa soma é maior que a esperada. Assim, mantemos o valor da distância entre eles igual, pois estamos somando o mesmo valor a todos. 
Se for menor, então somamos na última linha o quanto falta em cada elemento, garantindo assim também que não ocorram repetições, pois serão gerados apenas valores maiores dos que já existiam. 

# Análise do Algoritmo
Como precisamos criar o quadrado e cada um dos valores dentro dele, o tempo de execução do algoritmo é O(n^2). 