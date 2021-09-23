[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Podemos dividir o problema em dois. Primeiro, pensemos, como encontrar o chefe mais novo. Podemos fazer isso "subindo" no grafo de relações, assim, partindo do empregado dado, manter referência de quem são seus chefes, e ir então verificando seu chefe, os chefes dos seus chefes. Podemos fazer isso facilmente com uma busca em profundidade, mas eu utilizei uma busca em largura, que também atende a necessidade. 

Agora, pensemos em como manter a mesma estrutura, para que possamos fazer a verificação de chefe mais jovem, fazendo as trocas. A ideia é ter uma vetor de posições, que armazena que posição no vetor de empregados aquele empregado referencia. Assim, quando trocamos dois empregados, trocamos as posições que eles referenciam no vetor empregados, assim como a idade que aquela posição de empregados possui. Quando formos fazer a verificação de chefe mais jovem, as idades estarão atualizadas, e a verificaçãos será correta, e em trocas futuras, saberemos onde cada empregado está. 

# Análise do Algoritmo
O que mais demora é encontrar o chefe mais novo, que leva O(N + E), e é executado I vezes, que é o número de instruções, então o tempo é O(I(N + E))