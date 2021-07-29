#include <stdio.h>

int cad[210][210], lin[210], col[210], mark[210];

int main () {

    int m, n;

    scanf ("%d %d", &m, &n);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cad[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        col[i] = (cad[0][i]-1)%n;
        mark[i] = 0;
    }

    int mc[210][2], ml[210][2], nc = 0, nl = 0;

    for (int i = 0; i < n; i++) {
        if (mark[i] == 1) continue;
        int atual = col[i];
            
        while (atual != i) {
            mc[nc][0] = atual+1;
            mc[nc][1] = col[atual]+1;
            nc++;
            //printf("C %d %d\n", atual+1, col[atual]+1);
            mark[atual] = 1;
            atual = col[atual];
            //printf("i %d at %d\n", i, atual);
        }
        
    }


    for (int i = 0; i < m; i++) {
        lin[i] = (cad[i][0]-1)/n;
        mark[i] = 0;
    }

    for (int i = 0; i < m; i++) {
        if (mark[i] == 1) continue;
        int atual = lin[i];
            
        while (atual != i) {
            ml[nl][0] = atual+1;
            ml[nl][1] = lin[atual]+1;
            nl++;
            //printf("L %d %d\n", atual+1, lin[atual]+1);
            mark[atual] = 1;
            atual = lin[atual];
        }
    }

    printf ("%d\n", nc+nl);
    for (int i = 0; i < nl; i++)
        printf("L %d %d\n", ml[i][0], ml[i][1]);
    for (int i = 0; i < nc; i++)
        printf("C %d %d\n", mc[i][0], mc[i][1]);

    return 0;
}
/*
3 4
1 4 2 3
9 10 11 12
5 6 7 8
*/
