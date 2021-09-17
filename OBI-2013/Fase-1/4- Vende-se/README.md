[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Inicialmente, ordemos a lista de prédio, de formo que temos o primeiro elemento sendo o mais próximo da avenida e o último o mais distante. 
Após isso, verificamos da esquerda para direita, cada conjunto seguido de prédios, partindo de i e indo até i + n - k, e calculamos a distância do primeiro e do último, que é a maior distância desse conjunto, e verificamos se é a menor possível. 

# Análise do Algoritmo
Como verificamos cada um dos prédios como sendo o mais próximo da avenida de um conjunto, o tempo de execução é O(n). 