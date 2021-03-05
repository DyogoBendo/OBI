[Formatação utilizada](https://katex.org/docs/supported.html)

# Análise do Problema

O problema pede para que respondamos se é possível arquivar de forma perfeita a pasta. Para isso, é necessário que: 
- Para um elemento de aba < P, sendo P a maior aba, sempre deve ter um sucessor que tem o seu valor de aba + 1 ou nenhum. 
- Se a aba do elemento for P, então o sucessor deve ser 1 ou nenhum
- Todos os elementos devem ser armazenados. 

Bem, podemos iniciar de qualquer ordem. Ou seja, se temos as posições de aba (1, 2, 3, 4), podemos arquivar formando as seguintes sequências: 

- 1, 2, 3, 4, 1, 2...
- 2, 3, 4, 1, 2, 3...
- 3, 4, 1, 2, 3, 4...
- 4, 1, 2, 3, 4, 1...

Algo interessante, é começar sempre pela posição que mais aparece, porque assim, ela pode aparecer mais que as outras (na primeira e na última posição). Por exemplo, supomos que temos os valores (1, 2, 3, 3, 4), podemos iniciar pelo 3, e finalizar pelo 3, essa é a única forma de manter a sequência e ter todos os elementos incluídos: 

- 3, 4, 1, 2, 3

Qualquer outra forma de ordenação é falha.  

Agora, vejamos se temos duas posições que aparecem mais frequentemente (1, 2, 3, 3, 4, 4). Seguindo pela lógica anterior, poderíamos ordenar de duas formas: 

- 3, 4, 1, 2, 3, 4
- 4, 1, 2, 3, 4, 1 X 

A segunda opção de mostra falha. Isso porque, quem sucede o 4 é o 1, que não é um dos que aparece mais frequentemente. De forma intuitiva, podemos considerar duas coisas até aqui então:

- Devemos iniciar sempre por uma posição que aparece com maior frequência. 
- Se houverem mais de duas posições com maior frequência, escolhemos a de menor valor

Mas, essa segunda constatação pode se mostrar falha em outro caso. Consideremos as posições (1, 1, 2, 3, 3, 4), se seguirmos o que foi proposto, teremos: 

- 1, 2, 3, 4, 1, 2 X

Se mostra falho novamente, isso porque, mesmo que o 1 seja menor que o 3, eles não estão em sequência. Corrigindo a proposição anterior, temos: 

- Se houverem duas ou mais posições com maior frequência, elas devem estar em sequência. Se for o caso, escolhemos a menor posição para iniciar. 

Outro detalhe, é que, não é sempre que uma posição com maior frequência permite uma sequência válida. Por exemplo: (1, 1, 1, 2, 3, 4)

- 1, 2, 3, 4, 1, 2 X

Podemos generalizar para que sempre que houver um elemento que a frequência é ao menos 2 a mais que o elemento que menos aparece, então é impossível formar uma sequência válida. 

Assim, podemos considerar as seguintes proposições para formular o código: 

- Devemos observar a frequência que cada elemento aparece
    - Se a frequência que um elemento aparece é 2 maior que a do elemento com menor frequência, então a sequência é inválida
    - Se os elementos com maior frequência não estiverem em sequência, então também temos uma situação inválida
    - Se os elementos de maior frequência estiverem em sequência, e a distância deles para o elemento de menor frequência é apenas 1, então, devemos iniciar pelo menor elemento dos que aparecem com maior frequência. 