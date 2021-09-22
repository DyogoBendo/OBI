[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia por trás do problema, é percebê-lo como uma soma binária qualquer, o único detalhe é que devemos ignorar, no resultado, os dígitos que são 0 até aparecer o primeiro digito que é 1. 


# Análise do Algoritmo
Como verificamos cada um dos dígitos dos dois números, o tempo é dominado pelo número de dígitos, digamos n, então a solução é O(n). 