[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia para a solução é contar quantas botas em cada tamanho em cada pé (direito/esquerdo) existem. Depois, o número de pares formados será a soma de pares possíveis em cada tamanho. O número de par possível em um determinado tamanho é o menor número de botas de um dos pés, já que ele limita a quantidade pares que podem ser formados. 

# Análise do Algoritmo
Como verificamos todas as botas e todos os tamanhos de botas o tempo de execução é O(N + M)