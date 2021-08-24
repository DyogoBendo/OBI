#include <cstdio>

int main() {
  
  // basta fazer o numero E ser o indice de um vetor de registros. cada
  // registro salva a letra e o proximo indice (numero D)
  for (int N; scanf("%d", &N) == 1 && (N);) {
    static struct {
      char c;
      int D;
    } vet[200001];
    for (int n = 0; n < N; n++) {
      int E;
      scanf("%d ", &E);
      scanf("%c %d", &vet[E].c, &vet[E].D);
    }
    int E;
    for (E = 0; E != 1; E = vet[E].D) {
      printf("%c", vet[E].c);
    }
    printf("\n");
  }
  
  return 0;
}
