[Formatação utilizada](https://katex.org/docs/supported.html)

# Análise do Problema

Um móbile é bem balanceado quando para cada peça, todos os sub móbiles pendurados nela são compostos pelo mesmo número de peças.

        |
       / \
      /\ /\

Nesse exemplo, a primeira peça (linha 7), tem suas subpeças (linhas 8), e ambas são compostas por 4 peças (todas as suas subpeças, elas mesmas, e a peça raiz) 

A primeira subpeça (linha 8) possui 2 subpeças (linha 9), e cada uma delas é composta pelo mesmo número de peças(2) e o mesmo vale para a segunda subpeça (linha 8)

Precisamos identificar se o móbile está bem balanceado. 

Nesse caso, percebe-se a formação de uma estrutura de árvore, na realidade, uma estrutura de heap, já que uma peça raiz sempre será formada por mais peças que uma subpeça. 

Para resolvermos isso, basta que percorremos cada elemento do heap, um a um, e comparamos elementos de um mesmo nível se eles possuem o mesmo valor. 

A fim de se implementar, foi-se pensado no seguinte: 

Cada peça deveria ter as informações necessárias para que a heap fosse percorrida de cima para baixo. Nesse caso, era necessário que cada peça "soubesse" quem eram suas filhas. 

Como o enunciado informa apenas quem são as mães de cada peça, pensei em alguma forma de armazenar quais eram as mães que apareciam, e em qual posição de localizava o elemento que tinha aquela mãe. 

Assim, depois de receber todos os dados passados para a resolução do problema, bastava percorrer a heap, e adicionando em cada um dos elementos a posição na heap de cada um de seus filhos. 

Tendo feito isso, o processo se torna simples: criei um método recursivo: 
- Se a heap não continha filhos ela retorna o valor 1, pois é esse o valor que ela vale para a sua mãe
- Se a heap possui filhos, seria feito uma chamada recursiva, para cada um de seus filhos, analisando qual o valor eles representavam 

Para realizar a comparação se um nível estava equilibrado, o que era o objetivo do exercício, cada valor que os filhos representam é pego, e colocado em um set. 

Como o set aceita apenas valores únicos, se houver mais de um elemento, quer dizer que ela está desequilibrada.  

Sempre que ela está desequilibrada, aquela peça passa a contar 0. Sempre que a heap possuir apenas um 0, ela se torna inválida

Como todas as filhas de um caso podem estar desequilibradas, não podemos considerar esse caso correto, e então verificamos se o set contém apenas um valor, e se esse valor é diferente de 0. 

Se for o caso, retornamos o valor da soma de todos os filhos + 1, pois a peça representa todas as suas filhas, mais ela mesma, para a sua peça mãe. 

# Análise do Algoritmo 
- A declaração da classe Peca possui tempo constante (6 linhas) 
- A declaração da função calcula_peca é constante (35 linhas, contando comentários) 
- Receber o número de entradas, declarar o vetor heap, e o dicionário maes_filhos possui tempo constante (8 linhas)
- As linhas 58 é executada n + 1 vezes
- As linhas 59 e 62 são executadas n vezes
- As linhas 63 e 66 são executadas n vezes 
- As linhas 67 e 69 podem ser executadas n vezes no pior caso, e nenhuma vez no melhor caso
- A linha 72 é executada n vezes
- A linha 74 é executada n vezes
- As linhas 76 e 77 são executadas n vezes
- A linha 78 é executada n vezes no pior dos casos e 0 vezes no melhor dos casos
- A linha 86 tem tempo constante
- A linha 91 chama a função, então o tempo da função será analisado separadamente, mas seu tempo é constante
- As linhas 92 à 94 são constantes. 
- A função calcula_peca, linha 9, apresenta a seguinte soma de tempo:
      - linha 14 é uma constante, que vai ser executada n vezes
      - linhas 15 à 17 vão ser executadas n - 1 vezes no pior dos casos, e no melhor dos casos 1 vez
      - linha 20 é constante, e pode ser executada 1 vez no melhor dos casos, e n - 1 vezes no pior dos casos
      - linha 22 pode ser executada n vezes no pior dos casos, e 2 vezes no melhor dos casos
      - linhas 24 e 27 serão executadas 1 vez no melhor dos casos, ou n - 1 vezes no pior dos casos
      - linhas 33, 34 são constantes, e serão executadas n-1 vezes no pior dos casos ou nenhuma no melhor dos casos
      - 41, 46 são constantes, que podem ser executadas 0 ou n-1 vezes  

A motivo dessa constatação de tempos é simples: a função serve para percorrer um a um os elementos do heap. Se todos os filhos da raíz forem folhas, a linha 14 é executada n-1 vezes. Se houver apenas uma folha, será executada apenas uma vez. 

Se todos os filhos da raíz forem folhas, então temos que o for é executado n-1 vezes, assim como o que houver dentro dele. No entanto, nesse caso, a definição da fila, e o testes de valores, ocorre apenas 1 vez. 

De forma indutiva, é possível notar que o caso básico, da linha 14, é executado igual ao número de folhas do heap, pois são todos os elementos sem filhos. O set e os testes de valores se executados de acordo com o número de não-folhas do heap. Já o for, é igual a quantidade de filhos. Isso porque, é percorrido os valores de todos os elementos descendentes da raíz, mas não ela, ou seja, n-1 vezes.  

A soma então desses valores é igual a: 
- f = número de folhas
- nf = número de não folhas
- n = número de peças
- n = nf + f

Temos então: f + nf  + n + n - 1 + nf = n + n + n - 1 + n  -> (consideramos nf como n para arredondamento)

$$
4n - 1 = O(f(n)) -> f(n) = cn
$$

$$
cn >= 4n - 1 ->  4n >= 4n - 1
$$

c = 4, para todo n >= 0

Somando com o tempo de execuções anteriores temos: 
$$
4n - 1 + 19 + 8n = 12n + 18 = O(n)
$$

$$
12n + 18 <= cn -> 12n + 18 <= 20n \  \forall  \ n >= \ \frac{9}{4}
$$

Consideramos c como 20 então, podemos assim afirmar que o algoritmo possui resolução O(n)

# [Análise de Tempo](https://www.inf.ufpr.br/maratona/tle.html)

Para a análise de tempo, devemos considerar: 

$$
f(10 ^ 4 ) <= 10 ^ 7
$$
Como o algoritmo é linear: 
$$
f(10 ^ 4) = 10 ^ 4 <= 10 ^ 7
$$

O algoritmo então atende aos requisitos de tempo impostos pelo exercício. 