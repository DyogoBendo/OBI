[Formatação utilizada](https://katex.org/docs/supported.html)

# Análise do Problema

O problema de certa forma é bem simples. Precisamos ler quais os programas instalados nos computadores e suas respectivas versões. Depois, comparar com os programas presentes da internet. Se existir algum programa na internet que não está presente no computador, ou em uma versão mais nova, devemos imprimir o programa e sua versão mais recente. 

A ideia que eu usei para resolver foi mais simples ainda: criei um dicionário para os programas existentes no computador, em que as chaves são o número identificador do programa, e o valor é a versão. 

Para as programas na internet, a lógica é similar, a única diferença, é que devemos salvar apenas uma versão do programa, a mais recente, nesses dicionários. Para isso, sempre que vamos salvar algum programa no dicionário, verificamos se ele já está presente. Se estiver, verificamos se a versão é maior do que a que estava salva anterior, e colocamos  maior. Se não estava, simplesmente adiocionamos no dicionário. 

Agora, basta percorrer cada uma das chaves do dicionário de programas da internet. Verificamos se o programa que está na internet está no computador. Se não estiver, imprimimos. Se estiver, verificamos se a versão da internet é superior a do computador, se sim, imprimimos. 

# Análise do Algoritmo 

De forma geral, podemos constatar que o algoritmo é linear: 
- As linhas 2 a 17 tratam da entrada de dados
    - Linhas 2 a 4 são constantes
    - Linhas 5 a 7 executadas c vezes
    - Linhas 9 a 15 executadas n vezes
- Linhas 17 a 22 executadas n vezes

Temos então que as linhas são executadas n ou c vezes, então de forma intuitiva, podemos considerar que o limite assintótico superior do algoritmo é O(n) + O(c)


# [Análise de Tempo](https://www.inf.ufpr.br/maratona/tle.html)
A função pensada na resolução é uma função linear, então, considerando que a maior entrada é 10000 para c e 1000 para n:

$$
f(n) = n -> f(10^ 3) = 10 ^ 3
$$

$$
f(c) = c -> f(10^ 4) = 10 ^ 4
$$


$$
10 ^ 3 + 10 ^ 4 < 10 ^ 7
$$

Logo, podemos precisar que o algoritmo atende a necessidade de tempo. 