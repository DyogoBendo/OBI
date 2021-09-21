[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, o mais importante é achar algum padrão de contagem. No caso, eu dividi em três casos:
- Quando M é maior que N: então todas as possibilidades são possíveis. Por exemplo, para N = 100 e M = 200, podemos pensar em todas as possibilidades. Olhando-as, podemos perceber que se o primeiro pegar 1 palito, os outros dois devem somar de forma a dar 99, e isso pode ser feito de 99 formas diferentes, se o primeiro pegar 2 palitos, os outros dois devem somar 98. tendo 98 possibilidades e assim sucessivamente. 
- Quando M é menor que metade de N: temos um limite bem restritivo de possibilidades, encontramos qual o menor valor que podemos pegar de palitos, e vamos testando as possibilidades até chegar em M palitos.
- Quando M é maior que a metade de N: nesse caso, podemos partir de 0, e ir verificando as possibilidades até M, no entanto, apesar de sempre conseguirmos somar até N com os outros dois palitos, eles não podem assumir qualquer valor, o que restringe a faixa de valores aceitos até M. 

# Análise do Algoritmo
Como verificamos com o primeiro iniciando com cada valor de palito, temos no pior caso O(n) execuções. 