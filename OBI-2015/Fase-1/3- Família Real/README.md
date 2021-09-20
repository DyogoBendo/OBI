[Formatação utilizada](https://katex.org/docs/supported.html)
# Análise do Problema
Esse é um problema que podemos pensar como um grafo de certa forma. Partindo do rei, queremos descobrir as gerações. Então, basta fazermos uma busca em largura, descobrindo assim a qual geração relativa ao rei cada pessoa pertence. Depois, contamos quantas pessoas de cada geração existem e quantas participaram da festa. 

# Análise do Algoritmo
A busca em largura visita exatamente cada pessoa uma vez e suas relações, que não é muito explícito, mas podemos simplificar como O(n), que é o que domina o tempo de execução, junto com a verificação de cada um dos presentes, que lava O(m), por isso a solução é O(n + m). 