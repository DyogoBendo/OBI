[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, precisamos verificar cada posição do pacman no tabuleiro, e manter quanta comida ele possuí. Se a quantidade que ele possuí em algum momento for superior ao máximo que temos de comida, esse se torna o novo máximo. 

# Análise do Algoritmo
Como verificamos cada posição do tabuleiro, e ele tem as dimensões N x N, então a solução tem tempo O(n ^ 2). 