[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Eu não consegui resolver esse problema adequadamente (falha em um caso de teste). Mas a lógica que eu utilizei é a seguinte: podemos utilizar uma lista de tamanho m, sendo m o número de caracteres da sequência de dígitos. 
Começamos a preencher ela de baixo para cima, ou seja, a informação do último dígito até o primeiro. O valor que é inserido é a soma de números possíveis que podem ser formados a partir daquele dígito. 
O último dígito sempre tem um caso válido e apenas um, que é ele mesmo. Consideramos que o número de letras no nosso alfabeto seja n. Então, do segundo ao n-ésimo digito, vamos avaliar cada vez i casos, sendo i o número de digitos. Se i for 5, então temos que analisar as "palavras" formadas por: 1 dígito, 2 dígitos, 3 dígitos, 4 dígitos, 5 dígitos. 
E quantas possibilidades existem para quando formamos cada uma das palavras? Se usarmos i dígitos, então o número de possibilidades é 1, isso porque usamos todos os dígitos disponíveis, então só uma palavra é possível. Agora se usarmos i - k digitos, o número de possibilidade é quantas possibilidades temos quando i era i - k, pois "vira" o caso em que tinhamos i - k dígitos. Então basta guardarmos a informação de cada i e usar posteriormente. 
Depois de passarmos do n-ésimo dígito, não teremos mais o caso de pegar todos os dígitos e não sobrar nenhum, assim, quando pegamos i dígitos, ainda irá sobrar uma quantidade k de digitos, e analisamos quantas possibilidades temos com k dígitos. Após analisar cada uma delas separadas, somamos todas as possibilidades com i dígitos e guardamos.
No entanto, se o i-ésimo digito for 0, não existe nenhuma possibilidade válida iniciando por ele, assim como se pegarmos k dígitos e o número resultante for maior que o tamanho do alfabeto, também desconsideramos essa possibilidade. 
O resultado para o problema sempre estará na posição 0 dessa lista, pois ela analisa o caso partindo do primeiro número, quantas possibilidades são possíveis. 

# Análise do Algoritmo

A solução tem complexidade O(nm), sendo n o tamanho do alfabeto e m o tamanho da sequência. 