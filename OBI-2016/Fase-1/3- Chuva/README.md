[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
A ideia de resolução do problema, é que as seções que estão cobertas por água estão entre duas seções que são maiores que qualquer uma delas. Por exemplo se temos as alturas das seções 5, 3, 4, 2, 1, 5; todas as seções entre os dois 5 estão cobertas de água. 

Podemos partir da esquerda para a direita, definimos o tamanho da nossa seção esquerda como m. Se encontrarmos uma seção que é >= m, então todas as seções que estão entre elas devem ser contadas. E agora, m passa ser essa seção maior, e vamos até encontrar a próxima. 

Se não encontrarmos nenhuma maior, e chegarmos ao final, podem existir seções máximas que foram contadas mas que não deveriam. Então usamos a mesma lógica, só que da direita para a esquerda, com m sendo a altura da seção mais a direita, e sempre que encontrarmos uma seção maior, iremos descontar um. 

# Análise do Algoritmo
Como verificamos cada seção no máximo 2 vezes, o tempo de execução é O(n). 