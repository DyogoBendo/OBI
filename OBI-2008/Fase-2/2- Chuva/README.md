[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos encontrar qual a quantidade mínimade terreno que o robô precisa passar na chuva. 

Para fazer isso, a ideia é pensar em algoritmo guloso. Partindo do ponto inicial, verificamos o retângulo que possuí o menor custo para se chegar, logicamente, não existe nenhuma forma de se chegar a ele por um custo menor, então após ele ser considerado, verificamos o custo de cada retângulo em relação a ele, o que tiver o menor custo sendo feito isso será o próximo, e assim sucessivamente até termos calculado o menor custo para se chegar em todos os retângulos. É muito similar ao algoritmo de Dijkstra. 

# Análise do Algoritmo
Para calcular a distância entre cada par de retângulos, demoramos O(n^2). Esse é o mesmo tempo para o cálculo da menor distância em relação ao ponto inicial, já que ele é executado também no tempo O(n^2), mas possuí uma constante de tempo maior, já que a retirada do elemento de maior prioridade demora O(log n) e é executada n vezes. 
