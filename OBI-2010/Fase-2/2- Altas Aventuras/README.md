[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Bom, eu não resolvi o problema. Não passa em todos os casos de testes, mas passa nos mais "difíceis". 
O que acontece é que a minha lógica funciona para valores grandes, especialmente de k. 
A ideia é a seguinte: os balões são como um vetor ordenado, e queremos encontrar um valor qualquer nesse valor, qual a menor maior quantidade de "perguntas" de qual valor é precisamos fazer pra encontrar o valor? lg n. 
Isso porque é como se estivéssemos fazendo uma busca binária, então vamos dividindo o vetor na metade até encontrarmos o valor procurado. 
E é isso que meu algoritmo prevê: se for possível fazer log n divisões, então a solução é exatamente log n. Senão, dividimos o quanto pudermos por 2, e depois verificamos um a um. 
Essa solução funciona muito bem para valores grandes, mas para valores pequenos, como n = 20 e k = 2, ele definitivamente não dá certo. 

# Análise do Algoritmo
O algoritmo é executado no pior dos casos O(lg n). 