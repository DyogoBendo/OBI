/*
 * Solução do problema 'Reunião' (OBI 2010 - Nível 2, Fase 1)
 *
 * Maurício de Lemos Rodrigues Collares Neto (<mauricioc@gmail.com>)
 *
 * Este arquivo implementa a solução usual para o problema de calcular o diâme-
 * tro de um grafo, que é o nome técnico dado ao que a questão pede.
 *
 * A idéia desta solução é computar, para cada um dos pares de cidades (u,v),
 * a menor distância entre u e v usando o algoritmo de menor caminho de 
 * Floyd-Warshall. Tendo esta informação, podemos tentar colocar o ponto de 
 * encontro dos caminhoneiros em cada uma das cidades, verificando qual delas 
 * faz com que a maior distância percorrida pelos caminhoneiros seja a menor 
 * possível.
 *
 * O tempo necessário para a execução deste algoritmo é dominado pelo algorit-
 * mo de Floyd-Warshall, e portanto a solução executa em tempo proporcional a
 * n^3. 
 * 
 * O mesmo problema, com outra história, apareceu na prova da OBI de 2006, no 
 * mesmo nível (programação nível 2, fase 1, questão 'Lanche na empresa').
 */

#include <cstdio>
#include <algorithm>

using namespace std;

/* O maior caminho possível para um caminhoneiro passa por todas as cidades
 * (e portanto por n-1 estradas), cada uma com custo no máximo 100, donde
 * qualquer valor maior que 99*100 serve para esta constante. Usaremos um
 * valor maior por questão de costume. */
const int INF = 1000000000;

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    int dist[n][n];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            dist[i][j] = INF;

    /* A menor distância entre uma cidade e ela mesma é zero. */
    for(int i = 0; i < n; i++)
        dist[i][i] = 0;

    for(int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);

        /* Atualizando a menor distância entre u e v. Vale lembrar que, como
         * pode haver mais de um par de estradas ligando o mesmo par de cidades,
         * tomar o mínimo entre o valor atual e o novo é importante. */
        dist[u][v] = min(dist[u][v], w);

        /* Não esquecer de atualizar o custo de ir no sentido oposto, já
         * que as estradas são todas bidirecionais. */
        dist[v][u] = dist[u][v];
    }

    /* Este é o algoritmo de Floyd-Warshall. Uma explicação detalhada sobre ele
     * pode ser encontrada no Wikipedia, no seguinte endereço:
     * http://pt.wikipedia.org/wiki/Algoritmo_de_Floyd-Warshall
     *
     * Ao final de sua execução, dist[u][v] é a menor distância que tem que ser
     * percorrida para ir de u a v, possivelmente usando cidades e estradas
     * intermediárias. */
    for(int k = 0; k < n; k++)
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]);

    int resp = INF;
    /* A i-ésima iteração deste loop corresponde a tomar a cidade i como
     * o ponto de encontro dos caminhoneiros. */     
    for(int i = 0; i < n; i++) {
        /* Calculamos a maior distância que um caminhoneiro tem que percorrer 
           para chegar em i partindo de alguma outra cidade... */
        int max_dist = 0;
        for(int j = 0; j < n; j++)
            max_dist = max(max_dist, dist[i][j]);

        /* ...e verificamos se este valor é melhor que o que já encontramos
         * até agora, atualizando a variável resp caso seja. */
        resp = min(resp, max_dist);
    }

    printf("%d\n", resp);
}
