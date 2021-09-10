[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia para resolver esse problema é testar todas as posições possíveis. Verificamos cada posição e comparamos com as pistas dadas, se a distância em relação a todas as pistas for a esperada, então é um caso possível. Basta então verificar se é o primeiro par de coordenadas que "bate" ou não, para informar a coordenada final corretamente. 

# Análise do Algoritmo
O algoritmo percorre cada uma das posições e para cada posição, testa cada uma das pistas, assim, o tempo de complexidade é: O(k n ^ 2)
