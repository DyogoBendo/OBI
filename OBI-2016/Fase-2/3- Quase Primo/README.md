[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia que podemos utilizar, é encontrar a quantidade de múltiplos até n de cada um dos primos, subtraindo do total. No entanto, devemos tomar cuidado quando existem intersecções nos múltiplos de dois primos, que devemos somar de volta ao total. 

# Análise do Algoritmo
Eu não sei expressar exatamente o tempo desse problema, mas ele depende apenas de k, e não de n. O que devemos testar é cada combinação de múltiplos. Então testar o 1, 2, 3, ..., k primo. Depois cada um deles combinado em pares: (1, 2), (1, 3), ..., (1, k), em trios, etc. Até testarmos (1, 2, 3,... k) multiplicado em um único número.
