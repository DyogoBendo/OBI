[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Nesse problema, podemos pensar da seguinte forma: cada pasta está em um nível em relação a raiz. Em cada uma dessas pastas, temos um número de subpastas e arquivos que são afetados quando iniciamos por elas, por estarem contido nela e terem o número de caracteres reduzidos em seu caminho pelo número de caracteres do nome da pasta, e as outras pastas e arquivos, que não estão contidos, e que terem o número de caracteres aumentado em 3, pois será necessário sair daquela pasta para chegar nelas. 

O que fazemos no programa é calcular o número de subpastas de cada pasta, e comparar cada relação de caracteres partindo de cada uma dessas pastas. 

É importante notar que a chamada para realizar o cálculo é recursivo, porque a ideia de adicionar "../" para cada uma das pastas que não estão contidas, ocorre porque já adicionamos os "../" da pasta pai (se tiver), assim, a adição de "../" e a remoção do nome da pasta, é em relação ao caminho do pai daquela pasta. Como os testes começam nos filhos da raiz, então verificamos todos os casos, e cada chamada é relativa a situação do pai da pasta. 

# Análise do Algoritmo
O algoritmo tem um fator constante bem alto, porque executamos várias chamadas, vários loops, várias funções, mas em geral, podemos dizer que o programa tem tempo O(n), que é o tempo de verificar cada uma das n pastas. 