[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O problema é uma questão de filas e filas de prioridade. Cada pessoa deve ser pega na ordem que chega, e o caixa escolhido para cada pessoa é o de maior prioridade: o que termina o atendimento primeiro.

# Análise do Algoritmo
Como temos que atender cada pessoa e em cada pessoa pegamos o caixa de maior prioridade e o adicionamos de volta com o tempo modificado, o tempo de execução do programa é O(n log c), já que inserir um elemento em um heap demora O(lg n). 
