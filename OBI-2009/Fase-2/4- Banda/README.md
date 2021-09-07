[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos encontrar o trio que maximiza o entrosamento. A ideia de solução é simples: força bruta. Podemos testar todas as combinações de trios, e o que tiver maior entrosamento será o escolhido. 

# Análise do Algoritmo
O algoritmo é executado O(n^ 3), já que para cada músico, testamos com cada músico que testa com cada músico. Ou, de forma mais clara, testamos cada uma das O(n^ 2) duplas com O(n) músicos. 