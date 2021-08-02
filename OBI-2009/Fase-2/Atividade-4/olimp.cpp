#include <stdio.h>
#include <math.h>

int main () {

    int m, n, vec[110], aux;

    scanf("%d %d", &n, &m);

    for (int i = 0; i < m; i++)
            vec[i] = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < 3; j++) {
            scanf ("%d", &aux);
            vec[aux-1] += pow(110,2-j);
        }
    }
/*
    for (int i = 0; i < n; i++)
        printf ("%d ", vec[i]);
    printf("\n");
*/    
    for (int i = 0; i < n; i++) {
        int ma = -1;
        int mw = -1;
        for (int j = 0; j < n; j++) {
            if (vec[j] > ma) {
                ma = vec[j];
                mw = j;
            }
        }
        printf("%d ", mw+1);
        vec[mw] = -2;
    }

    return 0;
}
