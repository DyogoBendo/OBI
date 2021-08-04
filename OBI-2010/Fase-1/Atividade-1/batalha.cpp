#include <cstdio>
#include <cstring>

#define MAXN 100
#define MAXM 100

int N, M, K, T;

char tabuleiro[MAXN][MAXM+1];

int navio[MAXN][MAXM];

int tamanho[MAXN*MAXM];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int marca_navio(int i, int j, int id) {
    int ret = 1;

    navio[i][j] = id;
    for(int d = 0; d < 4; ++d)  {
        int i2 = i + dy[d];
        int j2 = j + dx[d];
        if(i2 < 0 or j2 < 0 or i2 >= N or j2 >= M) {
            continue;
        }
        if(tabuleiro[i2][j2] == '#' and navio[i2][j2] == -1) {
            ret += marca_navio(i2, j2, id);
        }
    }
    return ret;
}

int main(void) {

    scanf("%d%d", &N, &M);

    for(int i = 0; i < N; ++i) {
        scanf("%s", tabuleiro[i]);
        for(int j = 0; j < M; ++j) {
            navio[i][j] = -1;
        }
    }

    K = 0;

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < M; ++j) {
            if(navio[i][j] == -1 and tabuleiro[i][j] == '#') {
                tamanho[K] = marca_navio(i, j, K);
                K++;
            }
        }
    }

    int destruidos = 0;

    scanf("%d", &T);

    for(int k = 0; k < T; ++k) {
        int i, j;
        scanf("%d%d", &i, &j);
        i--; j--;
        if(navio[i][j] != -1) {
            tamanho[navio[i][j]] --;
            if(tamanho[navio[i][j]] == 0) {
                destruidos ++;
            }
            navio[i][j] = -1;
        }
    }

    printf("%d\n", destruidos);

    return 0;
}
