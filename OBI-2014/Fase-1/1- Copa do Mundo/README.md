[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
O problema é claramente um árvore geradora mínima, pois queremos ligar todas as cidades (vértices), ao menor custo. A única diferença, é que existem dois tipos de arestas: ferroviais e rodovias. Mesmo com uma ferrovia sendo mais cara que uma rodovia, ela deve ser priorizada. 

É isso que fazemos, a ferrovia sempre terá uma prioridade maior. Então na nossa ligação dos vértices, pelas ferrovias terem uma maior prioridade, serem consideradas sempre que possível primeiro que uma rodovia, ao ligar duas cidades. 

# Análise do Algoritmo
Como utilizamos o algoritmo de Prim para a resolução, o tempo de execução é O((f + r) log n)