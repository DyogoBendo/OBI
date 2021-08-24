#include <cstdio>

int N, M;

int main(void) {

    int pessoas = 0;
    int excedeu = 0;

    scanf("%d%d", &N, &M);

    for(int i = 0; i < N; ++i) {
        int s, e;
        scanf("%d%d", &s, &e);
        pessoas += e - s;
        if(pessoas > M) {
            excedeu = 1;
        }
    }

    printf("%c\n", excedeu?'S':'N');

    return 0;
}
